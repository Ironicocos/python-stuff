jugadores = {
 "Mario": {"vidas": 3, "puntos": 120},
 "Luigi": {"vidas": 2, "puntos": 150},
 "Peach": {"vidas": 4, "puntos": 90}
}
for i, j in jugadores.items():
    j.update({"puntos": (j.get("puntos") + 50)})
    if j.get("vidas") < 3:
        j.update({"vidas": (j.get("vidas") + 1)})
        print(f"Actualizado con éxito: {j}")
print(jugadores)