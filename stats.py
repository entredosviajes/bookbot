def sort_on(items):
    return items["num"]

def sortedDicts(dictio):
    dictList = []
    for key in dictio:
        unitDict = {}
        unitDict['char'] = key
        unitDict['num'] = dictio[key]
        dictList.append(unitDict)
    dictList.sort(reverse=True, key=sort_on)
    return dictList

def count(text):
    return len(text.split())

def countChars(text):
    lower = text.lower()
    dico = {}
    for char in lower:
        value = dico.get(char, 0) + 1
        dico[char] = value
    return dico

