def minkowski_distance(point1, point2, p):

    return sum(abs(x - y)**p for x, y in zip(point1, point2))**(1/p)

def get_coordinates(name):

    print(f"Masukkan koordinat untuk {name} (pisahkan dengan koma jika lebih dari dua dimensi):")
    coordinates = input(f"  Koordinat {name}: ").strip()
    return tuple(float(x) for x in coordinates.split(','))

def main():
    print("=== Program Menghitung Jarak dengan Minkowski Distance ===")
    
    gudang_a = get_coordinates("Gudang A")
    gudang_b = get_coordinates("Gudang B")
    toko = get_coordinates("Toko")

    p = float(input("\nMasukkan nilai parameter Minkowski (p ≥ 1, p = 1 untuk Manhattan, p = 2 untuk Euclidean): "))

    distance_to_a = minkowski_distance(toko, gudang_a, p)
    distance_to_b = minkowski_distance(toko, gudang_b, p)

    print("\n=== Jarak Gudang dan Toko ===")
    print(f"Koordinat Gudang A: {gudang_a}")
    print(f"Koordinat Gudang B: {gudang_b}")
    print(f"Koordinat Toko: {toko}")
    print(f"\nJarak toko ke Gudang A (Minkowski, p={p}): {distance_to_a:.2f}")
    print(f"Jarak toko ke Gudang B (Minkowski, p={p}): {distance_to_b:.2f}")


    if distance_to_a < distance_to_b:
        print("\nGudang A lebih dekat ke toko.")
    elif distance_to_b < distance_to_a:
        print("\nGudang B lebih dekat ke toko.")
    else:
        print("\nGudang A dan Gudang B memiliki jarak yang sama ke toko.")

if __name__ == "__main__":
    main()