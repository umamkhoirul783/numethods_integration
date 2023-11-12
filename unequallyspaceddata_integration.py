import math

def v(t, g, m, c):
    return (g * m / c) * (1 - math.exp(-(c / m) * t))

def trapezoidal_rule(x, y):
    n = len(x) - 1
    h = (x[n] - x[0]) / n
    integral_sum = y[0] + y[n]

    for i in range(1, n):
        integral_sum += 2 * y[i]

    result = (h / 2) * integral_sum
    return result

def simpsons_trapezoidal_combination(x, y):
    n = len(x) - 1
    h = (x[n] - x[0]) / n
    integral_sum = y[0] + y[n]

    for i in range(1, n):
        factor = 4 if i % 2 == 1 else 2
        integral_sum += factor * y[i]

    result = (h / 3) * integral_sum
    return result

# Konstanta
g_value = 9.8  # konstanta gravitasi (m/s^2)
m_value = 68.1  # massa penerjun payung (kg)
c_value = 12.5  # koefisien drag (kg/s)

# Menghasilkan data yang tidak teratur (misalnya, t dan v)
# Untuk tujuan ilustrasi, kita menggunakan data yang sederhana
t_data = [0, 0.5, 1.0]
v_data = [v(t, g_value, m_value, c_value) for t in t_data]

# Menggunakan aturan trapezoidal untuk mengintegrasikan data yang tidak teratur
integral_trapezoidal = trapezoidal_rule(t_data, v_data)
print("Hasil Integral menggunakan Trapezoidal Rule:", integral_trapezoidal)

# Menggunakan kombinasi simpson dengan trapezoidal rule untuk mengintegrasikan data yang tidak teratur
integral_simpsons_trapezoidal_combination = simpsons_trapezoidal_combination(t_data, v_data)
print("Hasil Integral menggunakan Simpson's Combination:", integral_simpsons_trapezoidal_combination)
