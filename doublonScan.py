import os
import infoFile
import tqdm
import hashlib

def isIdentique(file1, file2):
    if not infoFile.isUserFile(file1) or not infoFile.isUserFile(file2):
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

def hash_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except PermissionError as e:
        print(f"Erreur : permission refusée pour le fichier {file_path}")
        return None
    except Exception as e:
        print(f"Erreur : impossible de générer une valeur de hachage pour le fichier {file_path}. Erreur : {e}")
        return None

def scanDisk(disk: str) -> dict:
    try :
        filesDict = {}
        for root, dirs, files in tqdm.tqdm(os.walk(disk)):
            dirs[:] = [d for d in dirs if not d[0] == '.' and  d !="AppData"]  # Ignorer les dossiers commençant par un point
            for file in files:
                if not infoFile.isUserFile(file):
                    file_path = os.path.join(root, file)
                    hash_val = hash_file(file_path)
                    if hash_val is not None:
                        print("OK")
                        filesDict[hash_val] = file_path
        return filesDict
    except Exception as e: 
        print(f"Erreur : {e}", e.__traceback__.tb_lineno)

def doublonScanRep(rep:str)-> None:
    try :
        print("Analyse des fichiers en cours ... ")
        print("Veuillez patienter ... ")
        filesinRep = scanDisk(rep)
        cmptFind = 0
        print(f"Comparaison des fichiers en cours ... Parmis : {len(filesinRep)} fichiers.")
        i = 0
        for file_hash, file_path in tqdm.tqdm(filesinRep.items()):
            i += 1
            j = 0
            for other_file_hash, other_file_path in filesinRep.items():
                j += 1
                if file_hash != other_file_hash and os.path.samefile(file_path, other_file_path):
                    cmptFind += 1
                    if cmptFind == 1:
                        print("Les fichiers suivants sont identiques : ")
                    print(f"{cmptFind}{os.path.basename(file_path)} = {os.path.basename(other_file_path)} ")
        print(f"Analyse terminée. TOTAL : {cmptFind}")
    except Exception as e:
        print(f"Erreur : {e}", e.__traceback__.tb_lineno, e.__traceback__.tb_frame.f_code.co_filename)