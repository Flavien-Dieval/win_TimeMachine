import TwoRepScanner, autosave, doublonScan, filesAndDirectory
import os 

def repDuppli():
    try :
        while True : 
            pathDisk1 = input("Saisir le chemin vers le premier repertoire à scanner : ")
            if os.path.exists(pathDisk1):
                break
            else :
                print("Erreur : le repertoire n'existe pas.")
        while True : 
            pathDisk2 = input("Saisir le chemin vers le second repertoire à scanner : ")
            if os.path.exists(pathDisk2):
                break
            else :
                print("Erreur : le repertoire n'existe pas.")
        TwoRepScanner.twoRepScanner(pathDisk1, pathDisk2)
    except KeyboardInterrupt:
        print("Opération annulée.")
    except ModuleNotFoundError:
        print("Erreur : le module tqdm ou os n'est pas installé. Veuillez l'installer pour continuer.")
    except Exception as e:
        print("Erreur lors de l'analyse des fichiers en doubles.: ", e)

def save():
    try :
        while True : 
            pathDisk1 = input("Saisir le chemin vers le repertoire original : ")
            if os.path.exists(pathDisk1):
                break
            else :
                print("Erreur : le repertoire n'existe pas.")
        while True : 
            pathDisk2 = input("Saisir le chemin le repertoire de sauvegarde : ")
            if os.path.exists(pathDisk2):
                break
            else :
                print("Erreur : le repertoire n'existe pas.")
        autosave.autosave(pathDisk1, pathDisk2)
    except KeyboardInterrupt:
        print("Opération annulée.")
    except ModuleNotFoundError:
        print("Erreur : le module tqdm ou os n'est pas installé. Veuillez l'installer pour continuer.")
    except Exception as e:
        print("Erreur lors de l'analyse des fichiers en doubles.: ", e)

def logo():
    print(r"          _              _____ _                                       _     _             ")
    print(r"__      _(_)_ __        /__   (_)_ __ ___   ___   _ __ ___   __ _  ___| |__ (_)_ __   ___  ")
    print(r"\ \ /\ / / | '_ \         / /\/ | '_ ` _ \ / _ \ | '_ ` _ \ / _` |/ __| '_ \| | '_ \ / _ \ ")
    print(r" \ V  V /| | | | |       / /  | | | | | | |  __/ | | | | | | (_| | (__| | | | | | | |  __/ ")
    print(r"  \_/\_/ |_|_| |_|____   \/   |_|_| |_| |_|\___| |_| |_| |_|\__,_|\___|_| |_|_|_| |_|\___| ")
    print(r"                |_____|                                                                    ")

def main():
    try :
        logo()
        while True : 
            print("Usage :")
            print("\t1 - Doublons (1 repertoires)\n\t2 - Doublons (2 repertoires) \n\t3 - Retirer les disques vides \n\t4 - Sauvegarder (WORK IN PROGRESS) \n\t5 - Quitter")
            entry = input("Saisir une opération : ").split(" ")[0].rstrip()
            if entry == '1' : 
                while True : 
                    path = input("Saisir le chemin vers le repertoire à scanner : ")
                    if os.path.exists(path):break
                    else :print("Erreur : le repertoire n'existe pas.")
                doublonScan.doublonScanRep(path)
                input("Appuyer sur une touche pour continuer.")
            elif entry == '2':
                repDuppli()
                input("Appuyer sur une touche pour continuer.")
            elif entry == '3':
                save()
                input("Appuyer sur une touche pour continuer.")
            elif entry == '4':
                filesAndDirectory.findAndRemove_empty_dirs()
            elif entry =='5':
                print("Au revoir.")
                exit()
            else :
                print("Commande non reconnue.")
    except KeyboardInterrupt:
        print("Au revoir.")
    except Exception as e:
        print("Erreur critique : ", e, e.__traceback__.tb_lineno)

main()