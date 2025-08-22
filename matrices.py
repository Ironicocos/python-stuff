"""
def getPlayerPos():
    posCounter = -1
    filaCounter = -1
    for filas in range(len(mapa)):
        filaCounter += 1
        for columnas in range(4):
            posCounter += 1
            if mapa[filas][columnas] == "P":
                if posCounter > 3:
                    posCounter = 0
                    return posCounter, filaCounter
"""
"""
def getFila():
    newFila = 0
    if actualPlayerPos > 0 and actualPlayerPos < 5:
        newFila = 1
    elif actualPlayerPos > 4 and actualPlayerPos < 9:
        newFila = 2
    elif actualPlayerPos > 8 and actualPlayerPos < 12:
        newFila = 3
    return newFila
def getColumna():
    newColumna = actualPlayerPos - 4
    return newColumna
"""
mapa = [
 [" ", " ", "Mambo", " "],
 ["P", " ", " ", "Hachimi"],
 ["Mambo", " ", "Mambo", " "]
]
def showMap():
    for filas in mapa:
        print(filas)
def getPlayerPos():
    for filas in range(len(mapa)):
        for columnas in range(len(mapa[filas])):
            if mapa[filas][columnas] == "P":
                return filas, columnas
playerFila, actualPlayerPos = getPlayerPos()
def gameState():
    gameState = True
    for filas in range(len(mapa)):
        for columnas in range(len(mapa[filas])):
            if mapa[filas][columnas] == "PHachimi":
                gameState = False
                print("Aún no has llegado a la meta")
                return gameState
            else:
                gameState = True
                return gameState
def mamboState():
    enemyFound = False
    for filas in range(len(mapa)):
        for columnas in range(len(mapa[filas])):
            if mapa[filas][columnas] == "PMambo":
                enemyFound = True
                print("Te encontraste con un MAMBO")
                return enemyFound
            else:
                enemyFound = False
                return enemyFound
mambo = mamboState()
gameData = gameState()
def playerMovement():
    print("'W' para moverse hacia arriba, 'S' hacia abajo, 'A' hacia atrás, 'D' hacia delante")
    newPos = input()
    if newPos == 'W':
        newColumna = actualPlayerPos
        newFila = playerFila - 1
    elif newPos == 'S':
        newColumna = actualPlayerPos
        newFila = playerFila + 1
    elif newPos == 'A' and actualPlayerPos > 0:
        newColumna = actualPlayerPos - 1
        newFila = playerFila
    elif newPos == 'D':
        newColumna = actualPlayerPos + 1
        newFila = playerFila
    else:
        newColumna = actualPlayerPos
        newFila = playerFila
        print("El valor ingresado no coincide con ninguna de las opciones")
    for filas in range(3):
        for columnas in range(4):
            if mapa[filas][columnas] == "P":
                mapa[filas][columnas] = " "
                mapa[newFila][newColumna] = "P" + mapa[newFila][newColumna]
    showMap()
    gameState()
    mamboState()
def gameStart():
    while gameData == True and mambo == False:
        playerMovement()
gameStart()