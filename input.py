""""Entrada de Dados"""

nome = input("Qual seu nome? ")

print("O usuário digitou", nome, "e o tipo de variável é ", type(nome))

idade = input("Qual sua idade? ")

print("O usuário digitou", idade, "e o tipo de variável é ", type(idade))

# Mesmo digitando um número, o tipo da variável da função input sempre será no formato string
# É preciso converter o tipo de variável. Ex:

nascimento = input("Em que ano você nasceu? ")
nascimento = int(nascimento)

print("Você nasceu no ano de ", nascimento, "e o tipo de variável é ", type(nascimento))


#Já uma variável é do tipo int. Ex:

#numero = 10

#print(type(numero))





