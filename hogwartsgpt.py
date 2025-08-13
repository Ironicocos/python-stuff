import random

hechizos_basicos = ["Lumos", "Alohomora", "Wingardium Leviosa"]
atkSpells = ["Lumos", "Nox", "Alohomora", "Colloportus", "Wingardium Leviosa",
             "Accio", "Depulso", "Locomotor", "Scourgify", "Reparo", "Aparecium",
             "Rictusempra", "Tarantallegra", "Sonorus", "Quietus"]
randomSpell = random.choice(atkSpells)

def spellCast():
    learntSpell = False
    print(f"El jugador castea {randomSpell}")
    if randomSpell in hechizos_basicos:  # más simple que el for
        learntSpell = True
        print("Hechizo casteado con éxito")
    else:
        print("Aún no aprendiste ese hechizo")
    return learntSpell  # devolvemos el estado

# Guardamos el resultado
aprendido = spellCast()
print("Estado de aprendizaje:", aprendido)