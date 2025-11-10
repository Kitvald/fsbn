
def even_numbers(n):
    for i in range(2, n-1, 2):
        yield i
n = int("102 ")
nut = [num for num in even_numbers(n)]
print(sum(nut))

def odd_numbers(n):
    for i in range(1, n-1, 2):
        yield i
n = int("11")
nat = [(lambda nom: nom*nom)(nom) for nom in odd_numbers(n)]
print(nat)


