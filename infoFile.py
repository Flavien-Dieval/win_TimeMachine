def isUserFile(file:str)->bool:
    listTypeOk = [".txt", ".pdf", ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".mp3", ".wav", ".mov", ".avi", ".mkv","doc", "docx", "xls", "xlsx", "ppt", "pptx", "odt", "ods", "odp", "odg", "odf", "odc", "odi", "odm", "ott", "ots", "otp", "otg", "otf", "otc", "oti", "oth","pkt","html", "htm", "xml", "css", "js", "json", "php", "c", "cpp", "h", "hpp", "java", "py", "sh", "bat","csv",".psd",".ia","mp4","m4a",".py","aac",".zip",".rar",".tar",".gz",".7z",".bz2",".xz",".iso",".dmg",".img",".exe",".msi",".deb",".rpm",".apk",".app",".ipa",".jar",".war",".ear",".tar.gz",".tar.bz2",".tar.xz",".ogg",".flac",".m4a",".wma",".aiff",".aif",".mid",".midi",".amr",".mka",".opus",".webm",".flv"]
    if file.startswith(".") or file.startswith("__"):
        return False
    for typeFile in listTypeOk:
        if file.endswith(typeFile):
            return True
    return False