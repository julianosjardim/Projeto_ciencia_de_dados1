# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

# variáveis

#Tela
print("Selecione o número da operação desejada\n")
print("1 - Soma\n")
print("2 - Subtração\n")
print("3 - Multiplicação\n")
print("4 - Divisão\n")

#Inserindo dados

a = int(input("Digite sua opção (1/2/3/4): "))
b = int(input("Digite o primeiro número: "))
c = int(input("Digite o segundo número: "))

#Processando
if(a == 1):
	conta = b+c
	print("{0} + {1} = {2}".format(b,c,conta))
elif(a == 2):
	conta = b-c
	print("{0} - {1} = {2}".format(b,c,conta))
elif(a == 3):
	conta = b*c
	print("{0} * {1} = {2}".format(b,c,conta))
elif(a == 4):
	conta = b/c
	print("{0} / {1} = {2}".format(b,c,conta))
else:	
	print("Favor digitar opção (1/2/3/4) válida!")



