locqueen = (2,8)
locknight = (5,8)
listqueen = []
listknight = []
queenx = locqueen[0]
queeny = locqueen[1]
knightx = locknight[0]
knighty = locknight[1]

def formlistqueen():
    global listqueen, queenx, queeny
    for x in range(1,9):
        listqueen.append((x,queeny))
    for y in range(1,9):
        listqueen.append((queenx,y))
    x = queenx
    y = queeny
    while ((x>1) & (y>1)):
        x -= 1
        y -= 1
        listqueen.append((x,y))
    x = queenx
    y = queeny
    while ((x>1) & (y<8)):
        x -= 1
        y += 1
        listqueen.append((x,y))
    x = queenx
    y = queeny
    while ((x<8) & (y>1)):
        x += 1
        y -= 1
        listqueen.append((x,y))
    x = queenx
    y = queeny
    while ((x<8) & (y<8)):
        x += 1
        y += 1
        listqueen.append((x,y))

def formlistknight():
    global listknight
    listknight = [(3,4)]

def checkqueen():
    print(queenx, queeny)
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
