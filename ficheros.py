from VALID import ns

def ver_text():
    while True:
        nombre_fichero=((input("Escriba el nombre del fichero que quiere leer: ")+".txt"))
        try:
            fichero=open(nombre_fichero,"r")
            break
        except:
            pass
    return fichero

while True:
    print("TRABAJANDO CON TEXTOS")
    print("¿Que desea hacer?: ")
    print("A)LEER UN TEXTO")
    print("B)CONTAR EL NUMERO DE LINEAS DE TEXTO")
    print("C)CONTAR EL NUMERO DE PALABRAS DEL TEXTO")
    print("D)CONTAR EL NUMER DE CARACTERES DEL TEXTO")
    op=input("Introduzca aquí su opción: ")

    fichero=ver_text()
    contador=0
    print("")
    for linea in fichero:
        if op==("A"):
            if linea[-1]==('\n'):
                linea=linea[:-1]
            print(linea)
        elif op==("B"):
            contador+=1
        elif op==("C"):
            contador+=len(linea.split(" "))
        elif op==("D"):
            for i in linea:
                if i==(" ") or i==('\n'):
                    contador-=1
                contador+=1
    fichero.close()
    if op==("B"):
        print("El texto consta de",contador,"líneas")
    elif op==("C"):
        print("El texto consta de",contador,"palabras")
    elif op==("D"):
        print("El texto consta de",contador,"caracteres")
    print("") 
        


