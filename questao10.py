'''
10)	Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso.
Utilize a fórmula prestação	=	valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias).
'''

prest = float(input("Qual o valor noemal da prestação? R$"))
temp = int(input("Há quantos dias a prestação está atrasada? "))
tax = float(input("Qual é a taxa de júros?"))

print("O valor da prestação com os júros é: R$",prest + (prest * (tax / 100) * temp))