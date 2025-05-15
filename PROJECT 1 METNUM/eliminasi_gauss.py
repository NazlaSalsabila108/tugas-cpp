def tampilkan_matriks(A, b):
    n = len(b)
    for i in range(n):
        baris = ""
        for j in range(len(A[i])):
            baris += f"{A[i][j]:8.3f} "
        baris += f"| {b[i]:8.3f}"
        print(baris)
    print()


def eliminasi_gauss(A, b):
    """
    Fungsi untuk menyelesaikan sistem persamaan linear Ax = b
    menggunakan metode Eliminasi Gauss.

    Parameter:
    - A: Matriks koefisien (list of list)
    - b: Vektor konstanta (list)

    Return:
    - x: Solusi sistem persamaan linear (list)
    """
    n = len(b)

    print("Langkah-langkah Eliminasi Gauss:")
    for i in range(n):
        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    b[i], b[j] = b[j], b[i]
                    print(f"Tukar baris {i+1} dengan baris {j+1}:")
                    tampilkan_matriks(A, b)
                    break

        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

            print(f"Eliminasi elemen A[{j+1}][{i+1}] menggunakan baris {i+1}:")
            tampilkan_matriks(A, b)

    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


def main():
    print("Sistem Persamaan Linear - Metode Eliminasi Gauss")
    print("================================================")

    n = int(input("Masukkan jumlah persamaan: "))

    print("\nMasukkan elemen matriks A:")
    A = []
    for i in range(n):
        baris = list(map(float, input(f"Baris {i+1}: ").split()))
        A.append(baris)

    print("\nMasukkan elemen vektor b:")
    b = []
    for i in range(n):
        nilai = float(input(f"b[{i+1}]: "))
        b.append(nilai)

    print("\nMatriks augmented awal:")
    tampilkan_matriks(A, b)

    solusi = eliminasi_gauss(A, b)

    print("Solusi sistem persamaan linear:")
    for i in range(n):
        print(f"x[{i+1}] = {solusi[i]:.3f}")


if __name__ == "__main__":
    main()