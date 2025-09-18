my_string = "Делать делать чёрным, Ппридавать чёрный  цвет, цвет цвет оттенок." # для теста функции for
my_string_clean = my_string.replace(',', '').replace('.', '').lower()
words = my_string_clean.split()
dict_word = {}
glasnue = ("уёеыаоэяию")
counts = 0


for word in words:
    dict_word[word] = dict_word.get(word, 0) + 1
for word, count in sorted(dict_word.items()):
        print(word, count)


for word in my_string_clean:
    if word in glasnue:
        counts += 1


print("Количество гласных:",counts)
print("Количество слов:",len(words))
print("Самое длинное слово:",max(words, key=len))
