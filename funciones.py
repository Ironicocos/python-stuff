playerInventory = ["Espada corta", "Arco", "Flechas", "Poción de salud", "Poción de mana", "Escudo de hierro",
"Capa de invisibilidad", "Pergamino de fuego", "Pergamino de hielo", "Llave antigua", "Monedas de oro", 
"Anillo mágico", "Botas de velocidad", "Casco de protección", "Fruta mágica", "Mapa del tesoro",
"Amuleto de fuerza", "Piedra de teletransporte", "Cuerda resistente", "Antorcha"]
def showInventory():
    for i in playerInventory:
        print(i)
def addItem(newItem):
    playerInventory.append(newItem)
    if playerInventory.count(newItem) >= 1:
        print("Item agregado con éxito")
def checkItem(item):
    if playerInventory.count(item) >= 1:
        return True
    else:
        return False
def eraseItem(itemName):
    itemStatus = checkItem(itemName)
    if itemStatus == True:
        playerInventory.remove(itemName)
        print("Item eliminado con éxito")
    else:
        print("El item no se encuentra dentro del inventario")

eraseItem("Pera")