class Personaje:
    es_humano = True

    def __init__(self, nombre, nivel = 1, vida = 100, experiencia = 0):
        self.__nombre = nombre
        self.__nivel = nivel
        self.__vida = vida
        self.__experiencia = experiencia
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, newName):
        self.__nombre = newName
    @property
    def nivel(self):
        return self.__nivel
    @nivel.setter
    def nivel(self, newLvl):
        self.__nivel = newLvl
    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self, newVida):
        if newVida >= 0:
            self.__vida = newVida
        else:
            print("Ingrese otro valor")
    @property
    def experiencia(self):
        return self.__experiencia
    @experiencia.setter
    def experiencia(self, newXP):
        self.__experiencia = newXP
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nNivel: {self.nivel}\n{self.__vida}"
    def subirNivel(self):
        self.experiencia = self.experiencia + 10
        self.nivel = self.nivel + 1
    def estado(self):
        if self.vida > 0:
            print("Vivo")
        else:
            print("Derrotado")
    def restarDaño(self, dmgDealt):
        self.vida = self.vida - dmgDealt
        return Personaje.estado(self)

jugador1 = Personaje("Thiago", 2, 200, 400)
#Personaje.setVida(jugador1, -300)
print(jugador1)
Personaje.subirNivel(jugador1)
#print(Personaje.getExperiencia(jugador1))
#print(jugador1.nivel)
Personaje.restarDaño(jugador1, 200)