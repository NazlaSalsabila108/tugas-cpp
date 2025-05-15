import heapq

class SistemPemesananTiket:
    def __init__(self):
        self.graf = {}

    def tambah_penerbangan(self, asal, tujuan, harga):
        """Menambahkan penerbangan ke dalam graf"""
        if asal not in self.graf:
            self.graf[asal] = []
        if tujuan not in self.graf:
            self.graf[tujuan] = []
        self.graf[asal].append((tujuan, harga))
        self.graf[tujuan].append((asal, harga))  

    def cari_rute_termurah(self, kota_asal, kota_tujuan):
        """Mencari rute termurah menggunakan algoritma Dijkstra"""
        antrian_prioritas = [] 
        heapq.heappush(antrian_prioritas, (0, kota_asal))  
        jarak = {kota: float('inf') for kota in self.graf}
        jarak[kota_asal] = 0
        simpul_sebelumnya = {kota: None for kota in self.graf}

        while antrian_prioritas:
            harga_saat_ini, kota_saat_ini = heapq.heappop(antrian_prioritas)

            if kota_saat_ini == kota_tujuan:
                break

            for tetangga, harga in self.graf[kota_saat_ini]:
                harga_baru = harga_saat_ini + harga
                if harga_baru < jarak[tetangga]:
                    jarak[tetangga] = harga_baru
                    simpul_sebelumnya[tetangga] = kota_saat_ini
                    heapq.heappush(antrian_prioritas, (harga_baru, tetangga))

        jalur = []
        kota_sekarang = kota_tujuan
        while kota_sekarang is not None:
            jalur.append(kota_sekarang)
            kota_sekarang = simpul_sebelumnya[kota_sekarang]
        jalur.reverse()

        return jarak[kota_tujuan], jalur


def main():
    sistem = SistemPemesananTiket()

    print("Masukkan daftar penerbangan dalam format: asal tujuan harga")
    print("Ketik 'selesai' jika sudah selesai memasukkan data:")
    while True:
        input_data = input()
        if input_data.strip().lower() == 'selesai':
            break
        asal, tujuan, harga = input_data.split()
        sistem.tambah_penerbangan(asal, tujuan, int(harga))

    print("\nSilahkan masukkan kota asal dan kota tujuan:")
    kota_asal = input("Kota asal: ").strip()
    kota_tujuan = input("Kota tujuan: ").strip()

    if kota_asal not in sistem.graf or kota_tujuan not in sistem.graf:
        print("Kota asal atau tujuan tidak ditemukan dalam sistem.")
        return

    biaya, rute = sistem.cari_rute_termurah(kota_asal, kota_tujuan)
    if biaya == float('inf'):
        print(f"Tidak ada rute dari {kota_asal} ke {kota_tujuan}.")
    else:
        print(f"Rute termurah dari {kota_asal} ke {kota_tujuan}: {' -> '.join(rute)} dengan harga {biaya}")


if __name__ == "__main__":
    main()