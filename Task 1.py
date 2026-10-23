text = "apple banana apple orange apple banana apple banana banana"

def count_words(text):
    words = text.split()
    words_count = {}

    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    return words_count

result = count_words(text)

print("Кількість слів:", result)

more_3 = []

for word in result:
    if result[word] > 3:
        more_3.append(word)

print("Слова, які зустрічаються більше 3 разів:", more_3)
