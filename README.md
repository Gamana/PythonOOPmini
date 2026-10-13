# Student–Job Skill Analysis System

A beginner-friendly Python mini-project that compares a student's technical skills with a job description and reports the match score, matching skills, and missing skills.

Built with **Object-Oriented Programming (OOP)** using only core Python (no database, no external libraries).

## How to Run

```bash
cd student_job_analyzer
python main.py
```

## Project Structure

```
student_job_analyzer/
├── main.py          # Sample data, demos, and edge-case tests
├── models.py        # StudentProfile and JobDescription
├── analyzers.py     # SkillAnalyzer, MatchScoreCalculator, MissingSkillDetector
├── manager.py       # Manager that runs analyzers and prints the report
└── README.md        # This file
```

## Classes and Responsibilities

| Class | File | Responsibility |
|-------|------|----------------|
| `StudentProfile` | `models.py` | Store student name and skills; normalize skills |
| `JobDescription` | `models.py` | Store job title and required skills; normalize skills; handle empty lists |
| `SkillAnalyzer` | `analyzers.py` | Abstract base class with a common `analyze()` method |
| `MatchScoreCalculator` | `analyzers.py` | Count matches and calculate match percentage |
| `MissingSkillDetector` | `analyzers.py` | Find skills the student is missing |
| `Manager` | `manager.py` | Run both analyzers and display the full report |

## Match Formula

```
Match Percentage = (Number of Matching Skills / Total Required Skills) × 100
```

If a job has **no required skills**, the match score is **0%** (avoids division by zero).

## Matching Rules

- Case-insensitive (`Python` matches `python`)
- Leading/trailing spaces are ignored
- Only full skill-name matches count
- Each unique skill is counted once
- Original readable names appear in the report
- Comparison uses **lists, loops, and conditions** (no sets)

## Sample Output (expected)

```
STUDENT–JOB SKILL ANALYSIS REPORT

Student Name: Gamana

Job Title: Python Developer

Required Skills: 5

Matching Skills:
- Python
- SQL

Missing Skills:
- Django
- REST API
- Git

Match Score: 40%

Explanation:
The student matches 2 out of 5 unique required skills. Therefore, the skill match percentage is 40%.
```

## Execution Flow (Step by Step)

1. `main.py` creates a `StudentProfile` with name and skills.
2. `main.py` creates one or more `JobDescription` objects.
3. Skills are normalized inside the model constructors (trim spaces, lowercase, remove duplicates).
4. A `Manager` is created with one student and one job.
5. `Manager` holds a list of analyzer objects: `MatchScoreCalculator` and `MissingSkillDetector`.
6. Using **polymorphism**, `Manager` calls `analyze(student, job)` on each analyzer.
7. `MatchScoreCalculator.analyze()` returns matching skills and the percentage.
8. `MissingSkillDetector.analyze()` returns the list of missing skills.
9. `Manager` prints the complete analysis report.
10. `main.py` repeats the process for a second job (same student) and for edge-case tests.

## Inheritance and Polymorphism in This Project

### Inheritance

- `SkillAnalyzer` is the **parent (abstract base) class**.
- `MatchScoreCalculator` and `MissingSkillDetector` are **child classes**.
- Both children inherit from `SkillAnalyzer` and **override** `analyze()`.

```
SkillAnalyzer (abstract)
 ├── MatchScoreCalculator   → analyze() calculates match %
 └── MissingSkillDetector   → analyze() finds missing skills
```

### Polymorphism

- `Manager` stores different analyzer objects in one list.
- It calls the **same method name** (`analyze`) on each object.
- Each object runs its **own version** of `analyze()`.
- The manager does not need separate code paths for each analyzer type.

### Encapsulation

- Attributes like `_student_name` and `_student_skills` are prefixed with `_` to mark them as internal.
- Outside code uses getter methods such as `get_name()` and `get_skills()`.

## Beginner-Friendly OOP Interview Questions

1. **What is a class, and what is an object?**  
   A class is a blueprint. An object is a concrete instance created from that blueprint (for example, one `StudentProfile` for Gamana).

2. **What is encapsulation, and how is it used here?**  
   Encapsulation means keeping data private inside a class and exposing it safely through methods. Skills are stored as `_student_skills` and accessed via `get_skills()`.

3. **What is inheritance?**  
   Inheritance lets a child class reuse and extend a parent class. Both analyzers inherit from `SkillAnalyzer`.

4. **What is an abstract base class?**  
   It defines a required interface (here, `analyze()`) but does not provide a full implementation. Child classes must override it.

5. **What is polymorphism?**  
   Different objects respond to the same method call in different ways. `Manager` calls `analyze()` on each analyzer, and each returns a different result.

6. **Why override `analyze()` in both child classes?**  
   Both need the same method name for a shared interface, but each performs a different task (score vs missing skills).

7. **What does “single responsibility” mean in this project?**  
   Each class has one job: models store data, calculators analyze, and `Manager` coordinates and displays results.

8. **How does this project avoid division by zero?**  
   If the job has zero required skills, `MatchScoreCalculator` returns 0% instead of dividing.

9. **Why normalize skills to lowercase?**  
   So matching is case-insensitive without changing how names are shown in the report.

10. **Why avoid sets in the core comparison logic?**  
    The exercise focuses on lists, loops, and conditions so beginners practice fundamental control flow.

## Edge Cases Covered

1. No matching skills  
2. All required skills present  
3. Partial match  
4. Student has no skills  
5. Job has no required skills  
6. Uppercase / lowercase variations  
7. Extra spaces in skill names  
8. Duplicate student skills  
9. Duplicate job skills  
10. Both skill lists empty  
