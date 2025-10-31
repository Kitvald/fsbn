def create_word_dict(words):
    dict_word = {}
    for word in words:
        dict_word[word] = dict_word.get(word, 0) + 1
    return dict_word


my_string = str(input("Введите текст: "))
my_string_clean = my_string.replace(',', '').replace('.', '').lower()
words = my_string_clean.split()
word_dict = create_word_dict(words)

def vowels_count(text):
    vowels = "уёеыаоэяию"
    counts = 0
    for char in text:
        if char in vowels:
            counts += 1
    return counts

for word, count in sorted(word_dict.items()):
    print(word, count)

print("Количество гласных:",vowels_count(my_string_clean))
print("Количество слов:",len(words))
print("Самое длинное слово:",max(words, key=len))
