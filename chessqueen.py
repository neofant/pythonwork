locqueen = (3,4)
locknight = (5,8)
listqueen = []
listknight = []

def formlistqueen():
    global listqueen
    listqueen = [(5,8), (1,2)]
    return listqueen

def formlistknight():
    global listknight
    listknight = [(3,4)]
    return listknight

def checkqueen():
    print(listqueen)
    if locknight in listqueen:
        print("Queen takes knight")

def checkknight():
    if locqueen in listknight:
        print("Knight takes queen")

formlistqueen()
formlistknight()
checkqueen()
checkknight()
