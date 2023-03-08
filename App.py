# Laço de repetição normal

x = 10 

while x <= 50:
    print(x)
    x = x + 1 #Operador de incrementação em Python

# Laço de repetição inverso 
y = 20 

while y >=0:
    print(y)
    y = y - 1

#Determinando quando um loop vai terminar com uma entrada de dados.

fim = int(input("Quando o loop vai terminar ? "))

inicio = 0

while inicio < fim:
    print(inicio)
    inicio = inicio + 1 

#Estrutura de repetição com numeros pares 

numero = 1 

while numero <= 50:
    if numero % 2 == 0: #Se o resto da divisão for 0, é par. 
        print (numero)
        numero = numero + 1