"""
manager.py
----------
Coordinates the student and job objects with the analyzers,
then prints a complete analysis report.
"""

from analyzers import MatchScoreCalculator, MissingSkillDetector


class Manager:
    """
    Accepts a student and a job, runs both analyzers through
    the shared SkillAnalyzer interface (polymorphism), and
    displays the full report.
    """

    def __init__(self, student, job):
        self._student = student
        self._job = job
        # Both objects share the same analyze() interface
        self._analyzers = [
            MatchScoreCalculator(),
            MissingSkillDetector(),
        ]

    def run_analysis(self):
        """
        Run every analyzer using polymorphism.
        Each object responds to analyze() in its own way.
        """
        match_result = None
        missing_skills = None

        for analyzer in self._analyzers:
            result = analyzer.analyze(self._student, self._job)

            # Identify results by type returned from each analyzer
            if isinstance(result, dict):
                match_result = result
            else:
                missing_skills = result

        self._display_report(match_result, missing_skills)

    def _display_report(self, match_result, missing_skills):
        """Print the complete student–job skill analysis report."""
        print("=" * 50)
        print("STUDENT–JOB SKILL ANALYSIS REPORT")
        print("=" * 50)
        print()
        print("Student Name:", self._student.get_name())
        print()
        print("Job Title:", self._job.get_title())
        print()
        print("Required Skills:", match_result["total_required"])
        print()

        print("Matching Skills:")
        if len(match_result["matching_skills"]) == 0:
            print("- None")
        else:
            for skill in match_result["matching_skills"]:
                print("-", skill)
        print()

        print("Missing Skills:")
        if len(missing_skills) == 0:
            print("- None")
        else:
            for skill in missing_skills:
                print("-", skill)
        print()

        # Show whole-number percentage when possible (e.g. 40%)
        percentage = match_result["percentage"]
        if percentage == int(percentage):
            print("Match Score: {}%".format(int(percentage)))
        else:
            print("Match Score: {:.1f}%".format(percentage))
        print()

        print("Explanation:")
        print(
            "The student matches {} out of {} unique required skills. "
            "Therefore, the skill match percentage is {}%.".format(
                match_result["match_count"],
                match_result["total_required"],
                int(percentage) if percentage == int(percentage) else round(percentage, 1),
            )
        )
        print()
