def find_top_students(grades: dict) -> dict:
    max_grade = max(grades.values())
    students = []

    for name, grade in grades.items():
        if grade == max_grade:
            students.append(name)

    return {
        "max_grade": max_grade,
        "students": students
    }

print(find_top_students({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}))