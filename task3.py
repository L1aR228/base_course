import numpy as np

# Начальные параметры
x0 = 0  # начальная координата по x
y0 = 0  # начальная координата по y
v0 = 20  # начальная скорость (м/с)
angle_deg = 45  # угол в градусах
angle_rad = np.radians(angle_deg)  # угол в радианах

# Вычисляем компоненты начальной скорости
v0x = v0 * np.cos(angle_rad)  # горизонтальная компонента
v0y = v0 * np.sin(angle_rad)  # вертикальная компонента

# Константы
g = 9.81  # ускорение свободного падения (м/с²)

# Время от 0 до 5 секунд
t_values = np.linspace(0, 5, num=100)  # 100 точек времени

# Массивы для координат
x_values = x0 + v0x * t_values
y_values = y0 + v0y * t_values - 0.5 * g * (t_values ** 2)

# Сохраним результаты в массив
results = np.column_stack((t_values, x_values, y_values))

# Вывод результатов
print("t (с) \t x (м) \t y (м)")
print(results)