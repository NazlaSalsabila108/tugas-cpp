def input_matriks(baris, kolom):
    print(f"Masukkan elemen matriks berukuran {baris}x{kolom}:")
    matriks = []
    for i in range(baris):
        baris_data = []
        for j in range(kolom):
            elemen = int(input(f"Elemen [{i+1},{j+1}]: "))
            baris_data.append(elemen)
        matriks.append(baris_data)
    return matriks

def cetak_matriks(matriks):

    for baris in matriks:
        print(" ".join(map(str, baris)))

def kalikan_matriks(matriks1, matriks2):

    baris_matriks1 = len(matriks1)
    kolom_matriks1 = len(matriks1[0])
    kolom_matriks2 = len(matriks2[0])

    hasil = [[0 for _ in range(kolom_matriks2)] for _ in range(baris_matriks1)]

    for i in range(baris_matriks1):
        for j in range(kolom_matriks2):
            for k in range(kolom_matriks1):
                hasil[i][j] += matriks1[i][k] * matriks2[k][j]
    return hasil

def main():
    print("Mari Menghitung Perkalian Matriks")

    baris1 = int(input("Masukkan jumlah baris untuk matriks pertama: "))
    kolom1 = int(input("Masukkan jumlah kolom untuk matriks pertama: "))

    baris2 = int(input("Masukkan jumlah baris untuk matriks kedua: "))
    kolom2 = int(input("Masukkan jumlah kolom untuk matriks kedua: "))

    if kolom1 != baris2:
        print("Perkalian matriks ini tidak dimungkinkan. Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.")
        return

    matriks1 = input_matriks(baris1, kolom1)
    matriks2 = input_matriks(baris2, kolom2)

    print("\nMatriks 1:")
    cetak_matriks(matriks1)

    print("\nMatriks 2:")
    cetak_matriks(matriks2)

    hasil = kalikan_matriks(matriks1, matriks2)
    
    print("\nHasil Perkalian Matriks:")
    cetak_matriks(hasil)

if __name__ == "__main__":
    main()