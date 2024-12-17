import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

square = np.array([[-0.5, -0.5],
                   [0.5, -0.5],
                   [0.5, 0.5],
                   [-0.5, 0.5],
                   [-0.5, -0.5]])

line, = ax.plot([], [], color='blue')


def update(frame):
    angle = np.radians(frame)  # Перевод угла в радианы, без этого будет полная диц
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)

    rotation_matrix = np.array([[cos_a, -sin_a],
                                [sin_a, cos_a]])

    rotated_square = square @ rotation_matrix
    # rotated_square = np.dot(square, rotation_matrix) матричное умножение
    line.set_data(rotated_square[:, 0], rotated_square[:, 1])
    return line,


ani = FuncAnimation(fig, update, frames=100, interval=50)
ani.save('dop_task_5.gif', writer="pillow")