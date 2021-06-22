#Diseñar juego del ahorcado con el siguiente patrón:
#¡Adivina la palabra!
#_ _ _ _ _ _ _  (dependiendo el número de letras se coloca el número de underscores)
#Un input esperando que se ingrese un caracter con el mensaje: "Ingresa una letra:"
#Cuando se descubren todas las letras lanza mensaje:
# ¡Ganaste! La palabra era XXXXX y se cierra el juego.


#Primero necesito acceder al listado de palabras en el words.txt y guardarlo en una lista
import os
import random

def read():
    palabras=[]
    with open("./HangMan Game/words.txt","r", encoding="utf-8") as f:
        for line in f:
            l=line[:-1]
            palabras.append(l)
    return palabras

def start_game(palabra):
    os.system('cls')
    print("¡Adivina la palabra!")
    for i in range(len(palabra)):
       print("_",end=" ")

def imprimir_avance_descubierto(palabra_oculta):
    os.system('cls')
    print("¡Adivina la palabra!")
    #finalmente imprimo en pantalla lo que hay en palabra oculta
    for valor in palabra_oculta:
        if valor=="_":
            print("_",  end=" ")
        else:
            print(valor, end=" ")

def run():
   lista_palabras=read()
   #La palabra la tomamos al azar del listado leído
   palabra=random.choice(lista_palabras)
   palabra_oculta=["_" for i in range(len(palabra))]  
   relacion_indice_letra={i:palabra[i] for i in range(len(palabra))}
   #print(relacion_indice_letra)
   start_game(palabra)
   
   indices_descubiertos=[]
   
   
   while True:       
        print("")
        print("")
        letra_escrita=input("Ingresa una letra: ").lower()
        
        try:
            assert len(letra_escrita)>0,"** No se permiten vacíos"
            assert len(letra_escrita)==1 ,"** Debe escribirse sólo una letra"           
            assert letra_escrita.isalpha(),"** Sólo se permiten letras"
               
            #busco la letra en el diccionario, por su valor. Si está, guardo su llave
            for key,value in relacion_indice_letra.items():
                if value==letra_escrita:
                    indices_descubiertos.append(key)  
        
            #luego con estas llaves reemplazaré en el indice de la palabra_oculta con su valor correspondiente
            for indice in indices_descubiertos:
                valor_indice=relacion_indice_letra.get(indice)
                palabra_oculta[indice]=valor_indice
        
            imprimir_avance_descubierto(palabra_oculta)
            
            #si ya no hay más underscores entonces se ha descubierto la palabra, por tanto nos salimos del while e imprimimos que ha ganado
            if "_" not in palabra_oculta:
                break
        except AssertionError as e:
            imprimir_avance_descubierto(palabra_oculta)
            print("")
            print("")
            print(e)
        
        
   #si llega aquí es que ya se salió del while, por lo tanto descubrió la palabra
   os.system('cls')
   print("")
   print(f"¡Ganaste! La palabra era {palabra}")


if __name__=="__main__":
    run()
