import math

def f(x):
    # Contoh fungsi: x^2 - 4*x - 5
    return x*2 - 4*x - 5

def df(x):
    return 2*x - 4

# Metode Bagi Dua 
def bisection(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Metode bagi dua tidak dapat dijalankan: f(a) dan f(b) harus berlainan tanda.")
        return None
    print(f"{'Iter':<5}{'a':<12}{'b':<12}{'c':<12}{'f(c)':<12}{'Error':<12}")
    c_old = a
    for i in range(1, max_iter+1):
        c = (a + b) / 2
        fc = f(c)
        error = abs(c - c_old)
        print(f"{i:<5}{a:<12.6f}{b:<12.6f}{c:<12.6f}{fc:<12.6f}{error:<12.6f}")
        if abs(fc) < tol or error < tol:
            print(f"\nAkar ditemukan pada x = {c:.6f} setelah {i} iterasi.")
            return c
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        c_old = c
    print(f"\nAkar tidak ditemukan dalam {max_iter} iterasi.")
    return None

# Metode Regula-Falsi
def regula_falsi(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Metode regula-falsi tidak dapat dijalankan: f(a) dan f(b) harus berlainan tanda.")
        return None
    print(f"{'Iter':<5}{'a':<12}{'b':<12}{'c':<12}{'f(c)':<12}{'Error':<12}")
    c_old = a
    for i in range(1, max_iter+1):
        fa = f(a)
        fb = f(b)
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)
        error = abs(c - c_old)
        print(f"{i:<5}{a:<12.6f}{b:<12.6f}{c:<12.6f}{fc:<12.6f}{error:<12.6f}")
        if abs(fc) < tol or error < tol:
            print(f"\nAkar ditemukan pada x = {c:.6f} setelah {i} iterasi.")
            return c
        if fa * fc < 0:
            b = c
        else:
            a = c
        c_old = c
    print(f"\nAkar tidak ditemukan dalam {max_iter} iterasi.")
    return None

# Metode Newton-Raphson
def newton_raphson(x0, tol, max_iter):
    print(f"{'Iter':<5}{'x':<15}{'f(x)':<15}{'Error':<15}")
    for i in range(1, max_iter+1):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Turunan sama dengan nol. Metode gagal.")
            return None
        x1 = x0 - fx/dfx
        error = abs(x1 - x0)
        print(f"{i:<5}{x1:<15.8f}{f(x1):<15.8f}{error:<15.8f}")
        if abs(f(x1)) < tol or error < tol:
            print(f"\nAkar ditemukan pada x = {x1:.8f} setelah {i} iterasi.")
            return x1
        x0 = x1
    print(f"\nAkar tidak ditemukan dalam {max_iter} iterasi.")
    return None

# Metode Secant
def secant(x0, x1, tol, max_iter):
    print(f"{'Iter':<5}{'x0':<15}{'x1':<15}{'x2':<15}{'f(x2)':<15}{'Error':<15}")
    for i in range(1, max_iter+1):
        f0 = f(x0)
        f1 = f(x1)
        if f1 - f0 == 0:
            print("Terjadi pembagian dengan nol. Metode gagal.")
            return None
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        error = abs(x2 - x1)
        print(f"{i:<5}{x0:<15.8f}{x1:<15.8f}{x2:<15.8f}{f(x2):<15.8f}{error:<15.8f}")
        if abs(f(x2)) < tol or error < tol:
            print(f"\nAkar ditemukan pada x = {x2:.8f} setelah {i} iterasi.")
            return x2
        x0, x1 = x1, x2
    print(f"\nAkar tidak ditemukan dalam {max_iter} iterasi.")
    return None

# Metode Leltaran Titik Tetap
def g(x):
    # Contoh: x = (x**3 + 1)/4 (dari x^3 - 4x + 1 = 0)
    return (x**3 + 1) / 4

def fixed_point_iteration(x0, tol, max_iter):
    print(f"{'Iter':<5}{'x':<15}{'g(x)':<15}{'Error':<15}")
    for i in range(1, max_iter+1):
        x1 = g(x0)
        error = abs(x1 - x0)
        print(f"{i:<5}{x1:<15.8f}{g(x1):<15.8f}{error:<15.8f}")
        if error < tol:
            print(f"\nAkar ditemukan pada x = {x1:.8f} setelah {i} iterasi.")
            return x1
        x0 = x1
    print(f"\nAkar tidak ditemukan dalam {max_iter} iterasi.")
    return None

if __name__ == "__main__":
    while True:
        print("\nPilih Metode Solusi Persamaan Nirlanjar yang Ingin Digunakan Ya!:")
        print("1. Metode Bagi Dua")
        print("2. Metode Regula-Falsi")
        print("3. Metode Newton-Raphson")
        print("4. Metode Secant")
        print("5. Metode Lelaran Titik Tetap")
        print("6. Keluar")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == '1':
            print("\nMetode Bagi Dua")
            a = float(input("Masukkan batas bawah (a): "))
            b = float(input("Masukkan batas atas (b): "))
            tol = float(input("Masukkan toleransi error: "))
            max_iter = int(input("Masukkan jumlah iterasi maksimum: "))
            bisection(a, b, tol, max_iter)
        elif pilihan == '2':
            print("\nMetode Regula-Falsi")
            a = float(input("Masukkan batas bawah (a): "))
            b = float(input("Masukkan batas atas (b): "))
            tol = float(input("Masukkan toleransi error: "))
            max_iter = int(input("Masukkan jumlah iterasi maksimum: "))
            regula_falsi(a, b, tol, max_iter)
        elif pilihan == '3':
            print("\nMetode Newton-Raphson")
            x0 = float(input("Masukkan tebakan awal (x0): "))
            tol = float(input("Masukkan toleransi error: "))
            max_iter = int(input("Masukkan jumlah iterasi maksimum: "))
            newton_raphson(x0, tol, max_iter)
        elif pilihan == '4':
            print("\nMetode Secant")
            x0 = float(input("Masukkan tebakan awal pertama (x0): "))
            x1 = float(input("Masukkan tebakan awal kedua (x1): "))
            tol = float(input("Masukkan toleransi error: "))
            max_iter = int(input("Masukkan jumlah iterasi maksimum: "))
            secant(x0, x1, tol, max_iter)
        elif pilihan == '5':
            print("\nMetode Lelaran Titik Tetap")
            x0 = float(input("Masukkan tebakan awal (x0): "))
            tol = float(input("Masukkan toleransi error: "))
            max_iter = int(input("Masukkan jumlah iterasi maksimum: "))
            fixed_point_iteration(x0, tol, max_iter)
        elif pilihan == '6':
            print("Terima kasih ya telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid.")
