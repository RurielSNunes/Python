# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

'Minha resposta'
#a = input('Digite algo: ')
#print('O tipo primitivo desse valor é ', type(a))
#print('Só tem espaços? ', a.isspace())
#print('É um número? ', a.isnumeric())
#print('É alfabetico? ', a.isalpha())
#print('É alfanúmerico? ', a.isalnum())
#print('Está em maiúculas? ', a.isupper())
#print('Está em minúsculas? ', a.islower())
#print('Está capitalizada? ', a.istitle())

a = input('Digite algo: ')
print('O tipo primitivo de {} é '.format(a), type(a))
print('{} só tem espaços? '.format(a), a.isspace())
print('{} é um número? '.format(a), a.isnumeric())
print('{} é alfabetico? '.format(a), a.isalpha())
print('{} é alfanúmerico? '.format(a), a.isalnum())
print('{} está em maiúculas? '.format(a), a.isupper())
print('{} está em minúsculas? '.format(a), a.islower())
print('{} está capitalizada? '.format(a), a.istitle())
