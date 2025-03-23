import logging
from functions import *

dir = ""
while len(dir) <1:
    dir = input("Chemin du dossier à réordonner : ")
    if len(dir) < 1:
        print("Saisie incorrect ")

DOSSIER = Path(dir)
allFIles = all_files_dirs(DOSSIER)
if len(allFIles) < 1:
    print("Sans Contenu")
else:
    logging.basicConfig(filename= Path(DOSSIER/'Moving-process.log'), 
                    filemode = 'w',
                    level=logging.INFO,
                    encoding='utf-8')
    for file in allFIles:
        destination = finalDir(file, DOSSIER)
        try:   
            move(file, destination)
            logging.info(f"Fichier {file.name} déplacé vers {destination}")
        except PermissionError:
            print(file.name)
            pass