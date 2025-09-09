from dataclasses import replace

my_string = "Делать чёрным, придавать чёрный  цвет, цвет цвет оттенок." # для теста функции for
my_string_clean = my_string.replace(',', '').replace('.', '')
words = my_string_clean.split()

for s in my_string:
    print(max(words, key=len))
    print(len(words))
    #print(list(enumerate(words)))
    break
