import os
import filesAndDirectory
import tqdm 

def isIdentique(file1, file2):
    """Check if two files are identical in content."""
    if not filesAndDirectory.isUserFile(file1) or not filesAndDirectory.isUserFile(file2):
        return False
    try :
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            text1 = f1.read()
            text2 = f2.read()
        return text1 == text2
    except PermissionError as e:
        print(f"Erreur: permission refusée")

    except Exception as e:
        print(f"Erreur : impossible de decoder le fichier {file1} ou {file2} {e}", e.__traceback__.tb_lineno, e.__traceback__.tb_frame.f_code.co_filename, file1, file2)
        return False

def scanDisk(disk: str) -> list:
    """Scan the disk and return a list of files."""
    try :
        filesDict = []
        for root, dirs, files in tqdm.tqdm(os.walk(disk)):
            dirs[:] = [d for d in dirs if not d[0] == '.' and  d !="AppData"]  # Ignorer les dossiers commençant par un point
            for file in files:
                if not filesAndDirectory.isUserFile(file) or file.startswith(".") or file.startswith("__") or file.startswith('~') or file.startswith("._") or file.startswith("$") or file.startswith("_"):
                    file_path = os.path.join(root, file)
                    filesDict.append((file_path, file))
        return filesDict
    except Exception as e: 
        print(f"Erreur : {e}", e.__traceback__.tb_lineno)

def diskScanner(disk1: str, disk2: str)->None:
    try :
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
    except Exception as e:
        print(f"Erreur : {e}", e.__traceback__.tb_lineno, e.__traceback__.tb_frame.f_code.co_filename, filesDictDisk1[i][0], filesDictDisk2[j][0])
