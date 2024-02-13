import difflib
import os
import tqdm 
def isIdentique(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.readlines()
        text2 = f2.readlines()

    diff = list(difflib.unified_diff(text1, text2, fromfile=file1, tofile=file2, n=3))

    if not diff:
        return True
    return False

def isFileSystem(file:str)->bool:
    return file.startswith(".") or file.startswith("__")

def scanDisk(disk: str) -> list:
    filesDict = []
    for root, _, files in tqdm.tqdm(os.walk(disk)):
        for file in files:
            if not isFileSystem(file):
                file_path = os.path.join(root, file)
                filesDict.append((file_path, file))
    return filesDict

def diskScanner(disk1: str, disk2: str)->None:
    print("Analyse des fichiers en cours ... ")
    print("Veuillez patienter ... ")
    filesDictDisk1 = scanDisk(disk1)
    filesDictDisk2 = scanDisk(disk2)
    cmptFind = 0
    print("Comparaison des fichiers en cours ... ")
    for i in tqdm.tqdm(range(len((filesDictDisk1)))):
        for j in range(len(filesDictDisk2)):
            if filesDictDisk1[i][1] == filesDictDisk2[j][1]:  # vérifier si le nom du fichier existe dans le deuxième dictionnaire
                if isIdentique(str(filesDictDisk1[i][0]), str(filesDictDisk2[j][0])):
                    cmptFind += 1
                    if cmptFind == 1:
                        print("Les fichiers suivants sont identiques : ")
                    print(f"{cmptFind}{filesDictDisk1[i][0]} = {filesDictDisk2[j][0]} ")
    print(f"Analyse terminée. TOTAL : {cmptFind}")


def uniqueRepDuppli(rep:str)-> None:
    print("Analyse des fichiers en cours ... ")
    print("Veuillez patienter ... ")
    filesinRep = scanDisk(rep)
    find = []
    cmptFind = 0
    for i in tqdm.tqdm(range(len(filesinRep))):
        cmpt = 0
        for j in range(len(filesinRep)):
            if i !=j and isIdentique(filesinRep[i][0], filesinRep[j][0]):
                cmptFind += 1
                if cmptFind == 1:
                    print("Les fichiers suivants sont identiques : ")
                print(f"{filesinRep[i][1]} = {filesinRep[j][1]} ")
    print(f"Analyse terminée. TOTAL : {cmptFind}")