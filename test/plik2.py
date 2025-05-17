import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Tworzenie obszaru rysowania
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)  # Przedział dla osi x
line, = ax.plot(x, np.sin(x))  # Inicjalny wykres sinus

# Ustawienia osi
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)

# Funkcja aktualizująca wykres w każdej klatce animacji
def update(frame):
    line.set_ydata(np.sin(x + frame / 10))  # Przesuwanie sinusoidy w osi x
    return line,

# Tworzenie animacji (interwał w milisekundach)
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

# Wyświetlanie animacji
plt.show()
