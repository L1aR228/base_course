import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

point = 100

t = np.arange(0, 10, 0.01)

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
plt.grid()

line1, = ax.plot([], [], color='blue')
line2, = ax.plot([], [], color='orange')

trail1, = ax.plot([], [], color='blue', alpha=0.5) 
trail2, = ax.plot([], [], color='orange', alpha=0.5)

history_x = []  # Все x координаты
history_y1 = []  # Все y1 координаты
history_y2 = []  # Все y2 координаты


def animate(i, t_values):
    t_current = t_values[:i + 1]

    y1 = 1 * np.sin(1 * t_current)
    y2 = 0.5 * np.sin(2 * t_current)

    line1.set_data(t_current, y1)
    line2.set_data(t_current, y2)

    # Сохраняем текущие координаты
    history_x.extend(t_current)
    history_y1.extend(y1)
    history_y2.extend(y2)

    # Обновляем линии траекторий
    trail1.set_data(history_x, history_y1)
    trail2.set_data(history_x, history_y2)

    return line1, line2, trail1, trail2


ani = FuncAnimation(fig, animate, frames=1000, fargs=(t,), interval=20)
plt.show() # строго через пайчарм