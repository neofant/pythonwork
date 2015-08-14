locqueen = (2,8)
locknight = (3,4)
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
    global listknight, knightx, knighty
    oqx = (-2,-2,-1,-1,1,1,2,2)
    oqy = (-1,1,-2,2,-2,2,-1,1)
    for i in range (0,8):
        if ((knightx+oqx[i]) > 0) & ((knighty+oqy[i])>0) & ((knightx+oqx[i])<8) & ((knighty+oqy[i])<8):
            listknight.append(((knightx+oqx[i]),(knighty+oqy[i])))

def checkqueen():
    print("List of Queen")
    print(listqueen)
    if locknight in listqueen:
        print("Queen takes knight")

def checkknight():
    print("List of Knight")
    print(listknight)
    if locqueen in listknight:
        print("Knight takes queen")

formlistqueen()
formlistknight()
checkqueen()
checkknight()
