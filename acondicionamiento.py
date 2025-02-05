#Ejercicio 1

def SumaDeDigitos (x):
    sum = 0
    while x > 0:
        dig = x % 10
        sum += dig 
        x = x // 10
    return sum

#x = int(input("Ingresar Numero Para contar: "))
#print("El Total de la suma del digito es: ", SumaDeDigitos(x))  


#Ejercicio 2

def ContarVocales (x):
    sum = 0
    num = len(x)

    for i in range (num):
        if x[i] == 'a' or x[i] == 'e' or x[i] == "i" or x[i] == "o" or x[i] == "u":
            sum += 1
        elif x[i] == 'A' or x[i] == 'E' or x[i] == "I" or x[i] == "O" or x[i] == "U":
            sum += 1
    return sum

#x = input("Ingresar Palabra Para contar: ")
#print("El Total de la suma del digito es: ", ContarVocales(x))


#Ejercicio 3
def palindromo(x):
    
    texto = x.replace(" ", "").lower()
    if texto == texto[::-1]:
        print("Sí")
    else:
        print("No")

# Entrada del usuario
#cadena = input()
#palindromo(cadena)


#ejercicio 4
def InvertirNumeros(x):
    num = len(x)
    lis = []
    for i in range (num):
        if x[i] != ' ':
            lis.append(x[i])
    lis.reverse()

    j= 0
    while j < len(lis):
        print(lis[j], end = " ")
        j += 1


#x = "1 2 3 4 5"
#InvertirNumeros(x)


#Ejercicio 5
def ContarCadena(x):
    tex = x.split(" ")
    tol = len(tex)
    return tol

#x = "Hola Mundo Desde python gonzo"
#print(ContarCadena(x))


#Ejercicio 6
def EncontrarMaxyMin(x):
    numeros = []
    for num in x.split():
        num_entero = int(num)
        numeros.append(num_entero)

    maximo = numeros[0]
    minimo = numeros[0]

    for num in numeros:
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num

    print(maximo, " ", minimo)

x = "3 1 4 1 5 9"
EncontrarMaxyMin(x)
