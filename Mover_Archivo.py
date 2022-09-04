import imp
import os
import shutil
from unicodedata import name
from xml.dom import IndexSizeErr

from_dir = r"C:/Users/tomas/Downloads"
to_dir = r"D:/Proyectos de la escuela/Quinta etapa/Clase 102/Proyecto clase 102"

list_of_files = os.listdir(from_dir)
#print(list_files)

for indice in list_of_files:
    name_extension = os.path.splitext(indice)
   # print(name_extension[0])
   # print(name_extension[1])

    if(name_extension[1] == ""):
        continue

    if(name_extension[1] in [".txt", ".doc", ".docx", ".pdf"]):
        path1 = from_dir + "/" + indice
        path2 = to_dir + "/" + "Archivos de documentos"
        path3 = to_dir + "/" + "Archivos de documentos" + "/" + indice
        #print(path1)
        #print(path3)
        if(os.path.exists(path2)):
            print("Moviendo" + indice)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moviendo" + indice)
            shutil.move(path1, path3)    