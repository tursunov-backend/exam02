def calculate_stats(numbers: list) -> dict:
    total = sum(numbers)
    average = total / len(numbers)
    average = round(average, 2)
    
    return {"sum": total, "average": average}

print(calculate_stats([3, 7, 10, -5, -8, 15, 22]))