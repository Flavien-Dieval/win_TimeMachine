import doublescanner
import tqdm, os 

def doublon():
    while True : 
        pathDisk1 = input("Saisir le chemin vers le premier repertoire à scanner : ")
        if os.path.exists():
            break
        else :
            print("Erreur : le repertoire n'existe pas.")
    while True : 
        pathDisk2 = input("Saisir le chemin vers le second repertoire à scanner : ")
        if os.path.exists():
            break
        else :
            print("Erreur : le repertoire n'existe pas.")
    doublescanner.diskScanner(pathDisk1, pathDisk2)

def main():
    while True : 
        print("1 - Analyse de doublon entre deux disques\n exit - Quitter")
        entry = input("Saisir une opération : ").rstrip()[0].split(" ")[0]
        if entry == '1' : 
            doublon()
        elif entry =='exit':
            exit()
        else :
            print("Commande non reconnue.")



main()