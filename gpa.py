# gpa.py

from utils import extract_year

GRADE_POINTS = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}


def calculate_gpa(courses):
    total_points = 0.0
    total_credits = 0.0

    for c in courses:
        base = GRADE_POINTS.get(c["grade"].upper(), 0.0)
        weighted = min(base * c.get("weight", 1.0), 4.0)

        total_points += weighted * c["credits"]
        total_credits += c["credits"]

    return round(total_points / total_credits, 3) if total_credits else 0.0


def get_semester_gpa(student, semester_name):
    for term in student["terms"]:
        if term["semester"].lower() == semester_name.lower():
            return calculate_gpa(term["courses"])
    return None


def get_year_gpa(student, year):
    all_courses = []

    for term in student["terms"]:
        if extract_year(term["semester"]) == year:
            all_courses.extend(term["courses"])

    return calculate_gpa(all_courses) if all_courses else None


def get_cumulative_gpa(student):
    all_courses = []

    for term in student["terms"]:
        all_courses.extend(term["courses"])

    return calculate_gpa(all_courses) if all_courses else None