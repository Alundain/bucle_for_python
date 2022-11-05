
# 1. Imprime todos los numeros enteros desde el 0 al 150
for x in range(0, 151):
    print(x)

# 2.Multiplos de 5. Imprime todos los números multiplos de 5 entre 5 y 1000
for y in range(5, 1001):
    if y % 5 == 0 :
        print(y)

# 3.Contar a la manera dojo: imprime número enteros de 1 al 100. Si es divisible por 5 imprime "Coding" 
# en su lugar. Si es divisible por 10 imprime "Coding Dojo"
for g in range (1, 101):
    print(g)
    if g % 5 == 0:
        print("Coding")

    elif g % 10 == 0:
        print("Coding Dojo")

# 4. Agrega los entero impares del 0 al 500,000 e imprime la suma final

for a in range (0, 500002 ):
    if a % 2 == 1 :
        print(a)
    a += 1

#5. Cuenta regresiva de a 4, imprime números positivos comenzando desde 
#el 2018, en cuenta regresiva de 4 en 4
num = 2018
for i in range(1,num+1):
    print(num-i)



#6. Contador flexible, establece 3 variables : lowNum, highNum, mult. 
#comenzar con lowMun y pasando por los hughNum, imprime solo los enteros 
#que sean multiplos de mult. Por ejemplo si lowNum=2, highNum=9 y mult=3. 
#El bucle debe imprimir 3,6,9(en lineas sucesivas)
