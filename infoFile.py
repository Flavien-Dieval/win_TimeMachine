def isUserFile(file:str)->bool:
    print("Analyse doublon",file)
    prefixList =  [".", "__", "~", "._", "$", "_"]
    if any(file.startswith(prefix) for prefix in prefixList):
        return False
    print("Analyse doublon",file,"OK")
    return True