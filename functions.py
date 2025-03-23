import os
from pathlib import Path
import time
from DICT import *

def all_files_dirs(chemin):
    all_files = []
    all_contens = os.walk(chemin)
    for root, dirs, files in all_contens:
        for file in files:
            full_path = Path(root)/file
            if full_path not in all_files:
                all_files.append(full_path)
    return all_files

def type_dest(file):
    for key, value in typesExtension.items():
        if file.suffix in value:
            return key
    return "Autres"

def finalDir(file, mainDir):
    destinationType = type_dest(file)
    details = os.stat(file)
    year = str(time.gmtime(details.st_birthtime).tm_year)
    month = months[time.gmtime(details.st_birthtime).tm_mon]
    return Path(mainDir)/destinationType/year/month

def move(file, destination):
    os.makedirs(destination, exist_ok=True)
    try:
        file.rename(destination/file.name)
    except FileExistsError:
        file.replace(destination/file.name)