import math

def f(x):
    # Contoh fungsi: x^2 - 4*x - 5 dengan interval [-2,1]
    return x*2 - 4*x - 5

# 1.1. Metode Pias (Kaidah Segiempat)
def pias_segiempat(a, b, n):
    h = (b - a) / n
    print(f"\nLangkah-langkah Metode Pias (Kaidah Segiempat):")
    print(f"h = (b - a) / n = ({b} - {a}) / {n} = {h}")
    total = 0
    for i in range(n):
        xi = a + i * h
        fx = f(xi)
        print(f"f(x{i}) = f({xi}) = {fx}")
        total += fx
    hasil = h * total
    print(f"Integral ≈ h * jumlah f(xi) = {h} * {total} = {hasil}")
    return hasil

# 1.2. Metode Pias (Kaidah Trapesium)
def pias_trapesium(a, b, n):
    h = (b - a) / n
    print(f"\nLangkah-langkah Metode Pias (Kaidah Trapesium):")
    print(f"h = (b - a) / n = ({b} - {a}) / {n} = {h}")
    total = f(a) + f(b)
    print(f"f(a) = f({a}) = {f(a)}")
    print(f"f(b) = f({b}) = {f(b)}")
    for i in range(1, n):
        xi = a + i * h
        fx = f(xi)
        print(f"f(x{i}) = f({xi}) = {fx}")
        total += 2 * fx
    print(f"Jumlah total = f(a) + f(b) + 2 * jumlah f(xi) tengah")
    hasil = (h / 2) * total
    print(f"Integral ≈ (h/2) * total = ({h}/2) * {total} = {hasil}")
    return hasil

# 1.3. Metode Pias (Kaidah Titik Tengah)
def pias_titik_tengah(a, b, n):
    h = (b - a) / n
    print(f"\nLangkah-langkah Metode Pias (Kaidah Titik Tengah):")
    print(f"h = (b - a) / n = ({b} - {a}) / {n} = {h}")
    total = 0
    for i in range(n):
        xi = a + (i + 0.5) * h
        fx = f(xi)
        print(f"f(x_tengah{i}) = f({xi}) = {fx}")
        total += fx
    hasil = h * total
    print(f"Integral ≈ h * jumlah f(x_tengah) = {h} * {total} = {hasil}")
    return hasil

# kaidah newton cotes trapesium
def pias_trapesium(a, b, n):
    h = (b - a) / n
    print(f"\nLangkah-langkah Metode Newton-Cotes(Kaidah Trapesium):")
    print(f"h = (b - a) / n = ({b} - {a}) / {n} = {h}")
    total = f(a) + f(b)
    print(f"f(a) = f({a}) = {f(a)}")
    print(f"f(b) = f({b}) = {f(b)}")
    for i in range(1, n):
        xi = a + i * h
        fx = f(xi)
        print(f"f(x{i}) = f({xi}) = {fx}")
        total += 2 * fx
    print(f"Jumlah total = f(a) + f(b) + 2 * jumlah f(xi) tengah")
    hasil = (h / 2) * total
    print(f"Integral ≈ (h/2) * total = ({h}/2) * {total} = {hasil}")
    return hasil

# 2. Newton-Cotes (Simpson 1/3)
def simpson13(a, b, n):
    if n % 2 != 0:
        raise ValueError('n harus genap untuk Simpson 1/3')
    h = (b - a) / n
    print(f"\nLangkah-langkah Metode Simpson 1/3:")
    print(f"h = (b - a) / n = ({b} - {a}) / {n} = {h}")
    total = f(a) + f(b)
    print(f"f(a) = f({a}) = {f(a)}")
    print(f"f(b) = f({b}) = {f(b)}")
    for i in range(1, n):
        x = a + i * h
        fx = f(x)
        if i % 2 == 0:
            print(f"2 * f(x{i}) = 2 * f({x}) = {2*fx}")
            total += 2 * fx
        else:
            print(f"4 * f(x{i}) = 4 * f({x}) = {4*fx}")
            total += 4 * fx
    hasil = (h / 3) * total
    print(f"Integral ≈ (h/3) * total = ({h}/3) * {total} = {hasil}")
    return hasil

# 3. Newton-Cotes (Simpson 3/8)
def simpson38(a, b, n):
    if n % 3 != 0:
        raise ValueError('n harus kelipatan 3 untuk Simpson 3/8')
    h = (b - a) / n
    print(f"\nLangkah-langkah Metode Simpson 3/8:")
    print(f"h = (b - a) / n = ({b} - {a}) / {n} = {h}")
    total = f(a) + f(b)
    print(f"f(a) = f({a}) = {f(a)}")
    print(f"f(b) = f({b}) = {f(b)}")
    for i in range(1, n):
        x = a + i * h
        fx = f(x)
        if i % 3 == 0:
            print(f"2 * f(x{i}) = 2 * f({x}) = {2*fx}")
            total += 2 * fx
        else:
            print(f"3 * f(x{i}) = 3 * f({x}) = {3*fx}")
            total += 3 * fx
    hasil = (3 * h / 8) * total
    print(f"Integral ≈ (3h/8) * total = (3*{h}/8) * {total} = {hasil}")
    return hasil

if __name__ == "__main__":
    while True:
        print("\nProgram Integral Numerik")
        print("Fungsi contoh: x^2 - 4*x - 5")
        print("1. Metode Pias (Kaidah Segiempat)")
        print("2. Metode Pias (Kaidah Trapesium)")
        print("3. Metode Pias (Kaidah Titik Tengah)")
        print("4. Newton-Cotes (Kaidah Trapesium)")
        print("5. Newton-Cotes (Simpson 1/3)")
        print("6. Newton-Cotes (Simpson 3/8)")
        print("7. Keluar")
        metode = input("Pilih metode: ")
        if metode == '1':
            a = float(input("Masukkan batas bawah (a): "))
            b = float(input("Masukkan batas atas (b): "))
            n = int(input("Masukkan jumlah pias (n): "))
            hasil = pias_segiempat(a, b, n)
            print(f"\nHasil integral (Pias Segiempat): {hasil}")
        elif metode == '2':
            a = float(input("Masukkan batas bawah (a): "))
            b = float(input("Masukkan batas atas (b): "))
            n = int(input("Masukkan jumlah pias (n): "))
            hasil = pias_trapesium(a, b, n)
            print(f"\nHasil integral (Pias Trapesium): {hasil}")
        elif metode == '3':
            a = float(input("Masukkan batas bawah (a): "))
            b = float(input("Masukkan batas atas (b): "))
            n = int(input("Masukkan jumlah pias (n): "))
            hasil = pias_titik_tengah(a, b, n)
            print(f"\nHasil integral (Pias Titik Tengah): {hasil}")
        elif metode == '4': 
            a = float(input("Masukkan batas bawah (a): "))
            b = float(input("Masukkan batas atas (b): "))
            n = int(input("Masukkan jumlah pias (n): "))
            hasil = pias_trapesium(a, b, n)
            print(f"\nHasil integral (Newton-Cotes Trapesium): {hasil}")
        elif metode == '5':
            a = float(input("Masukkan batas bawah (a): "))
            b = float(input("Masukkan batas atas (b): "))
            n = int(input("Masukkan jumlah pias genap (n): "))
            hasil = simpson13(a, b, n)
            print(f"\nHasil integral (Simpson 1/3): {hasil}")
        elif metode == '6':
            a = float(input("Masukkan batas bawah (a): "))
            b = float(input("Masukkan batas atas (b): "))
            n = int(input("Masukkan jumlah pias kelipatan 3 (n): "))
            hasil = simpson38(a, b, n)
            print(f"\nHasil integral (Simpson 3/8): {hasil}")
        elif metode == '7':
            print("Terima kasih telah menggunakan program integral numerik!")
            break
        else:
            print("Pilihan tidak valid.")
