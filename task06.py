def analyze_grades(students: dict) -> dict:
    total = sum(students.values())
    average = total / len(students)

    above_average = []

    for name, grade in students.items():
        if grade > average:
            above_average.append(name)

    return {
        'average': average,
        'above_average': above_average
    }


print(analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3}))
