import numpy as np

def tampilkan_matriks(A):
    """
    Fungsi untuk menampilkan matriks ke layar.
    """
    for baris in A:
        print(" ".join(f"{elemen:8.3f}" for elemen in baris))
    print()

def solusi_matriks_balikan(A, b):
    """
    Fungsi untuk menyelesaikan sistem persamaan linear Ax = b
    menggunakan metode matriks balikan.

    Parameter:
    - A: Matriks koefisien (numpy.ndarray)
    - b: Vektor konstanta (numpy.ndarray)

    Return:
    - x: Solusi sistem persamaan linear
    """
    print("Langkah 1: Periksa apakah matriks A memiliki invers.")
    det_A = np.linalg.det(A)
    print(f"Determinan matriks A = {det_A:.3f}")
    if det_A == 0:
        raise ValueError("Matriks A tidak memiliki invers (determinan = 0). Sistem tidak dapat diselesaikan.")

    print("\nLangkah 2: Hitung matriks invers dari A.")
    A_inv = np.linalg.inv(A)
    print("Matriks invers A:")
    tampilkan_matriks(A_inv)

    print("Langkah 3: Hitung solusi x = A^(-1) * b.")
    x = np.dot(A_inv, b)
    return x

def main():
    print("Sistem Persamaan Linear - Metode Matriks Balikan")
    print("===============================================")
    n = int(input("Masukkan jumlah persamaan: "))

    print("\nMasukkan elemen matriks A:")
    A = []
    for i in range(n):
        baris = list(map(float, input(f"Baris {i+1}: ").split()))
        A.append(baris)
    A = np.array(A)

    print("\nMasukkan elemen vektor b:")
    b = []
    for i in range(n):
        nilai = float(input(f"b[{i+1}]: "))
        b.append(nilai)
    b = np.array(b)

    print("\nMatriks A yang dimasukkan:")
    tampilkan_matriks(A)

    print("Vektor b yang dimasukkan:")
    print(b, "\n")

    try:
        solusi = solusi_matriks_balikan(A, b)
        print("\nSolusi sistem persamaan linear:")
        for i in range(n):
            print(f"x[{i+1}] = {solusi[i]:.3f}")
    except ValueError as e:
        print("\nError:", e)

if __name__ == "__main__":
    main()