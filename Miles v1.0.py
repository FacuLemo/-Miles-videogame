#menu del juego Miles, por Facundo E. Lemo

import os
from libs import (escribirRanking, inputCuatroNumeros, inputSino,inputCadena, leerRanking,
                  nroAleatorio)


def menu():
    orden = ""
    while orden != "3":
        os.system("cls")
        print("  JUEGO MILES\nMenú de opciones\n")
        print("1) ¡Jugar!")
        print("2) Ver top 10")
        print("3) Salir")
        orden = input("Ingrese una opción: ")
        if orden == "1": #JUEGO:MILES
            os.system("cls")
            puntuacion=0
            numero=nroAleatorio()
            print("Se ha creado un número aleatorio de 4 dígitos. Tu misión es encontrarlo.\nPara eso deberás ingresar un número, y se te dirá si acertaste o fallaste con los dígitos.\nRecuerda, no puedes poner el mismo dígito 2 o más veces! Ahora bien,")
            #print(numero) #con motivos de testeo
            victoria=False
            while not victoria:
                puntuacion+=1
                intento=inputCuatroNumeros("Ingresa un número de 4 dígitos: ")
                numero=str(numero)
                intento=str(intento)
                bien=0
                regular=0
                for x in range(4):
                    if intento[x]==numero[x]:
                        bien+=1
                    elif intento[x] in numero:
                        regular+=1
                if bien==4: #condicion de victoria
                    print(f"FELICIDADES! Adivinaste el número!\n El número era {numero}! Te tomó {puntuacion} intentos!")
                    cargarDatos=inputSino("Quieres guardar tu puntuación?(si/no): ")
                    if cargarDatos==True:
                        nombre=inputCadena("ingresa tus iniciales o nombre corto!: ",5)
                        escribirRanking(nombre,puntuacion)
                        input("Presiona enter para volver al menú.")
                        victoria=True
                    else:
                        input("Presiona enter para volver al menú.")
                        victoria=True
                else:
                    if bien==0 and regular!=0:
                        print(f"No hay ninguno bien, pero hay {regular} regular")
                    elif bien !=0 and  regular==0:
                        print(f"Hay {bien} bien, y ninguno regular")
                    elif bien==0 and regular==0:
                        print(f"No hay ningún bien y ningún regular! jajaja!")
                    elif bien!=0 and regular !=0:
                        print(f"Hay {bien} bien y {regular} regular")
                
        elif orden == "2":
            os.system("cls")
            leerRanking()
            input("Presione enter para volver al menú")
                
        elif orden == "3":
            input("Gracias por jugar. Presione enter para salir.")
        else:
            input("Esa orden no es válida. Presione enter para continuar.")

if __name__=="__main__":
    menu()
