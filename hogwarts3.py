import array
score = array.array('i', [70, 85, 60, 90, 75])
totalScore = 0
avrgScore = 0
passedExams = 0
examCounter = 0
for i in score:
    examCounter += 1
    totalScore = totalScore + i
    if i > 80:
        passedExams += 1
avrgScore = totalScore / examCounter
print(f"Promedio de calificaciones: {avrgScore}")
print(f"Puntaje total: {totalScore}")
print(f"Obtuvo más de 80 puntos {passedExams} veces")