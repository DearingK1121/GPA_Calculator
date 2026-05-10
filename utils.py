# utils.py

from datetime import datetime
import csv


def build_report(student, gpa_value, mode, extra_label):
    lines = []

    lines.append("=" * 50)
    lines.append("           SUPER GPA SYSTEM")
    lines.append("=" * 50)
    lines.append(f"Student: {student['name']}")
    lines.append(f"ID: {student['id']}")
    lines.append(f"Generated: {datetime.now()}")
    lines.append("")
    lines.append(f"MODE: {mode} ({extra_label})")
    lines.append("")
    lines.append("COURSES:")
    lines.append("-" * 50)

    # Filter terms based on mode
    filtered_terms = []
    if mode == "SEMESTER GPA":
        for term in student["terms"]:
            if term["semester"].lower() == extra_label.lower():
                filtered_terms.append(term)
    elif mode == "YEAR GPA":
        year = int(extra_label)
        for term in student["terms"]:
            if extract_year(term["semester"]) == year:
                filtered_terms.append(term)
    else:
        filtered_terms = student["terms"]

    for term in filtered_terms:
        lines.append(f"\n{term['semester']}:")
        for c in term["courses"]:
            lines.append(
                f"  {c['name']} | Grade: {c['grade']} | "
                f"Credits: {c['credits']} | Type: {c['type']}"
            )

    lines.append("-" * 50)
    lines.append(f"FINAL GPA: {gpa_value}")
    lines.append("=" * 50)

    return "\n".join(lines)


def export_to_csv(student, mode, extra_label, filename="report.csv"):
    # Filter terms as in build_report
    filtered_terms = []
    if mode == "SEMESTER GPA":
        for term in student["terms"]:
            if term["semester"].lower() == extra_label.lower():
                filtered_terms.append(term)
    elif mode == "YEAR GPA":
        year = int(extra_label)
        for term in student["terms"]:
            if extract_year(term["semester"]) == year:
                filtered_terms.append(term)
    else:
        filtered_terms = student["terms"]

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Semester", "Course Name", "Grade", "Credits", "Type", "Weight"])
        for term in filtered_terms:
            for c in term["courses"]:
                writer.writerow([term["semester"], c["name"], c["grade"], c["credits"], c["type"], c["weight"]])


def extract_year(semester):
    # "Fall 2026" -> 2026
    return int(semester.split()[-1])