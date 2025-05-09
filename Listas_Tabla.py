Cantones = [1,2,3]
 = ['Matematicas','Geometria','Algoritmia']
doc = ['Santiago Olovacha','Susana Pallasco','Segundo Corrales']
hor = [9,4,8]
thor = []
estudiante=[]
promedio=[]
resulAsig=[]
resulDoc=[]

for z in hor:
    hca = z*16
    thor.append(hca)
    

print("Distributivo Nivelación Software".center(101,"="))
print("{:<5}""{:<15}""{:<25}""{:<15}".format("N°","Asignatura","Docente","Horas"))
print("="*101)

for a,b,c,d in zip (num,asig,doc,hor):
    print("{:<5}""{:<15}""{:<28}""{:<15}".format(a,b,c,d))

print("="*101)

x = 1
while (x==1):
    s=0
    el = int(input("Ingrese el numero de asignatura:  "))
    while(el<1)or(el>3):
        el = int(input("Número correcto 1-3:  "))

    indice = num.index(el)

    print("\n",asig[indice])

    nom = input("Ingrese el nombre del estudiante:  ")
    while nom.isalpha()==False:
        nom =input("Ingrese un nombre sin numeros:  ")
    estudiante.append(nom)

    for i in range(3):
        nota = int(input(f"Nota {i+1}:  "))
        while(nota<0)or(nota>10):
            nota = int(input(f"Nota {i+1} correcta:  "))    
        s=s+nota
    prom = s/3
    promedio.append(prom)
    print("="*101)

    resulAsig.append(asig[indice])
    resulDoc.append(doc[indice])
    x = int(input("Desea realizar otra ingreso 1 = SI // 2 = NO:  "))
    
print("{:<25}""{:<25}""{:<25}""{:<25}".format("Asignatura","Docente","Estudiante","Promedio"))
print("="*101)

for f,g,h,i in zip(resulAsig,resulDoc,estudiante,promedio):
    print("{:<25}""{:<25}""{:<25}""{:<25}".format(f,g,h,i))
    







