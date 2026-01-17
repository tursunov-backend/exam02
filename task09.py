def find_min_max(numbers: list) -> dict:
    
    min_num = min(numbers)
    max_num = max(numbers)
    
    return {'max': max_num, 'min': min_num}

print(find_min_max([3, 7, 10, -5, -8, 15, 22]))