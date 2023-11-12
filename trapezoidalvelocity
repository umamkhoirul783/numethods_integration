import math

def v(t):
    g = 9.8  # konstanta gravitasi (m/s^2)
    m = 68.1  # massa penerjun payung (kg)
    c = 12.5  # koefisien drag (kg/s)

    result = (g * m / c) * (1 - math.exp(-(c / m) * t))
    return result

def trap(h, f0, f1):
    result = h * (f0 + f1) / 2
    return result

def trapm(h, n, f):
    trap_sum = f[0]
    
    for i in range(1, n - 1):
        trap_sum += 2 * f[i]
    
    trap_sum += f[n - 1]
    
    result = h * trap_sum / 2
    return result

# Contoh penggunaan single trapezoidal
t0 = 0
t1 = 5
h_single = t1 - t0
v_t0 = v(t0)
v_t1 = v(t1)

hasil_single_trapezoidal = trap(h_single, v_t0, v_t1)
print("Hasil Single Trapezoidal:", hasil_single_trapezoidal)

# Contoh penggunaan multiple trapezoidal
n = 1000  # jumlah subinterval
h_multiple = (t1 - t0) / n
v_multiple_trap = [v(t0 + i * h_multiple) for i in range(n + 1)]

hasil_multiple_trapezoidal = trapm(h_multiple, n + 1, v_multiple_trap)
print("Hasil Multiple Trapezoidal:", hasil_multiple_trapezoidal)
