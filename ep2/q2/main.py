# coding=utf-8

# Faça uma função que receba como entrada uma palavra e diga se ela é palíndroma.
def palindroma(palavra):
    return palavra.lower() == palavra[::-1].lower()

print palindroma("Osso")    # True
print palindroma("Ana")     # True
print palindroma("Jedi")    # False