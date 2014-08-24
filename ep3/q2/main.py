# coding=utf-8

# Faça um programa que receba do teclado um texto e grave-o em um arquivo.
text = raw_input("Digite um texto: ")

file = open("output.txt", "w")
file.write(text)
file.close()