import numpy as np
import matplotlib.pyplot as plt

# Задаем данные для аппроксимации
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Выполняем аппроксимацию с полиномом степени 1 (линейная аппроксимация)
coefficients = np.polyfit(x, y, 1)
poly = np.poly1d(coefficients)

# Рисуем график и аппроксимацию
plt.plot(x, y, 'o', label='Исходные данные')
plt.plot(x, poly(x), label='Аппроксимация')
plt.legend()
plt.show()

