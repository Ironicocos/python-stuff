import array
learntSpells = ["Lumos", "Nox", "Alohomora", "Colloportus", "Wingardium Leviosa", "Accio", "Depulso", "Locomotor", "Scourgify"]
points = 450
score = array.array('i', [70, 85, 60, 90, 75])
estudiantes = {
    "learntSpells": learntSpells,
    "points": points,
    "exams": score
}
for i, j in estudiantes.items():
    print(estudiantes.get("exams"))