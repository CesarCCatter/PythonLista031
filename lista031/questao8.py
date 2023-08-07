'''
8)	Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem.
O programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros;
qual é o valor do consumo médio do automóvel, em quilômetros por litro.
'''

dist = float(input("Qual será a distância da sua viagem em km? "))

lit = float(input("Quantos quilômetros o carro que você usará faz gastando um litro de comustível? "))

print("Você gastará em sua viagem: ",dist / lit,"Litros")