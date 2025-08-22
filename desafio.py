mapa = [
 ["", " ", "E", " "],
 ["P", " ", " ", "M"],
 [" ", " ", "E", " "],
]
playerStatus = ""
# wasd = input()

def showMap():
    for i in mapa:
        print(f"{i}")
"""
def movePlayer():
    playerPos = mapa.index("P")
    print("Presiona W para ir hacia arriba, A para ir hacia atrás, S para abajo, D para delante")
    #wasd

def gameStart():
    while playerStatus != "PM":
        movePlayer()
        showMap()
"""
def getPlayerPos():
    #pos = -1
    #playerStatus = False
    for filas in mapa:
        print(filas)
        for columnas in mapa:
            print(columnas)
print(getPlayerPos())
