# Script que limpia las salidas

from os import remove

lista=["Salida.mp4","Salida.ogg","Salida.flv","Salida.mp3","Salida.png","Salida.jpeg","Salida.bmp","Salida.gif"]

for x in lista:
    try: remove(x)
    except: pass

input("Salidas Limpiadas :) ")    
