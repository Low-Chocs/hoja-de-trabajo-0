n=int(input("Ingrese el número de niveles de su tríangulo: "))
for i in range (n):
    for j in range (i+1):
        print("*", end="")
    print("")


n1= int(input("Ingrese el número que deseas comprobar: "))
def primo(n1):
    cont=0
    
    for i in range (1,n1+1):
        if n1%i==0:
            cont +=1
    
    if cont==2:
        return "Es primo"

    else:
        return "No es primo"

print(primo(n1))
        
