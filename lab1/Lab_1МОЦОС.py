import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate as integrate

# Межі
li = -np.pi
lf = np.pi
# Порядок ряду Фур'є
n = 4  # Ваш номер студента (парний)

# Визначення функції
def f(x):
    """Обчислює значення функції f(x) = x^n * exp(-x^2/n)."""
    return x**n * np.exp(-x**2/n)

# Підпрограма для обчислення значення функції
def compute_function_values(x):
    """Обчислює значення функції f(x) для масиву x."""
    return f(x)

# Підпрограма для обчислення коефіцієнтів Фур'є
def calculate_fourier_coefficients(li, lf, n):
    """Обчислює коефіцієнти Фур'є a_k для функції f(x)."""
    l = (lf - li) / 2  # піддовжина інтервалу
    a0 = (2.0 / l) * (integrate.quad(lambda x: f(x), 0, l))[0]  # нульовий коефіцієнт
    an = [a0 / 2.0]  # список коефіцієнтів a_n
    
    for i in range(1, n + 1):
        an_i = (2.0 / l) * (integrate.quad(lambda x: f(x) * np.cos(i * np.pi * x / l), 0, l))[0]
        an.append(an_i)
        
    return an

# Підпрограма для обчислення наближення
def approximate_function(x, an, n):
    """Обчислює наближене значення функції за рядом Фур'є."""
    fx = an[0]  # починаємо з a0
    for i in range(1, n + 1):
        fx += an[i] * np.cos((i * x * np.pi) / ((lf - li) / 2))
    return fx

# Підпрограма для обчислення відносної похибки
def compute_relative_error(y_exact, y_approx):
    """Обчислює відносну похибку між точними та наближеними значеннями."""
    error = []
    for exact, approx in zip(y_exact, y_approx):
        if exact != 0:  # уникаємо ділення на нуль
            error.append((approx - exact) / exact)
    return np.abs(error)

# Підпрограма для побудови графіка гармонік
def plot_harmonics(an):
    """Побудова графіка гармонік a_k."""
    k_n = np.arange(len(an))  # Масив частот k
    plt.stem(k_n, an)  # Відображення гармонік
    plt.title('Графік гармонік a_k')
    plt.xlabel('k')
    plt.ylabel('a_k')
    plt.grid()
    plt.show()

# Головна програма
def main():
    # Генерація значень x
    x = np.arange(li, lf, 0.05)
    y_exact = compute_function_values(x)  # точні значення функції

    # Обчислення коефіцієнтів Фур'є
    an = calculate_fourier_coefficients(li, lf, n)

    # Вивід коефіцієнтів
    print("Коефіцієнти Фур'є a_n:")
    for i, coef in enumerate(an):
        print(f"a_{i}: {coef:.5f}")

    # Обчислення наближених значень функції
    y_approx = [approximate_function(xi, an, n) for xi in x]

    # 1. Побудова графіка точного значення функції на інтервалі
    plt.figure(figsize=(12, 6))
    plt.plot(x, y_exact, label='Точне значення функції', color='blue')
    plt.title('Графік функції f(x) на інтервалі [-π, π]')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.xlim([li, lf])
    plt.ylim([min(y_exact)-5, max(y_exact)+5])
    plt.show()

    # 2. Побудова графіка точних та наближених значень функції
    plt.figure(figsize=(12, 6))
    plt.plot(x, y_exact, label='Точне значення функції', color='blue')
    plt.plot(x, y_approx, label='Наближене значення розкладу Фур\'є', color='red', linestyle='--')
    plt.legend()
    plt.title('Порівняння точних та наближених значень функції')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.xlim([li, lf])
    plt.ylim([min(y_exact)-5, max(y_exact)+5])
    plt.show()

    # 3. Побудова графіка на менших координатах
    plt.figure(figsize=(12, 6))
    plt.plot(x, y_exact, label='Точне значення функції', color='blue')
    plt.plot(x, y_approx, label='Наближене значення розкладу Фур\'є', color='red', linestyle='--')
    plt.legend()
    plt.title('Порівняння точних та наближених значень функції на малих координатах')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.xlim([0, 1])  # Обмеження осі x від 0 до 1
    plt.ylim([min(y_exact)-5, max(y_exact)+5])
    plt.grid()
    plt.show()

    # 4. Обчислення відносної похибки
    relative_error = compute_relative_error(y_exact, y_approx)

    # Графік відносної похибки
    plt.figure(figsize=(12, 6))
    plt.plot(x, relative_error, color='orange')
    plt.title('Відносна похибка наближення')
    plt.xlabel('x')
    plt.ylabel('Відносна похибка')
    plt.xlim([li, lf])
    plt.grid()
    plt.show()

    # Виклик функції для побудови графіка гармонік у головній програмі
    plot_harmonics(an)

    # Обчислення ряду Фур'є в конкретній точці x = π/2
    x_point = math.pi / 2
    fx = approximate_function(x_point, an, n)  # наближене значення функції
    print(f'Наближення рядом Фур\'є з точністю до порядку {n} в точцi x = {x_point} дорівнює {fx}')

    # Запис результатів у файл
    with open('output1.txt', 'w') as file:
        file.write("Порядок: " + str(n) + "\n")
        file.write("Обчислені коефіцієнти a_n: " + str(an) + "\n")
        file.write("Обчислені похибки відхилень: " + str(relative_error) + "\n")
        file.write(f"Наближення рядом Фур'є з точністю до порядку 4 в точці x = {x_point} дорівнює {fx}\n")

if __name__ == "__main__":
    main()
