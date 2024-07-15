letra = input("Ingrese una letras: ")
if len(letra) > 1:
    print("Solo debe ingresar una letra")
else:
    if letra.lower() in ("a", "e", "i", "o", "u"):
        print("Es vocal")
    else:
        print("No es vocal")
        