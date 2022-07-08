#libs: inputCuatroNumeros,inputSino, inputCadena, nroAleatorio, escribirRanking, leerRanking
from random import randint

def inputCuatroNumeros(cartel):
    validado = False
    while not validado:
        n = input(cartel)
        cRepetido=False
        try:
            if len(n)==4:
                for x in range(4):
                    if n[x] in n[x+1:]:
                        cRepetido=True
            
                if cRepetido==True:
                    print("Parece que has repetido uno o más dígitos. Recuerda que deben ser todos distintos!")
                else:
                    if n[0]!= "0":
                        n = int(n)
                        validado=True
                    else:
                        print("Tu número no puede comenzar con 0!")
            else:
                print("Recuerda, deben haber sólo 4 dígitos!")
        except:
            print("Por favor, ingrese sólo números!")
    return n

def inputSino(cartel):
    validado=False
    while not validado:
        entrada=input(cartel)
        siono=entrada.lower()
        if siono=="si":
            validado=True
            return True
        if siono=="no":
            validado=True
            return False
        else:
            print("Por favor, ingrese si / no.")
            validado=False

def inputCadena(cartel,caracteresMax=999):
    parar=False
    while not parar:
        cadena=input(cartel)
        if len(cadena) > caracteresMax:
            print(f"Por favor, no ingrese más de {caracteresMax} caracteres")
        else:
            parar=True
            return cadena

def nroAleatorio():
    nro=randint(1000, 9999)
    frenar=False
    while not frenar:
        repetido=False
        nroCadena=str(nro)
        for x in range(4):
            if nroCadena[x] in nroCadena[x+1:]:
                repetido=True          
        if not repetido:
            frenar=True
        elif repetido:
            #print("Buscamos otro. el numero era", nro)
            nro=randint(1000, 9999)
    return nro

def escribirRanking(nombre,score):
    a=open("ranking.txt","r+",encoding="utf-8")
    a.read()
    a.write(f"{score}-{nombre}\n")
    a.close
    print("Tu puntuación se ha subido correctamente!")

def leerRanking():
    scores=[]
    nombres=[]
    o=open("ranking.txt","r",encoding="utf-8")
    for linea in o:
        score,nombre=linea.split("-")
        nombres.append(nombre[:-1])
        scores.append(int(score))
    highscores=sorted(scores)
    
    print("------HIGH SCORES------")
    posicion=0
    for x in range(10):
        if highscores[x] == highscores[x-1]:
            posicion=scores.index(highscores[x],posicion+1)
        else:
            posicion=scores.index(highscores[x])
        print(f"TOP {x+1}.\t{nombres[posicion].upper()}\tcon {scores[posicion]} intentos")
    o.close
    return


if __name__=="__main__":
    print(nroAleatorio())
    inputCuatroNumeros("ingrese nro:")


"""
El jugador va proponiendo números y el programa le contesta los aciertos:

Si un dígito del usuario está en el número de la computadora la respuesta será:
BIEN, si está en la misma posición
REGULAR si está presente pero en otra posición

Se termina al adivinar el número exacto y se debe almacenar en un archivo de texto el nombre del jugador y la cantidad de intentos que le llevó ganar.

El programa también debe permitir mostrar el top ten del ranking de jugadores, ordenados por las sesiones con menor cantidad de intentos para el acierto.
"""