import os
import filesAndDirectory
import tqdm

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
        filesinRep = filesAndDirectory.scanDisk(rep)
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
