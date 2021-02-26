def contra(name=(input("Ingrese su nombre: "))):
    nombre=name.lower()
    nombre1=name.capitalize()

    print("")
    print("Masculino/femenino (El texto no es sensible)")
    ver_gen=(input("¿Cuál es su género? "))

    genero=ver_gen.lower()
    if nombre[0]<='m'and genero=="femenino":
        return nombre1+" perteneces a la sección A"
    elif nombre[0]>='n'and genero=="masculino":    
       return nombre1+" perteneces a la sección A"
    else:
        return nombre1+" perteneces a la sección B"

print(contra())
