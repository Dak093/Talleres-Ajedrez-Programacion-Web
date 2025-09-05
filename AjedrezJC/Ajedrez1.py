import random

# Pedir datos al usuario
n = int(input("Ingrese el tamaño del tablero: "))
r_fila, r_col = map(int, input("Posición de la reina (fila, columna): ").split())

# Generar bloqueo aleatorio
b_fila = random.randint(1, n)
b_col = random.randint(1, n)

# Lista para guardar movimientos
posibles = []

# Desplazamientos de la reina
dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]

# Calcular posiciones posibles
for d_f, d_c in dirs:
    x = r_fila + d_f
    y = r_col + d_c
    while 1 <= x <= n and 1 <= y <= n:
        if x == b_fila and y == b_col:
            break
        posibles.append((x, y))
        x += d_f
        y += d_c

# Dibujar tablero
for i in range(1, n + 1):
    fila = ""
    for j in range(1, n + 1):
        if i == r_fila and j == r_col:
            fila += " R "
        elif i == b_fila and j == b_col:
            fila += " X "
        elif (i, j) in posibles:
            fila += " * "
        else:
            fila += " . "
    print(fila)

# Mostrar resultados
print("\nCantidad de movimientos:", len(posibles))
print("Casilla bloqueada:", b_fila, b_col)
