#ejemplo de convertir formato de audio
input("""\nConvertir archivo de mp3 a OGG\n
              Input     ->  Oputput
  ffmpeg -i Sonido1.mp3     Salida.ogg \n
        """)

from os import system

system(" ffmpeg -i Sonido1.mp3 Salida.ogg") #<--comando

input("\n abriendo Salida.ogg \n")
system("Salida.ogg") #<-- abriendo
