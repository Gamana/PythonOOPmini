# PythonOOPmini
Mini Project: Student–Job Skill Analysis System Using Python OOP
# Mini Project: Student–Job Skill Analysis System Using Python OOP

## Project Objective
Build a beginner-friendly Python mini-project that analyzes how well a student's technical skills match the requirements of a job description.

The project must use **Object-Oriented Programming (OOP)** and follow clean, modular Python code practices.

## 1. Technology Requirements
- Python 3
- Core Python concepts: lists, loops, conditions, and functions
- OOP concepts: classes, objects, encapsulation, inheritance, and polymorphism
- No database or external libraries
- Store sample student and job data directly in Python

## 2. Required Classes

### StudentProfile
Attributes:
- student_name
- student_skills

Responsibilities:
- Store student information.
- Normalize skills by removing extra spaces and converting them to lowercase.

### JobDescription
Attributes:
- job_title
- required_skills

Responsibilities:
- Store job information.
- Normalize required skills.
- Handle empty skill lists.

### MatchScoreCalculator
Responsibilities:
- Compare student skills with job requirements.
- Count matching skills.
- Calculate the match percentage.

Formula:

Match Percentage = (Number of Matching Skills / Total Required Skills) × 100

If a job has no required skills, return 0% to avoid division by zero.

### MissingSkillDetector
Responsibilities:
- Identify skills required by the job that the student does not possess.
- Return the missing skills as a list.
- Return an empty list when the student has all the required skills.

### Manager
Responsibilities:
- Accept a student and a job description.
- Run both analyzers.
- Display the complete analysis report.

## 3. OOP Requirements

1. Create a common abstract base class named `SkillAnalyzer`.
2. Make `MatchScoreCalculator` and `MissingSkillDetector` inherit from `SkillAnalyzer`.
3. Define a common `analyze()` method in the base class.
4. Override `analyze()` in both child classes.
5. Use polymorphism to execute both analyzers through the same interface.
6. Use encapsulation where appropriate.
7. Keep each class responsible for a single task.

## 4. Matching Rules

- Matching must be case-insensitive.
- Ignore leading and trailing spaces.
- A skill matches only when the complete skill name matches.
- Avoid counting the same skill more than once.
- Preserve the original readable skill names in the final report.
- Do not use sets or external libraries for the core comparison logic; use lists, loops, and conditions.
- Handle empty student skills, empty job requirements, and duplicate skills safely.

## 5. Sample Input

Student:

Name: Gamana

Skills:
Python, Java, SQL, HTML

Job:

Title: Python Developer

Required Skills:
Python, Django, SQL, REST API, Git

## 6. Expected Output

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

## 7. Testing Requirements

Test these scenarios:

1. Student has no matching skills.
2. Student has all required skills.
3. Student has only some required skills.
4. Student has no skills.
5. Job has no required skills.
6. Student and job skills contain uppercase and lowercase variations.
7. Skills contain extra spaces.
8. Student skills contain duplicates.
9. Job requirements contain duplicates.
10. Both student and job have empty skill lists.

## 8. Project Structure

Create the following structure:

student_job_analyzer/
- main.py
- models.py
- analyzers.py
- manager.py
- README.md

Keep the code simple enough for Python beginners to understand.

## 9. Execution Requirements

- Provide complete, working code for every file.
- Add sample data in `main.py`.
- Include clear explanations of the classes and their responsibilities.
- Add comments only where they help beginners understand important logic.
- Ensure the program runs using `python main.py`.
- Do not introduce unnecessary frameworks or advanced architecture.
- Explain how inheritance and polymorphism work in this project.
- Demonstrate at least two different job descriptions using the same student profile.

## 10. Final Deliverables

Generate the complete project in the current workspace. Before modifying existing files, inspect the workspace and preserve unrelated code.

After implementation:
1. Run the program.
2. Fix any errors.
3. Test the required edge cases.
4. Provide the final project structure.
5. Explain the execution flow step by step.
6. Provide beginner-friendly OOP interview questions based on this project.

Build a small, fully working educational project, not an unnecessarily complex enterprise application.
