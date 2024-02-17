import os
import filesAndDirectory
import tqdm
import hashlib

def isIdentique(file1, file2):
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
                if filesAndDirectory.isUserFile(file):
                    file_path = os.path.join(root, file)
                    hash_val = hash_file(file_path)
                    if hash_val is not None:
                        filesDict[file_path] = hash_val
        return filesDict
    except Exception as e: 
        print(f"Erreur : {e}", e.__traceback__.tb_lineno)

def removeIdenticalFiles(files: list)->list:
    """Remove identical files from a list."""
    for file in files:
        if [file[1], file[0]] in files:
            files.remove([file[1], file[0]])
    return files

def doublonScanRep(rep:str)-> None:
    try :
        print("Analyse des fichiers en cours ... ")
        print("Veuillez patienter ... ")
        filesinRep = scanDisk(rep)
        find = []
        print(f"Comparaison des fichiers en cours ... Parmi : {len(filesinRep)} fichiers.")
        for file_path,file_hash in tqdm.tqdm(filesinRep.items()):
            for other_file_path, other_file_hash  in filesinRep.items():
                if file_hash == other_file_hash and not os.path.samefile(file_path, other_file_path) and file_path:
                    find.append([file_path, other_file_path])
        if len(find) == 0:
            print("Aucun fichier en double n'a été trouvé.")
        else :
            print("Les fichiers suivants sont identiques : ")
            find = removeIdenticalFiles(find)
            for i in range(len(find)):
                print(f"{i} | {find[i][0]} = {find[i][1]}")
        print(f"Analyse terminée. TOTAL : {len(find)}")
        if len(find)>0 and input("Voulez-vous supprimer les fichiers en double ? (y/n) : ") == 'y':
            filesAndDirectory.deleteMenu(find, rep)
        print("Opération terminée.")
    except Exception as e:
        print(f"Erreur : {e}", e.__traceback__.tb_lineno, e.__traceback__.tb_frame.f_code.co_filename)
