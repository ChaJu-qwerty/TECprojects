# es este coso vamos a graficar tiro parabolico
#la validacion es "subjetiva", ya que la velocidad negrativa se puede tomar como retroceso
#y el angulo negativo tambien es valido

import matplotlib.pyplot as plt
import math

# Datos iniciales / de entrada
angulo_grados = int(input("introduce el angulo: "))  # Ángulo en grados
velocidad_inicial = int(input("introduce la velocidad: "))  # Velocidad inicial en m/s

# Convertimos el ángulo a radianes
angulo_radianes = math.radians(angulo_grados)

# Componentes de la velocidad inicial
v0x = velocidad_inicial * math.cos(angulo_radianes)
v0y = velocidad_inicial * math.sin(angulo_radianes)

# Parámetros
g = 9.8  # gravedad en m/s^2
t_max = 2 * v0y / g  # Tiempo total de vuelo

# Intervalo de tiempo
t_intervalo = 0.01
t = 0 #tiempo inicial
tiempos = [t]
posiciones_x = [0]
posiciones_y = [0]

# Calculamos las posiciones en cada instante de tiempo
while t <= t_max:
    t += t_intervalo
    tiempos.append(t)
    x = v0x * t
    y = v0y * t - 0.5 * g * t**2
    posiciones_x.append(x)
    posiciones_y.append(y)

# Graficamos la trayectoria
plt.plot(posiciones_x, posiciones_y)
plt.title("Tiro Parabólico")
plt.xlabel("Posición en X (metros)")
plt.ylabel("Posición en Y (metros)")
plt.show()