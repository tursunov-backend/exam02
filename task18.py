def square_values(numbers: list) -> list:
    result = []

    for item in numbers:
        result.append({'value': item['value'] ** 2})

    return result

print(square_values([{'value': 2}, {'value': 3}, {'value': 4}]))