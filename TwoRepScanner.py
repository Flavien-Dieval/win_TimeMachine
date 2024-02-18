import os
import filesAndDirectory
import tqdm 

def twoRepScanner(disk1: str, disk2: str)->None:
    try :
        print("Analyse des fichiers en cours ... ")
        print("Veuillez patienter ... ")
        filesDisk1 = filesAndDirectory.scanDisk(disk1)
        filesDisk2 = filesAndDirectory.scanDisk(disk2)
        findDisk1 = []
        findDisk2 = []
        print(f"Comparaison des fichiers en cours ... Parmi : {len(filesDisk1)} fichiers.")
        for file_path,file_hash in tqdm.tqdm(filesDisk1.items()):
            for other_file_path, other_file_hash  in filesDisk2.items():
                if file_hash == other_file_hash and not os.path.samefile(file_path, other_file_path) and file_path:
                    findDisk1.append(file_path)
                    findDisk2.append(other_file_path)
        if len(findDisk1) == 0:
            print("Aucun fichier en double n'a été trouvé.")
        else :
            print("Les fichiers suivants sont identiques : ")
            for i in range(len(findDisk1)):
                print(f"{i} | {findDisk1[i]} = {findDisk2[i]}")
        print(f"Analyse terminée. TOTAL : {len(findDisk1)}")
        if len(findDisk1)>0 and input("Voulez-vous supprimer les fichiers en double ? (y/n) : ") == 'y':
            while True : 
                print(f"Veuillez choisir les fichiers à effacer :\n\t1 - Les fichiers originaires du repertoire 1 : {disk1}\n\t2 -Les fichiers originaires du repertoire 2 : {disk2}\n\t 3 - Annuler")
                entry = input("Saisir une opération : ").rstrip()
                if entry == '1':    
                    filesAndDirectory.deleteFiles(findDisk1)
                    break
                elif entry == '2':
                    filesAndDirectory.deleteFiles(findDisk2)
                    break
                elif entry == '3':
                    break
        print("Opération terminée.")
    except Exception as e:
        print(f"Erreur : {e}", e.__traceback__.tb_lineno, e.__traceback__.tb_frame.f_code.co_filename)
