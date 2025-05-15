import numpy as np

def tampilkan_matriks(A):
    """
    Fungsi untuk menampilkan matriks ke layar.
    """
    for baris in A:
        print(" ".join(f"{elemen:8.3f}" for elemen in baris))
    print()

def lu_decomposition(A):
    """
    Fungsi untuk melakukan dekomposisi LU pada matriks A.

    Parameter:
    - A: Matriks koefisien (numpy.ndarray)

    Return:
    - L: Matriks segitiga bawah
    - U: Matriks segitiga atas
    """
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        
        for j in range(i, n):
            if i == j:
                L[i][i] = 1  # Diagonal utama L adalah 1
            else:
                L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U

def forward_substitution(L, b):
    """
    Fungsi untuk menyelesaikan Ly = b (substitusi maju).

    Parameter:
    - L: Matriks segitiga bawah
    - b: Vektor konstanta

    Return:
    - y: Vektor hasil substitusi maju
    """
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
    return y

def backward_substitution(U, y):
    """
    Fungsi untuk menyelesaikan Ux = y (substitusi mundur).

    Parameter:
    - U: Matriks segitiga atas
    - y: Vektor hasil substitusi maju

    Return:
    - x: Vektor solusi
    """
    n = len(y)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]
    return x

def main():
    print("Sistem Persamaan Linear - Metode Dekomposisi LU")
    print("==============================================")
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

    print("Melakukan dekomposisi LU...")
    L, U = lu_decomposition(A)

    print("Matriks L (Segitiga Bawah):")
    tampilkan_matriks(L)
    print("Matriks U (Segitiga Atas):")
    tampilkan_matriks(U)

    print("Melakukan substitusi maju untuk menyelesaikan Ly = b...")
    y = forward_substitution(L, b)
    print("Vektor y:")
    print(y, "\n")

    print("Melakukan substitusi mundur untuk menyelesaikan Ux = y...")
    x = backward_substitution(U, y)
    print("Vektor x (solusi):")
    for i in range(n):
        print(f"x[{i+1}] = {x[i]:.3f}")

if __name__ == "__main__":
    main()