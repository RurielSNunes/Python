"""Aula 004 - Primeiros comandos em Python"""

"As aspas simples ou dupla são delimitadores para mensagens"
"Toda função tem que ter parenteses"
"Números são usados primordialmente para fazer cálculos e não precisam ficar entre aspas"
'Diferença entre uma mensagem e uma soma'

print('Olá, Mundo!')

print(7+5)
"Mostra o resultado"
print('7+5')
"Mostra o que está entre as aspas"
print('7'+'5')
print('7','5')
"Mostra a junção dos dois números como mensagem, e pode ser usado o sinal de mais (+) ou a vírgula (,)"

"""Prática"""
"As variáveis devem sempre ser escritas com letras minúsculas"
"Objeto e mais que uma variável"
"O sinal de igual depois da variável significa (recebe)"

nome = 'Ruriel'
idade = '20'
peso = '85.5'
print(nome, idade, peso)
"As variáveis sõe espaços na memória guardados no computador"

nome = input('Qual é o seu nome?')
idade = input('Qual é a sua idade?')
peso = input('Qual é o seu peso?')
print(nome, idade, peso)

"""Desafio"""
'01 - Crie um script Python que leia o nome de uma pessoa e mostre uma mensagemde boas-vindas de acordo com o valor digitado.'
'Minha resposta'
nome = input('Qual é o seu nome?')
print('Seja bem vindo(a),{} !'.format(nome))

'02 - Crie um scrippt Python que leia o dia, o m~es e o ano de uma pessoa e mostre uma mensagem com a data formatada.'
'Minha resposta'
dia = input('Qual o dia que você nasceu?')
mes = input('Qual o mês você nasceu?')
ano = input('Qual e o ano que você nasceu?')
print('Você nasceu no dia , {} de {} de {} . Correto?'.format(dia, mes, ano))

'03 - Crie um script Python que leia dois números e tente mostrar a soma entre eles.'
'Minha respota'
n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número:'))
soma = (n1 + n2)
print('A soma entre {}+{}={}.'.format(n1, n2, soma))
