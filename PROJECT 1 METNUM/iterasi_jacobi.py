import numpy as np

def tampilkan_vektor(v, nama="v"):
    """
    Fungsi untuk menampilkan vektor ke layar.
    """
    print(f"Vektor {nama}:")
    for i, nilai in enumerate(v):
        print(f"{nama}[{i+1}] = {nilai:.6f}")
    print()

def jacobi_iteration(A, b, x0, tol=1e-6, max_iter=100):
    """
    Fungsi untuk menyelesaikan sistem persamaan linear Ax = b
    menggunakan metode iterasi Jacobi.

    Parameter:
    - A: Matriks koefisien (numpy.ndarray)
    - b: Vektor konstanta (numpy.ndarray)
    - x0: Tebakan awal solusi (numpy.ndarray)
    - tol: Toleransi error (float)
    - max_iter: Iterasi maksimum (int)

    Return:
    - x: Solusi sistem persamaan linear (numpy.ndarray)
    - langkah: Jumlah iterasi yang dilakukan
    """
    n = len(b)
    x = x0.copy()
    iterasi = 0

    print("Langkah-langkah Iterasi Jacobi:")
    while iterasi < max_iter:
        x_new = np.zeros_like(x)
        print(f"Iterasi {iterasi + 1}:")
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        tampilkan_vektor(x_new, nama=f"x_iterasi_{iterasi+1}")

        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print("Solusi telah konvergen.")
            return x_new, iterasi + 1

        x = x_new
        iterasi += 1

    print("Iterasi maksimum tercapai, solusi mendekati:")
    return x, iterasi

def main():
    print("Sistem Persamaan Linear - Metode Iterasi Jacobi")
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

    print("\nMasukkan tebakan awal solusi (x0):")
    x0 = []
    for i in range(n):
        nilai = float(input(f"x0[{i+1}]: "))
        x0.append(nilai)
    x0 = np.array(x0)

    print("\nMatriks A yang dimasukkan:")
    for baris in A:
        print(" ".join(f"{elemen:8.3f}" for elemen in baris))
    print("\nVektor b yang dimasukkan:")
    tampilkan_vektor(b, nama="b")
    print("Tebakan awal solusi (x0):")
    tampilkan_vektor(x0, nama="x0")

    tol = float(input("\nMasukkan toleransi error (default: 1e-6): ") or 1e-6)
    max_iter = int(input("Masukkan jumlah iterasi maksimum (default: 100): ") or 100)

    solusi, langkah = jacobi_iteration(A, b, x0, tol=tol, max_iter=max_iter)
    
    print("\nSolusi sistem persamaan linear:")
    tampilkan_vektor(solusi, nama="x")
    print(f"Jumlah iterasi yang dilakukan: {langkah}")

if __name__ == "__main__":
    main()