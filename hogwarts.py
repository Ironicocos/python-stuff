import random
hechizos_basicos = ["Lumos", "Alohomora", "Wingardium Leviosa"]
atkSpells = ["Lumos", "Nox", "Alohomora", "Colloportus", "Wingardium Leviosa", "Accio", "Depulso", "Locomotor", "Scourgify", "Reparo", "Aparecium", "Rictusempra", "Tarantallegra", "Sonorus", "Quietus"]
randomSpell = random.choice(atkSpells)
learntSpell = False
def spellCast(learntSpell):
    print(learntSpell)
    print(f"El jugador castea {randomSpell}")
    for spell in hechizos_basicos:
        if spell == randomSpell:
            print("Hechizo casteado con éxito")
            learntSpell = True 
            break
    if learntSpell == False:
            print("Aún no aprendiste ese hechizo")
    return learntSpell
learntSpell = spellCast(learntSpell)