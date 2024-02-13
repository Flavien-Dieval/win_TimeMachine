import doublescanner
import tqdm, os 

def doublon():
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
        doublescanner.diskScanner(pathDisk1, pathDisk2)
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
    logo()
    while True : 
        print("Usage :")
        print("\t1 - Fichiers duppliqués (2 repertoires), \n\t2 - Doublon \n\t3 - Sauvegarder \n\t4 - Quitter")
        entry = input("Saisir une opération : ").split(" ")[0].rstrip()
        if entry == '1' : 
            doublon()
            input("Appuyer sur une touche pour continuer.")
        elif entry =='5':
            exit()
        else :
            print("Commande non reconnue.")



main()