import random
import string
from Palabras import palabras
from Vidas import vidas


def Inicio():
  print(vidas[11])
  cantJugadores=input("Seleccione 1 para jugar en solitario y 2 para dos jugadores.")

  while(cantJugadores != "1" and cantJugadores!= "2"):
    cantJugadores=input("Caracter no válido, vuelva a ingresar.")
  
  if cantJugadores=="1":
    Juego()
  else:
    JuegoVS()

def traerPalabra(lista):
    palabra=random.choice(lista)
    return palabra.upper()

def Juego():

  while (True):
    
    nombreJugador=input("Ingrese su nombre para continuar.")
    palabra=traerPalabra(palabras)
    
    letrasPorAdivinar= set(palabra)
    utilizadas=set()

    abcd=set(string.ascii_uppercase)
    bandera= False

    Vida=8

    while len(letrasPorAdivinar) > 0 and Vida > 0:
      if bandera:
        print(f"Vidas disponibles: {Vida} \nLetras utilizadas: {' '.join(utilizadas)}")

      listaPalabras=[letra if letra in utilizadas
      else '-' for letra in palabra] 
      print(vidas[Vida])
      print(f"Palabra: {' '.join(listaPalabras)}")

      letraSeleccionada = input("Selecciona una letra: ").upper()
      bandera=True

      if letraSeleccionada in abcd and not letraSeleccionada in utilizadas:
        utilizadas.add(letraSeleccionada)
      
        if letraSeleccionada in letrasPorAdivinar:
          letrasPorAdivinar.remove(letraSeleccionada)
          print(' ')
          if len(letrasPorAdivinar)>0:
            print("¡Letra ADIVINADA!")
          else:
            print(f"¡¡¡{nombreJugador} adivinó la palabra!!!")
        else:
          Vida-=1
          print(f"\nLa letra '{letraSeleccionada}' no está en la palabra.")

      elif letraSeleccionada in utilizadas:
        print(f"\nLa letra '{letraSeleccionada}' ya fue utilizada, por favor ingresá una letra nueva.")
      else:
        print(f"\nEl caracter '{letraSeleccionada}' no es válido, ingrese otro.")

    if Vida==0:
      print(vidas[Vida])
      print("La palabra a adivinar era: "+palabra)
      print(vidas[10])
      resetearVidas=input("Si desea volver a jugar escriba 'SI'.").upper()
    else:
      print("La palabra era: "+palabra)
      print(vidas[12])
      resetearVidas=input("Si desea volver a jugar escriba 'SI'.").upper()

    if resetearVidas=="SI":
      Vidas=8
      palabra=traerPalabra(palabras)
    else:
      break

def JuegoVS():

  Jugador1=input("\nIngrese el nombre del jugador n° 1 y luego precione ENTER\n").upper()
  Jugador2=input("\nIngrese el nombre del jugador n° 2 y luego precione ENTER\n").upper()
  Turno=True
  print(f"Es el turno de: {Jugador1}")

  
  while (True):
    
    palabra=traerPalabra(palabras)
    
    letrasPorAdivinar= set(palabra)
    utilizadas=set()

    abcd=set(string.ascii_uppercase)
    bandera= False

    Vida=8

    while len(letrasPorAdivinar) > 0 and Vida > 0:
      if bandera:
        print(f"Vidas disponibles: {Vida} \nLetras utilizadas: {' '.join(utilizadas)}")
        if Turno==True:
          print(f"Es el turno de: {Jugador1}")
        else:
          print(f"Es el turno de: {Jugador2}")

      listaPalabras=[letra if letra in utilizadas
      else '-' for letra in palabra]
      print(vidas[Vida])
      print(f"Palabra: {' '.join(listaPalabras)}")

      letraSeleccionada = input("Selecciona una letra: ").upper()
      bandera=True

      if letraSeleccionada in abcd and not letraSeleccionada in utilizadas:
        utilizadas.add(letraSeleccionada)
      
        if letraSeleccionada in letrasPorAdivinar:
          letrasPorAdivinar.remove(letraSeleccionada)
          print(' ')
          if len(letrasPorAdivinar)>0:
            print("¡Letra ADIVINADA!")
          else:
            print("¡Palabra ADIVINADA!")
            if Turno==True:
              print(f"¡¡¡Gana {Jugador1}!!!")
            else:
              print(f"¡¡¡Gana {Jugador2}!!!")
        else:
          Vida-=1
          print(f"\nLa letra '{letraSeleccionada}' no está en la palabra.")
          Turno=cambioTurno(Turno)

      elif letraSeleccionada in utilizadas:
        print(f"\nLa letra '{letraSeleccionada}' ya fue utilizada, por favor ingresá una letra nueva.")
      else:
        print(f"\nEl caracter '{letraSeleccionada}' no es válido, ingrese otro.")

    if Vida==0:
      print(vidas[Vida])
      print("La palabra a adivinar era: "+palabra)
      print(vidas[10])
      resetearVidas=input("Si desea volver a jugar escriba 'SI'.").upper()
    else:
      print("La palabra era: "+palabra)
      print(vidas[12])
      resetearVidas=input("Si desea volver a jugar escriba 'SI'.").upper()

    if resetearVidas=="SI":
      Vidas=8
      palabra=traerPalabra(palabras)
      JuegoVS()
    else:
      break

def cambioTurno(Turno):

  if Turno== True:
    return False
  else:
    return True
      
Inicio()
