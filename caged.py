#!/bin/python3
import urllib.request
import os
import platform
import zipfile
import shutil
import random

        

###Variables necesarias

home = os.path.expanduser("~")
path = os.path.join(home, "NicolasCage.zip")
pathToExtract = os.path.join(home, "NicolasCage")

### Descargar imagenes.

def downloadImages(url):
    os.mkdir(pathToExtract)
    urllib.request.urlretrieve(url, path)

    zip_ref = zipfile.ZipFile(path, 'r')
    zip_ref.extractall(pathToExtract)
    zip_ref.close()
        

def saveToLog(imagen):
    #Creamos el log.
    
    logFile = open('caged.log', 'a')
    logFile.write(imagen + '\n')

def copiImages():
    for path, names, files in os.walk(home):
        for name in names:
            imagen1 =  os.path.join(pathToExtract,
                                    str(random.randint(0, 22)) + ".jpg")
            imagen = str(random.randint(0, 22)) + ".jpg"
            direct = os.path.join(path, name)
            a_copiar = os.path.join(direct, imagen)
            if not os.path.isfile(a_copiar):
               # print("aqui copiaria" + str(a_copiar))
                shutil.copy(imagen1, a_copiar)
                saveToLog(str(a_copiar))
                
random.seed()
downloadImages("http://jose-linares.com/Nicolas_Cage_Faces.zip")
copiImages()
