import os 
import doublescanner

def autosave(disk1 ,disk2):
    for racine, dossiers, fichiersDisk1 in os.walk(disk1):
        for fichier in fichiersDisk1:
            if doublescanner.isFileSystem(fichier):
                continue
            else:
                chemin_fichier = os.path.join(racine, fichier)
                notInDisk2 = False
                if fichier in doublescanner.filesDictDisk2:
                    if doublescanner.isIdentique(str(doublescanner.filesDictDisk1[fichier]), str(doublescanner.filesDictDisk2[fichier])):
                        print(f"Les fichiers {fichier} sont identiques : ", doublescanner.filesDictDisk1[fichier], doublescanner.filesDictDisk2[fichier])
                    else:
                        notInDisk2 = True
                else:
                    notInDisk2 = True
                if notInDisk2:
                    print(f"Le fichier {fichier} n'existe pas dans le répertoire de sauvegarde.")
                    print(f"Le fichier {fichier} sera copié dans le répertoire de sauvegarde.")
                    #os.system(f"cp {doublescanner.filesDictDisk1[fichier]} {disk2}")
    print("La sauvegarde est terminée.")

autosave("/Users/flaviendieval/Downloads", "/Users/flaviendieval/Documents")
