alumnos = {
 "Harry": 80,
 "Hermione": 95,
 "Ron": 60
}
for i, j in alumnos.items():
    print(f"{j}")
    if j > 90:
        print("Excelente")
    elif j > 70 and j < 90:
        print("Muy bien")
    else:
        print("Debe practicar más")