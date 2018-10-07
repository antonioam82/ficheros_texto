from VALID import ns,opt,OKI
import subprocess
def ver_text():
    while True:
        nombre_fichero=((input("Escriba el nombre de un fichero de texto existente: ")+".txt"))
        try:
            fichero=open(nombre_fichero,"r")
            break
        except:
            print(("El fichero introducido no existe"),chr(7))
    return fichero

def plu(n):
    if n==1:
        return"vez"
    else:
        return "veces"
        

while True:
    print("TRABAJANDO CON TEXTOS")
    print("¿Que desea hacer?: ")
    print("A)CREAR UN ARCHIVO DE TEXTO")
    print("B)REPRODUCIR UN TEXTO")
    print("C)CONTAR EL NUMERO DE LINEAS DE TEXTO")
    print("D)CONTAR EL NUMERO DE PALABRAS DEL TEXTO")
    print("E)CONTAR EL NUMER0 DE CARACTERES DEL TEXTO")
    print("F)BUSCAR UNA PALABRA")
    print("G)ANALIZADOR DE TEXTO")
    op=opt(input("Introduzca aquí su opción: "),["A","B","C","D","E","F","G"])
    #while op!=("A") and op!=("B") and op!=("C") and op!=("D") and op!=("E"):
        #op=input("Introduzca una opción válida: ")
    if op==("A"):
        nuevo_fichero=((input("Fichero: ")+".txt"))
        fichero=open(nuevo_fichero,"w")
        nl=OKI(input("Número de líneas: "))
        for i in range(0,nl):
            linea=input("Texto: ")
            fichero.write(linea+"\n")
        fichero.close()

    elif op==("G"):
        fichero=ver_text()
        contador=0
        car=[]
        elem=[]
        conta=0
        for linea in fichero:
            for i in linea:
                if i==(" ") or i==('\n'):
                    contador-=1
                contador+=1
                elem.append(i)
                if not i in car and (i!=(" ") and i!=('\n')):
                    car.append(i)
        for c in car:
            conta=0
            for e in elem:
                if e==c:
                    conta+=1
                    por=(conta*100)/contador
            print(c,("{:.2f}".format(por))+"%")
            

  
    else:
        fichero=ver_text()
        if op==("F"):
            palabra=input("Introduzca palabra a buscar: ")
        contador=0
        print("")
        for linea in fichero:
            if op==("B"):
                if linea[-1]==('\n'):
                    linea=linea[:-1]
                print(linea)
            elif op==("C"):
                contador+=1
            elif op==("D"):
                contador+=len(linea.split(" "))
            elif op==("E"):
                for i in linea:
                    if i==(" ") or i==('\n'):
                        contador-=1
                    contador+=1
            elif op==("F"):
                linea.split(" ")
                if palabra in linea:
                    contador+=1
        fichero.close()
        if op==("C"):
            print("El texto consta de",contador,"líneas")
        elif op==("D"):
            print("El texto consta de",contador,"palabras")
        elif op==("E"):
            print("El texto consta de",contador,"caracteres")
        elif op==("F"):
            print("La palabra se se encontró",contador,plu(contador))
        print("")
    conti=ns(input("¿Desea continuar?: "))
    if conti==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])
        
 




