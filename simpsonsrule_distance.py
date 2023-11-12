import math

def v(t, g, m, c):
    return (g * m / c) * (1 - math.exp(-(c / m) * t))

def simpsons_one_third_single(t0, t1, n, g, m, c):
    h = (t1 - t0) / n
    integral_sum = v(t0, g, m, c) + v(t1, g, m, c)

    for i in range(1, n):
        t_i = t0 + i * h
        factor = 4 if i % 2 == 1 else 2
        integral_sum += factor * v(t_i, g, m, c)

    result = h * integral_sum / 3
    return result

def simpsons_three_eighth_single(t0, t1, n, g, m, c):
    h = (t1 - t0) / n
    integral_sum = v(t0, g, m, c) + v(t1, g, m, c)

    for i in range(1, n):
        t_i = t0 + i * h
        factor = 3 if i % 3 == 0 else 2
        integral_sum += factor * v(t_i, g, m, c)

    result = 3 * h * integral_sum / 8
    return result

def simpsons_one_third_multiple_odd(t0, t1, n, g, m, c):
    h = (t1 - t0) / n
    integral_sum = v(t0, g, m, c) + v(t1, g, m, c)

    for i in range(1, n):
        t_i = t0 + i * h
        factor = 4 if i % 2 == 1 else 2
        integral_sum += factor * v(t_i, g, m, c)

    result = h * integral_sum / 3
    return result

def simpsons_one_third_multiple_even(t0, t1, n, g, m, c):
    h = (t1 - t0) / n
    integral_sum = v(t0, g, m, c) + v(t1, g, m, c)

    for i in range(1, n):
        t_i = t0 + i * h
        factor = 4 if i % 2 == 0 else 2
        integral_sum += factor * v(t_i, g, m, c)

    result = h * integral_sum / 3
    return result

# Konstanta
g_value = 9.8  # konstanta gravitasi (m/s^2)
m_value = 68.1  # massa penerjun payung (kg)
c_value = 12.5  # koefisien drag (kg/s)

# Contoh penggunaan aturan Simpson's 1/3 dan 3/8 untuk single-application
t0_single = 0
t1_single = 1
n_single = 1000  # jumlah segmen

hasil_simpsons_one_third_single = simpsons_one_third_single(t0_single, t1_single, n_single, g_value, m_value, c_value)
hasil_simpsons_three_eighth_single = simpsons_three_eighth_single(t0_single, t1_single, n_single, g_value, m_value, c_value)

print("Hasil Integral menggunakan Simpson's 1/3 (Single):", hasil_simpsons_one_third_single)
print("Hasil Integral menggunakan Simpson's 3/8 (Single):", hasil_simpsons_three_eighth_single)

# Contoh penggunaan aturan Simpson's 1/3 untuk multiple-application (jumlah segmen ganjil)
t0_multiple_odd = 0
t1_multiple_odd = 1
n_multiple_odd = 1001  # jumlah segmen ganjil

hasil_simpsons_one_third_multiple_odd = simpsons_one_third_multiple_odd(t0_multiple_odd, t1_multiple_odd, n_multiple_odd, g_value, m_value, c_value)
print("Hasil Integral menggunakan Simpson's 1/3 (Multiple - Ganjil):", hasil_simpsons_one_third_multiple_odd)

# Contoh penggunaan aturan Simpson's 1/3 untuk multiple-application (jumlah segmen genap)
t0_multiple_even = 0
t1_multiple_even = 1
n_multiple_even = 1000  # jumlah segmen genap

hasil_simpsons_one_third_multiple_even = simpsons_one_third_multiple_even(t0_multiple_even, t1_multiple_even, n_multiple_even, g_value, m_value, c_value)
print("Hasil Integral menggunakan Simpson's 1/3 (Multiple - Genap):", hasil_simpsons_one_third_multiple_even)
