enemigo = {
    "Goblin": {"vida": 500, "daño": 20},
    "Orco" : {"vida": 700, "daño": 50},
    "Troll": {"vida": 500, "daño": 100}, 
    "Esqueleto" : {"vida": 200, "daño": 500}, 
    "Zombie" : {"vida": 500, "daño": 10}, 
    "Dragón" : {"vida": 10000, "daño": 100000}
}
def displayEnemies():
    for i in enemigo.keys():
        print(f"{i}")
def dealDMG(enemyName, dmg):
