
limite = int(input("¿Ingrese el numero a multiplicar?: "))

for numero in range(1, limite + 1):
    print("Tabla del", numero)
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)
    print()  
