notas_estudiantes = {
    'Juan': [3.2, 4.5, 5],
    'Maria': [4.2, 3.5, 4.3],
    'Pedro': [3.9, 2.5, 4.8]
}

dicc = {}

for nombre, nota in notas_estudiantes.items():
    suma = 0
    for no in nota:
        suma = suma + no
        prom = suma / len(nota)
        dicc[nombre] = prom

print(dicc)
