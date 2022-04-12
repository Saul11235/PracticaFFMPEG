#ejemplo de convertir formato de video a gif
input("""\nConvertir archivo de mp3 a OGG\n
              Input     ->  Oputput
  ffmpeg -i  Video1.mp4     Salida.gif\n
        """)

from os import system

system(" ffmpeg -i Video1.mp4 Salida.gif") #<--comando

input("\n abriendo Salida.gif \n")
system("Salida.gif") #<-- abriendo
