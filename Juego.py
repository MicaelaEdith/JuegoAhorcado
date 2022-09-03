import random
import string
from Palabras import palabras
from Vidas import vidas

def traerPalabra(lista):
    palabra=random.choice(lista)
    return palabra.upper()

def Juego():
  banderaPrimerJuego=True

  while (True):
    if banderaPrimerJuego: 
      print(vidas[11])
    continuar=input("Presione una tecla para continuar.")
    palabra=traerPalabra(palabras)
    
    letrasPorAdivinar= set(palabra)
    adivinadas=set()

    abcd=set(string.ascii_uppercase)
    bandera= False

    Vida=8

    while len(letrasPorAdivinar) > 0 and Vida > 0:
      if bandera:
        print(f"Vidas disponibles: {Vida} \nLetras utilizadas: {' '.join(adivinadas)}")

      listaPalabras=[letra if letra in adivinadas
      else '-' for letra in palabra]
      print(vidas[Vida])
      print(f"Palabra: {' '.join(listaPalabras)}")

      letraSeleccionada = input("Selecciona una letra: ").upper()
      bandera=True

      if letraSeleccionada in abcd and not letraSeleccionada in adivinadas:
        adivinadas.add(letraSeleccionada)
      
        if letraSeleccionada in letrasPorAdivinar:
          letrasPorAdivinar.remove(letraSeleccionada)
          print(' ')
        else:
          Vida-=1
          print(f"\nLa letra '{letraSeleccionada}' no está en la palabra.")

      elif letraSeleccionada in adivinadas:
        print(f"\nLa letra '{letraSeleccionada}' ya fue utilizada, por favor ingresá una letra nueva.")
      else:
        print(f"\nEl caracter '{letraSeleccionada}' no es válido, ingrese otro.")

    if Vida==0:
      print(vidas[Vida])
      print("La palabra a adivinar era: "+palabra)
      print(vidas[10])
      resetearVidas=input("Si desea volver a jugar escriba 'SI'.").upper()
    else:
      print(vidas[12])
      resetearVidas=input("Si desea volver a jugar escriba 'SI'.").upper()

    if resetearVidas=="SI":
      banderaPrimerJuego=False
      Vidas=8
      palabra=traerPalabra(palabras)
    else:
      break

Juego()
