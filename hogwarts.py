import random
hechizos_basicos = ["Lumos", "Alohomora", "Wingardium Leviosa"]
atkSpells = ["Lumos", "Nox", "Alohomora", "Colloportus", "Wingardium Leviosa", "Accio", "Depulso", "Locomotor", "Scourgify", "Reparo", "Aparecium", "Rictusempra", "Tarantallegra", "Sonorus", "Quietus"]
randomSpell = random.choice(atkSpells)
def spellCast():
    learntSpell = False
    print(f"El jugador castea {randomSpell}")
    for spell in hechizos_basicos:
        if spell == randomSpell:
            learntSpell = True
            return print("Hechizo casteado con éxito")
    if learntSpell == False:
        print("Aún no aprendiste ese hechizo")
spellCast()