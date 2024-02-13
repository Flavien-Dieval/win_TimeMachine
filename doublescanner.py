import difflib
import os
import tqdm 
def isIdentique(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.readlines()
        text2 = f2.readlines()

    diff = list(difflib.unified_diff(text1, text2, fromfile=file1, tofile=file2, n=3))

    if not diff:
        print("Les deux fichiers sont identiques.")
        return True
    return False

def isFileSystem(file:str)->bool:
    return file.startswith(".") or file.startswith("__")

def diskScanner(dis1: str="/chemin/vers/repertoire/racine", dis2: str="/chemin/vers/repertoire/externe"):
    filesDictDisk1 = {}
    filesDictDisk2 = {}
    for racine, dossiers, fichiersDisk1 in tqdm.tqdm(os.walk(dis1)):
        for fichier in fichiersDisk1:
            if isFileSystem(fichier):
                continue
            else:
                chemin_fichier = os.path.join(racine, fichier)
                filesDictDisk1[fichier] = chemin_fichier  # stocker le nom du fichier comme clé
    for racine, dossiers, fichiersDisk2 in tqdm.tqdm(os.walk(dis2)):
        for fichier in fichiersDisk2:
            if isFileSystem(fichier):
                continue
            else:
                chemin_fichier = os.path.join(racine, fichier)
                filesDictDisk2[fichier] = chemin_fichier  # stocker le nom du fichier comme clé

    for fichier in tqdm.tqdm(filesDictDisk1):
        if fichier in filesDictDisk2:  # vérifier si le nom du fichier existe dans le deuxième dictionnaire
            if isIdentique(str(filesDictDisk1[fichier]), str(filesDictDisk2[fichier])):
                print(f"Les fichiers {fichier} sont identiques : ", filesDictDisk1[fichier], filesDictDisk2[fichier])
