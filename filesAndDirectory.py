import os, send2trash, hashlib,tqdm

def isUserFile(file:str)->bool:
    try :
        """Check if the file is a user file or not."""
        prefixList =  [".", "__", "~", "._", "$", "_"]
        if file.startswith(tuple(prefixList)):
            return False
        return True
    except Exception as e:
        print(f"Erreur : {e}", e.__traceback__.tb_lineno)

def isUserDirectory(path:str)->bool:
    """Check if the directory is a user directory or not."""
    try :
        prefixList =  [".", "__", "~", "._", "$", "_"]
        if path.split('/')[-1].startswith(tuple(prefixList)) or path.split('\\')[-1].startswith(tuple(prefixList)):
            return False
        return True
    except Exception as e:
        print(f"Erreur : {e}", e.__traceback__.tb_lineno)

def hash_file(file_path):
    """Generate a hash value for a file. MD5 is used here."""
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
                if isUserFile(file):
                    file_path = os.path.join(root, file)
                    hash_val = hash_file(file_path)
                    if hash_val is not None:
                        filesDict[file_path] = hash_val
        return filesDict
    except Exception as e: 
        print(f"Erreur : {e}", e.__traceback__.tb_lineno)

def deleteDoublon(files:list, keep_oldest:bool=True, fileByFile:bool = False)->None:
    try : 
        for doublon in files:
            # Trier les fichiers par date de modification
            doublon.sort(key=lambda x: os.path.getmtime(x), reverse=not keep_oldest)
            for file_to_delete in doublon[1:]:
                print(f"Suppression du fichier {file_to_delete} qui est identique à {doublon[0]}")
                entry = input("Voulez vous poursuivre ? (y/n) ou entrer pour effacer : ")
                if entry == "" or entry == 'y':
                    try :
                        send2trash.send2trash(file_to_delete)
                    except : 
                        if input(f"Impossible de mettre le fichier ({file_to_delete}) à la corbeille, voulez vous le supprimer définitivement ? (y/n) : ") == 'y':
                            try :
                                os.remove(file_to_delete)
                                print("fichier supprimé")
                            except :
                                print(f"Impossible de supprimer le {file_to_delete}, il est probablement manquant.")
                        else :
                            print("Annulation de la suppression du fichier")
                else :
                    print("Annulation de la suppression du fichier")
    except Exception as e :
         print("Erreur : impossible de supprimer les fichiers :", e, e.__traceback__.tb_lineno)

def findAndRemove_empty_dirs(dir_path):
    """Find and remove empty directories."""
    try :
        empty_dirs = []
        for root, dirs, files in os.walk(dir_path):
            files = [f for f in files if f not in ['.DS_Store','._.DS_Store', '.gitkeep', 'Thumbs.db','.','..']]  # Ignorer certains fichiers
            if not dirs and not files:  # Si le dossier ne contient ni sous-dossiers ni fichiers
                empty_dirs.append(root)
        if not empty_dirs:
            print("Aucun dossier vide trouvé.")
        for dir in empty_dirs:
            try:
                for file in ['.DS_Store', '._.DS_Store']:
                    file_path = os.path.join(dir, file)
                    if os.path.exists(file_path):
                        send2trash.send2trash(file_path)
                print(f"Suppression du dossier vide : {dir}")
                os.rmdir(dir)
                print(f"Dossier vide supprimé : {dir}")
            except Exception as e:
                print(f"Erreur : impossible de supprimer le dossier {dir} : {e}")
        return empty_dirs
    except Exception as e:
        print(f"Erreur : impossible de supprimer les dossiers vides : {e}")

def deleteMenu(find, rep) :
    """Create a menu to delete files in a list."""
    try :
        while True :
            print(" 1 - Conserver les fichiers les plus anciens\n", "2 - Conserver les fichiers les plus récents\n","3 - Voir les fichiers au cas par cas. (BETA)\n","4 - Annuler\n" )
            print("Les fichiers seront déplacés dans la corbeille s'il y a suffisamment de place.")
            entry = input("Saisir une opération : ").rstrip()
            if entry == '1' : 
                deleteDoublon(find)
                break
            elif entry =='2' :
                deleteDoublon(find, keep_oldest=False)
                break
            elif entry == '3' :
                deleteDoublon(find, fileByFile=True)
                break
            elif entry == '4':
                return
            else : 
                print("Operation inconnue")
        print("Opération terminée.")
        print("La suppression des fichiers en double à peut-être rendu des dossiers vides.")
        if input("Voulez vous rechercher les dosssier vides et les supprimer ? (y/n) :") =='y':
            findAndRemove_empty_dirs(rep)
        else :
            print("Opération non executée.")
    except : 
        print("Erreur : impossible d'executer le menu de suppression")

def deleteFiles(files:list)->None:
    """Direcly delete files in a list."""
    try : 
        for file in files:
            try :
                send2trash.send2trash(file)
            except : 
                if input(f"Impossible de mettre le fichier ({file}) à la corbeille, voulez vous le supprimer définitivement ? (y/n) : ") == 'y':
                    try :
                        os.remove(file)
                        print("fichier supprimé")
                    except :
                        print(f"Impossible de supprimer le {file}, il est probablement manquant.")
                    else :
                        print("Annulation de la suppression du fichier")
                else :
                    print("Annulation de la suppression du fichier")
    except Exception as e :
         print("Erreur : impossible de supprimer les fichiers :", e, e.__traceback__.tb_lineno)