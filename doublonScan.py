import os
import filesAndDirectory
import tqdm,time

def removeIdenticalFiles(files: list)->list:
    """Remove identical files from a list."""
    seen = set()
    unique_files = []
    for file in tqdm.tqdm(files):
        # Convert the file to a tuple so it can be added to a set
        file_tuple = tuple(file)
        # Check if the file or its reverse is in the set
        if file_tuple not in seen and file_tuple[::-1] not in seen:
            # Add the file and its reverse to the set
            seen.add(file_tuple)
            seen.add(file_tuple[::-1])
            # Add the file to the list of unique files
            unique_files.append(file)
    return unique_files

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
            print("Analyse terminée, optimisation des résultats ...")
            start = time.time()
            find = removeIdenticalFiles(find)
            input(time.time()-start)
            print("Les fichiers suivants sont identiques : ")
            for i in range(len(find)):
                print(f"{i} | {find[i][0]} = {find[i][1]}")
        print(f"Analyse terminée. TOTAL : {len(find)} doublons trouvés.")
        if len(find)>0 and input("Voulez-vous supprimer les fichiers en double ? (y/n) : ") == 'y':
            filesAndDirectory.deleteMenu(find, rep)
        print("Opération terminée.")
    except Exception as e:
        print(f"Erreur : {e}", e.__traceback__.tb_lineno, e.__traceback__.tb_frame.f_code.co_filename)
