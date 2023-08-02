'''
9)	Fazer um algoritmo que pergunte 1 número e apresente:
a)	O próprio número
b)	O quadrado deste número
c)	A raiz quadrada deste número

'''
import math

num = float(input("informe um número: "))

print("O número escolhido foi: ",num)
print("O quadrado do número escolhido é:", num*num)
print("A raiz quadrada do número escolhido é: ",math.sqrt(num))