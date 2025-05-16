import numpy as np

def mahalanobis_distance(point, mean, kovarians_matriks):

    diff = point - mean
    inv_cov_matrix = np.linalg.pinv(kovarians_matriks) 
    distance = np.sqrt(np.dot(np.dot(diff.T, inv_cov_matrix), diff))
    return distance

def main():
    gudang_a = np.array([4, 5])
    gudang_b = np.array([11, 3])
    toko = np.array([3, 8])

    mean = (gudang_a + gudang_b) / 2

    devisiasi = np.array([gudang_a - mean, gudang_b - mean])
    kovarians_matriks = np.cov(devisiasi.T)

    distance_to_a = mahalanobis_distance(toko, gudang_a, kovarians_matriks)
    distance_to_b = mahalanobis_distance(toko, gudang_b, kovarians_matriks)

    print("=== Hasil Perhitungan Jarak Mahalanobis ===")
    print(f"Koordinat Gudang A: {gudang_a}")
    print(f"Koordinat Gudang B: {gudang_b}")
    print(f"Koordinat Toko: {toko}")
    print(f"Mean (Pusat Distribusi): {mean}")
    print(f"Matriks Kovarians:\n{kovarians_matriks}")
    print(f"\nJarak Mahalanobis ke Gudang A: {distance_to_a:.2f}")
    print(f"Jarak Mahalanobis ke Gudang B: {distance_to_b:.2f}")

    if distance_to_a < distance_to_b:
        print("\nGudang A lebih dekat ke toko.")
    else:
        print("\nGudang B lebih dekat ke toko.")

if __name__ == "__main__":
    main()