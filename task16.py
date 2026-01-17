def count_by_grade(grades: dict, target_grade: int) -> dict:
    students = []

    for name, grade in grades.items():
        if grade == target_grade:
            students.append(name)

    return {
        'count': len(students),
        'students': students
    }

print(count_by_grade({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}, 5))