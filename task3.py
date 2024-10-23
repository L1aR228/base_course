import numpy as np

x0 = 0  
y0 = 0  
v0 = 20 
angle_deg = 45  # угол в градусах
angle_rad = np.radians(angle_deg)  # угол в радианах

# Вычисляем компоненты начальной скорости
v0x = v0 * np.cos(angle_rad)  # горизонтальная
v0y = v0 * np.sin(angle_rad)  # вертикальная

# Константы
g = 9.81  

# Время от 0 до 5 секунд
t_values = np.linspace(0, 5, 100)  # 100 точек времени

# Массивы для координат
x_values = x0 + v0x * t_values
y_values = y0 + v0y * t_values - 0.5 * g * (t_values ** 2)

results = np.column_stack((t_values, x_values, y_values))

print(f"t      (с)    \t       x (м)     \t      y (м)")
print(results) # хочу спать 

