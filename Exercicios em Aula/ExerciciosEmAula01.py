"""
Faça um programa em Python que solicite dois numeros 
e uma operação (Adição, subtração, multiplicação e divisão)
e apresente o resultado da operação solicitada
"""
#Laço principal que fara o questionário continuar até segunda ordem
while True:
    valor1 = float(input("Digite um valor: "))
    valor2 = float(input("Digite um segundo valor: "))
    operacao = input("Escolha uma operacao operacao(+, -, * ou /): ")

    #Estruturas condicionais que verificam o tipo de operacão digitada
    if operacao == '+' or operacao == 'Soma':
        print(f'{valor1} + {valor2} = {valor1 + valor2}')
    elif operacao == '-' or operacao == 'Subtracao':
        print(f'{valor1} - {valor2} = {valor1 - valor2}')
    elif operacao == '*' or operacao == 'Multiplicacao':
        print(f'{valor1} x {valor2} = {valor1 * valor2}')
    elif operacao == '/' or operacao == 'Divisao':
        print(f'{valor1} / {valor2} = {valor1 / valor2}')
    #Caso o usuario nao digite uma operacao valida
    else:
        print("Operação digitada inválida")

    #Pergunta ao usuario se ele deseja sair ou continuar 
    sair = int(input("Digite 0 para sair ou 1 para continuar: "))

    #Caso o usuario digite 0(Sair) o loop para e o programa encerra
    if sair == 0:
        break
    else:
        continue
#=================================================================================================

"""
Faça um algoritmo que solicite do usuário um número e imprima todos
os números naturais (a partir de 0) até o número informado pelo usuário
"""
# Pede um numero inteiro ao usuário
num = int(input("Informe um numero: "))

# Guarda o nome do arquivo
fileName = 'lacoFor.txt'

# Funcao que abre o arquivo no modo append
with open(fileName, 'a') as file_object:
    # Para cada numero entre 1 e o numro digitado
    for numero in range(num+1):
        print(numero)
        # Escreve cada numero em uma linha do arquivo
        file_object.write(str(numero)+'\n')
    # Adciona uma quebra de linha ao final
    file_object.write('\n')

#====================================================================================================

"""
Faça um algoritmo que solicite do usuário um número e imprima todos
os números naturais (a partir de 0) até o número informado pelo usuário
"""
# Pede um numero inteiro ao usuário
num = int(input("Informe um numero: "))

# Guarda o nome do arquivo
fileName = 'lacoFor.txt'

# Funcao que abre o arquivo no modo append
with open(fileName, 'a') as file_object:
    # Para cada numero entre 1 e o numro digitado
    for numero in range(num+1):
        print(numero)
        # Escreve cada numero em uma linha do arquivo
        file_object.write(str(numero)+'\n')
    # Adciona uma quebra de linha ao final
    file_object.write('\n')

#====================================================================================================

"""
Solicite o salário de um funcionário. Se o salário for maior que $2000, fornecer 
um aumento de 10%, senão, fornecer um aumento de 20%. Apresente como resultado o 
novo salário
"""

class Funcionario:
    # Contrutor da classe com o nome e o salario do funcionario
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    # Função que determina se o funcionario recebe um aumento de 20% ou de 10%
    def aumento(self):
        if self.salario > 2000:
            self.salario += self.salario*0.1
        else:
            self.salario += self.salario*0.2
    
    # Função que imprime o salário do funcionário no terminal
    def imprimirSalario(self):
        print(f'O salario do funcionario {self.nome} é de R$ {self.salario}')

# Criação do funcionário Kleber
funcionario_kleber = Funcionario("Kleber", 3000)
# Atribuição do aumento de Kleber
funcionario_kleber.aumento()
funcionario_kleber.imprimirSalario()

#=================================================================================================

"""
Faça um programa em Python que leia um número inteiro qualquer, e retorne se ele é par ou ímpar
"""
# Função que determina se o numero é par e imprime o resultado
def ehPar(num):
    if(num % 2 == 0):
        print("É par")
    else:
        print("É impar")


numero = int(input("Digite um numero: "))
ehPar(numero)

#===================================================================================================

"""
Elabore um algoritmo que receba como valor de entrada um ano, e informe se este ano é ou 
não é bissexto. Anos bissextos são múltiplos de 4 e não são múltiplos de 100, exceto os 
anos múltiplos de 400, que também são bissextos.
"""
# Função que verifiva se é um ano bissexto
def ehBissexto(year):
    if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        print(f'{year} é um ano bissexto')
    else:
        print(f'{year} não é um ano bissexto')

# Nome do arrquivo com os anos a serem analisados
arquivoAnos = 'anos.txt'

# Funcao que abre o arquivo no modo de leitura 'read'
with open(arquivoAnos, 'r') as file_object:
    linha = file_object.readline()
    # Divide a linha em uma lista contendo os anos 
    anos = linha.strip().split(" ")
    # Para cada ano na lista anos verifica se é um ano bissexto
    for ano in anos:
        ehBissexto(int(ano))

#==================================================================================================

"""
Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.
"""

# Objeto que contem a tabuada de um numero qualquer 
class tabuada:
    # Construtor que irá receber o valor que será a tabuada
    def __init__(self, num):
        self.num = num
    
    # Função que faz uma tabuada personalizada de um valor de inicio a um valor de termino
    def tabuadaInicioTermino(self, inicio, termino):
        for valor in range(inicio, termino+1, 1):
            print(f'{self.num} X {valor} = {self.num * valor}')
        print('\n')
    
    # Função que faz uma tabuada clássica ate de 0 ate 10 de um determinado valor
    def tabuadaComum(self):
        for valor in range(11):
            print(f'{self.num} X {valor} = {self.num * valor}')
        print('\n')

tabuada3 = tabuada(3)
tabuada3.tabuadaInicioTermino(567,584)
tabuada3.tabuadaComum()

#================================================================================================

"""
Crie um algoritmo que peça 10 números inteiros e positivos e apresente: a média, o maior 
e o menor. O algoritmo deve descartar valores negativos solicitando uma nova leitura.
"""

# Importa a biblioteca necessária para usar o maior valor suportado por Python
import sys

# Função que verifica a media, o maior e menor valor de uma lista de numeros 
def mediaMaiorMenor(listaDeNumeros):
    maior = -1
    menor = sys.maxsize
    media = 0
    soma = 0
    for numero in listaDeNumeros:
        if(numero > maior):
            maior = numero
        if(numero < menor):
            menor = numero
        
        soma += numero

    media = soma / len(listaDeNumeros)
    
    print(f'O maior numero digitado foi {maior}\nO menor numero digitado foi {menor}')
    print(f'A média desses numeros é igual a: {media}')

lista = []

# Laço que se repete 10 vezes adcionando numeros na lista
for i in range(10):
    num = int(input("Digite um numero: "))
    lista.append(num)

mediaMaiorMenor(lista)

#=================================================================================================

"""
Um determinado material radioativo perde metade de sua massa a cada 50 segundos. 
Dada a massa inicial, em gramas, faça um algoritmo que determine o tempo 
necessário para que essa massa se torne menor que 0,05 gramas.
"""

massa = int(input('Digite a massa do material em gramas: '))

# Contador do tempo necessário 
tempo = 0

# Massa que será descontada a cada laço do loop
massaAtual = massa

# Enquanto a massa atual for maior que 0.05 gramas
while (True):
    if (massaAtual >= 0.05):
        tempo += 1
        massaAtual /= 2
        continue
    else:
        break

print(f'Levou {tempo*50} segundos para o objeto fica com uma massa menor que 0,05 gramas')