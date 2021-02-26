def contra(contraseña=(input("Ingrese su nueva contraseña: "))):
    contras=contraseña.lower()

    ver_constraseña=(input("Ingrese su contraseña: "))
    contrass=ver_constraseña.lower()
    if contras==contrass:
        return "La contraseña es correcta"
    else:
        return "La contraseña es incorrecta"

print(contra())
