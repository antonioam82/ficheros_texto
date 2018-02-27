from VALID import ns
import subprocess
def ver_text():
    while True:
        nombre_fichero=((input("Escriba el nombre de un fichero de texto existente: ")+".txt"))
        try:
            fichero=open(nombre_fichero,"r")
            break
        except:
            print("El fichero introducudo no existe",chr(7))
    return fichero

while True:
    print("TRABAJANDO CON TEXTOS")
    print("¿Que desea hacer?: ")
    print("A)REPRODUCIR UN TEXTO")
    print("B)CONTAR EL NUMERO DE LINEAS DE TEXTO")
    print("C)CONTAR EL NUMERO DE PALABRAS DEL TEXTO")
    print("D)CONTAR EL NUMER0 DE CARACTERES DEL TEXTO")
    print("E)BUSCAR UNA PALABRA")
    op=input("Introduzca aquí su opción: ")
    fichero=ver_text()
    if op==("E"):
        palabra=input("Introduzca palabra a buscar: ")
    contador=0
    nconta=0
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
        elif op==("E"):
            linea.split(" ")
            if palabra in linea:
                contador+=1
   
    fichero.close()
    if op==("B"):
        print("El texto consta de",contador,"líneas")
    elif op==("C"):
        print("El texto consta de",contador,"palabras")
    elif op==("D"):
        print("El texto consta de",contador,"caracteres")
    elif op==("E"):
        print("La palabrase se encontró",contador,"veces")
    print("") 
    conti=ns(input("¿Desea continuar?: "))
    if conti==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])




