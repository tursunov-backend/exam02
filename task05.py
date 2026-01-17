def count_words(text: str) -> dict:
    words = text.split()  
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result

print(count_words("salom salom dunyo"))