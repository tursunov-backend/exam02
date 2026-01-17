def find_pattern(items: list, pattern: str, match_type: str) -> list:
    pattern = pattern.lower()
    result = []

    for item in items:
        item_lower = item.lower()
        if match_type == 'starts' and item_lower.startswith(pattern):
            result.append(item)
        elif match_type == 'ends' and item_lower.endswith(pattern):
            result.append(item)
        elif match_type == 'contains' and pattern in item_lower:
            result.append(item)

    return result


print(find_pattern(["Ali", "Alisher", "Vali", "Aziz"], "A", "starts"))