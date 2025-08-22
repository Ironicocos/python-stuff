class Personaje:
    es_humano = True

    def __init__(self, nombre, nivel = 1, vida = 100, experiencia = 0):
        self.nombre = nombre
        self.nivel = nivel
        self.__vida = vida
        self.__experiencia = experiencia
    def getVida(self):
        return self.__vida
    def setVida(self, newVida):
        if newVida >= 0:
            self.__vida = newVida
            return self.__vida
        else:
            print("Ingrese otro valor")
            return self.__vida
    def getExperiencia(self):
        return self.__experiencia
    def setExperiencia(self, newXP):
        self.__experiencia = newXP
        return self.__experiencia
    def __str__(self):
        return f"Nombre: {self.nombre}\nNivel: {self.nivel}\n{self.__vida}"
    def subirNivel(self):
        characterXP = Personaje.getExperiencia(self) + 10
        Personaje.setExperiencia(self, characterXP)
        self.nivel = self.nivel + 1
    def estado(self):
        if Personaje.getVida(self) > 0:
            print("Vivo")
        else:
            print("Derrotado")
    def restarDaño(self, dmgDealt):
        actualHP = Personaje.getVida(self) - dmgDealt
        Personaje.setVida(self, actualHP)
        return Personaje.estado(self)

jugador1 = Personaje("Thiago", 2, 200, 400)
#Personaje.setVida(jugador1, -300)
print(jugador1)
Personaje.subirNivel(jugador1)
#print(Personaje.getExperiencia(jugador1))
#print(jugador1.nivel)
Personaje.restarDaño(jugador1, 200)