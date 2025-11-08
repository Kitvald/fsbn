def counts_word(text):
    dict_word = {}
    for word in text:
        dict_word[word] = dict_word.get(word, 0) + 1
    return dict_word


def process_text_for_analysis(raw_text):
    punctuation = """!@#$"%^&*()_+=-?:%;№,<>,./?"""
    clean_translator = str.maketrans('', '', punctuation)
    cleaned_text = raw_text.translate(clean_translator).lower()
    words = cleaned_text.split()
    word_dict = counts_word(words)
    return word_dict, cleaned_text, words


def vowels_count(text):
    vowels = "уёеыаоэяию"
    counts = 0
    for char in text:
        if char in vowels:
            counts += 1
    return counts


def word_count(text):
    for word, count in sorted(word_dict.items()):
        print(word, count)


my_string = str(input("Введите текст: "))
word_dict, my_string_clean, words = process_text_for_analysis(my_string)
word_count(words)

print("Количество гласных:",vowels_count(my_string_clean))
print("Количество слов:",len(words))
print("Самое длинное слово:",max(words, key=len))

