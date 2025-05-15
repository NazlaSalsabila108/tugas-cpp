def tampilkan_matriks(A, b):
    """
    Fungsi untuk menampilkan matriks augmented [A|b] ke layar.
    """
    n = len(b)
    for i in range(n):
        baris = ""
        for j in range(len(A[i])):
            baris += f"{A[i][j]:8.3f} "
        baris += f"| {b[i]:8.3f}"
        print(baris)
    print()


def gauss_jordan(A, b):
    """
    Fungsi untuk menyelesaikan sistem persamaan linear Ax = b
    menggunakan metode Gauss Jordan.

    Parameter:
    - A: Matriks koefisien (list of list)
    - b: Vektor konstanta (list)

    Return:
    - x: Solusi sistem persamaan linear (list)
    """
    n = len(b)

    print("Langkah-langkah Gauss Jordan:")
    for i in range(n):
        faktor = A[i][i]
        for j in range(n):
            A[i][j] /= faktor
        b[i] /= faktor

        print(f"Normalisasi baris {i+1} (diagonal utama jadi 1):")
        tampilkan_matriks(A, b)
        for k in range(n):
            if k != i:
                faktor = A[k][i]
                for j in range(n):
                    A[k][j] -= faktor * A[i][j]
                b[k] -= faktor * b[i]

                print(f"Eliminasi elemen A[{k+1}][{i+1}] menggunakan baris {i+1}:")
                tampilkan_matriks(A, b)

    return b


def main():
    print("Sistem Persamaan Linear - Metode Gauss Jordan")
    print("=============================================")
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

    solusi = gauss_jordan(A, b)

    print("Solusi sistem persamaan linear:")
    for i in range(n):
        print(f"x[{i+1}] = {solusi[i]:.3f}")


if __name__ == "__main__":
    main()