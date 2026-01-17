def find_longest_name(names: list) -> str:
    longest = names[0]

    for name in names:
        if len(name) > len(longest):
            longest = name

    return longest

print(find_longest_name(['Ali', 'Diyor', 'Jasurbek', 'Muhammad']))
