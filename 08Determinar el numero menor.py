
N1 = int(input("Ingrese N1 entero: "))
N2 = int(input("Ingrese N2 entero: "))
if N1 == N2:
     print("Los numeros ingresados deber ser diferentes. ")
else:
    if N1 < N2:
        menor = N1
    else:
        menor = N2
    print(f"El menor es: {menor}")