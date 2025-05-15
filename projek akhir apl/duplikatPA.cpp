#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <conio.h> 

using namespace std;

int MAX_BARANG = 100;
int MAX_USER = 100;

struct Barang {
    string nama;
    string jenis;
    int jumlah;
};

struct User {
    string username;
    string password;
};

struct VapeStore {
    Barang barang[100];
    User users[100];
    int jumlahBarang = 6;
    int jumlahUser = 0;
};

void printWithColor(const string& text, const string& color) {
    string colorCode;
    if (color == "red") colorCode = "\033[31m"; 
    else if (color == "green") colorCode = "\033[32m"; 
    else if (color == "yellow") colorCode = "\033[33m"; 
    else if (color == "blue") colorCode = "\033[34m";   
    else if (color == "cyan") colorCode = "\033[36m";   
    else colorCode = "\033[0m"; 
    cout << colorCode << text << "\033[0m"; 
}

void tampilkanMenuLogin();
void prosesLogin(VapeStore* store, bool* loginBerhasil, bool* isAdmin); 
void prosesRegister(VapeStore* store); 
void tampilkanMenuUser();
void tampilkanMenuAdmin();
void tampilkanBarang(VapeStore* store); 
void tambahBarang(VapeStore* store); 
void ubahBarangDenganPointer(Barang* barang, int jumlahBarang); 
void hapusBarang(VapeStore* store); 
void tampilkanHeaderTabel();
void tampilkanBarisBarang(Barang* barang, int index); 
void tampilkanFooterTabel();
int hitungTotalBarang(VapeStore* store); 
int hitungTotalBarangByJenis(VapeStore* store, string* jenis);
void tampilkanInfoTotalBarang(VapeStore* store); 

void bubbleSortAscendingHuruf(Barang arr[], int n);
void selectionSortDescendingAngka(Barang arr[], int n);
void quickSortAscendingHuruf(Barang arr[], int low, int high);
int partition(Barang arr[], int low, int high);
void menuSortingUser(VapeStore* store);
void menuSortingAdmin(VapeStore* store);

string masukkanPassword() {
    string password;
    char ch;

    cout << "Password: ";
    while (true) {
        ch = _getch();

        if (ch == '\r') { 
            break;
        } else if (ch == '\b') { 
            if (!password.empty()) {
                password.pop_back();
                cout << "\b \b"; 
            }
        } else {
            password += ch;
            cout << '*'; 
        }
    }
    cout << endl;
    return password;
}


int main() {
    VapeStore store = {
        {{"Oxva xlim GO", "Device", 10}, {"Voopoo Drag X", "Device", 7}, {"TRML T99", "Device", 5}, 
         {"Makna V2 3mg", "Liquid", 15}, {"Bolu Lapis Talas V1 6mg", "Liquid", 12}, {"The Orama V1 3mg", "Liquid", 20}},
        {},
        6,
        0
    };

    while (true) {
        tampilkanMenuLogin();
        int menuLogin;
        cout << "Pilihan: ";
        cin >> menuLogin;

        switch (menuLogin) {
            case 1: {
                bool loginBerhasil = false;
                bool isAdmin = false;
                prosesLogin(&store, &loginBerhasil, &isAdmin);
                
                if (loginBerhasil) {
                    if (isAdmin) {
                        while (true) {
                            tampilkanMenuAdmin();
                            int pilihan;
                            cout << "Pilihan: ";
                            cin >> pilihan;

                            switch (pilihan) {
                                case 1: tampilkanBarang(&store); break;
                                case 2: tambahBarang(&store); break;
                                case 3: ubahBarangDenganPointer(store.barang, store.jumlahBarang); break;
                                case 4: hapusBarang(&store); break;
                                case 5: tampilkanInfoTotalBarang(&store); break;
                                case 6: menuSortingAdmin(&store); break;
                                case 7: 
                                    printWithColor("Logout berhasil.\n", "green");
                                    goto logout;
                                default: 
                                    printWithColor("Pilihan tidak valid!\n", "red");
                            }
                        }
                    } else {
                        while (true) {
                            tampilkanMenuUser();
                            int pilihan;
                            cout << "Pilihan: ";
                            cin >> pilihan;

                            switch (pilihan) {
                                case 1: tampilkanBarang(&store); break;
                                case 2: menuSortingUser(&store); break;
                                case 3: 
                                    printWithColor("Logout berhasil.\n", "green");
                                    goto logout;
                                default: 
                                    printWithColor("Pilihan tidak valid!\n", "red");
                            }
                        }
                    }
                    logout:;
                }
                break;
            }
            case 2:
                prosesRegister(&store); 
                break;
            case 3:
                printWithColor("Anda berhasil keluar dari program!.\n", "blue");
                return 0;
            default:
                printWithColor("Pilihan tidak valid!\n", "red");
        }
    }

    return 0;
}

void tampilkanMenuLogin() {
    printWithColor("\n=== Menu Login ===\n", "cyan");
    cout << "1. Login\n";
    cout << "2. Register\n";
    cout << "3. Keluar\n";
}

void prosesLogin(VapeStore* store, bool* loginBerhasil, bool* isAdmin) {
    string username, password;
    int attempts = 0;
    *loginBerhasil = false;
    *isAdmin = false;

    while (attempts < 3 && !(*loginBerhasil)) {
        cout << "Username: ";
        cin >> username;
        password = masukkanPassword();

        if (username == "google" && password == "kelompok4") {
            *loginBerhasil = true;
            *isAdmin = true;
            cout << "Login sebagai admin berhasil!\n";
            return;
        }

        for (int i = 0; i < store->jumlahUser; i++) {
            if (store->users[i].username == username && store->users[i].password == password) {
                *loginBerhasil = true;
                printWithColor("Login berhasil!\n", "green");
                return;
            }
        }

        printWithColor("Login gagal! Coba lagi.\n", "red");
        attempts++;
    }

    if (attempts == 3) {
        printWithColor("Kesempatan login anda habis.\n", "red");
    }
}

void prosesRegister(VapeStore* store) {
    if (store->jumlahUser >= MAX_USER) {
        printWithColor("Kapasitas user penuh!\n", "red");
        return;
    }

    cout << "Username: ";
    cin >> store->users[store->jumlahUser].username;
    store->users[store->jumlahUser].password = masukkanPassword();
    store->jumlahUser++;
    printWithColor("Registrasi berhasil!\n", "green");
}

void tampilkanMenuUser() {
    printWithColor("\n=== Menu User ===\n", "yellow");
    cout << "1. Tampilkan Barang\n";
    cout << "2. Sorting Barang\n";
    cout << "3. Logout\n";
}

void tampilkanMenuAdmin() {
    printWithColor("\n=== Menu Admin ===\n", "yellow");
    cout << "1. Tampilkan Barang\n";
    cout << "2. Tambah Barang\n";
    cout << "3. Ubah Barang\n";
    cout << "4. Hapus Barang\n";
    cout << "5. Info Total Barang\n";
    cout << "6. Urutkan Barang\n";
    cout << "7. Logout\n";
}

void tampilkanBarang(VapeStore* store) {
    if (store->jumlahBarang == 0) {
        printWithColor ("Belum ada barang dalam daftar.\n", "red");
        return;
    }

    tampilkanHeaderTabel();
    for (int i = 0; i < store->jumlahBarang; i++) {
        tampilkanBarisBarang(&(store->barang[i]), i + 1); 
    }
    tampilkanFooterTabel();
}

void tambahBarang(VapeStore* store) {
    if (store->jumlahBarang >= MAX_BARANG) {
        printWithColor ("Kapasitas penyimpanan penuh!\n", "red");
        return;
    }

    const int MAX_NAMA_BARANG = 15;

    string namaBarang;
    cout << "Nama barang (maksimal " << MAX_NAMA_BARANG << " karakter) : ";
    cin.ignore();
    getline(cin, namaBarang);

    while (namaBarang.length() > MAX_NAMA_BARANG) {
        cout << "Nama barang terlalu panjang! Masukkan nama barang dengan maksimal"
            << MAX_NAMA_BARANG << "karakter.\n";
        cout << "Nama barang: ";
        getline(cin, namaBarang);
    }

    store->barang[store->jumlahBarang].nama = namaBarang;

    cout << "Jenis (Device/Liquid): ";
    getline(cin, store->barang[store->jumlahBarang].jenis);

    cout << "Jumlah: ";
    cin >> store->barang[store->jumlahBarang].jumlah;
    store->jumlahBarang++;

    printWithColor ("Barang berhasil ditambahkan!\n", "green");
}

void ubahBarangDenganPointer(Barang* barang, int jumlahBarang) {
    if (jumlahBarang == 0) {
        cout << "Tidak ada barang untuk diubah.\n";
        return;
    }

    tampilkanHeaderTabel();
    for (int i = 0; i < jumlahBarang; i++) {
        tampilkanBarisBarang(&barang[i], i + 1);
    }
    tampilkanFooterTabel();

    int index;
    cout << "Pilih nomor barang yang ingin diubah: ";
    cin >> index;

    if (index < 1 || index > jumlahBarang) {
        cout << "Nomor tidak valid!\n";
        return;
    }

    Barang* barangToEdit = &barang[index - 1]; 
    cin.ignore();
    cout << "Nama baru: ";
    getline(cin, barangToEdit->nama);
    cout << "Jenis baru (Device/Liquid): ";
    getline(cin, barangToEdit->jenis);
    cout << "Jumlah baru: ";
    cin >> barangToEdit->jumlah;
    cout << "Barang berhasil diubah!\n";
}

void hapusBarang(VapeStore* store) {
    if (store->jumlahBarang == 0) {
        cout << "Tidak ada barang untuk dihapus.\n";
        return;
    }

    tampilkanBarang(store);
    int index;
    cout << "Pilih nomor barang yang akan dihapus: ";
    cin >> index;

    if (index < 1 || index > store->jumlahBarang) {
        cout << "Nomor tidak valid!\n";
        return;
    }

    for (int i = index - 1; i < store->jumlahBarang - 1; i++) {
        store->barang[i] = store->barang[i + 1];
    }
    store->jumlahBarang--;
    cout << "Barang berhasil dihapus!\n";
}

void tampilkanHeaderTabel() {
    printWithColor("+-----+----------------------+------------+--------+\n","blue");
    printWithColor("| No  | Nama Barang          | Jenis      | Jumlah |\n", "blue");
    printWithColor("+-----+----------------------+------------+--------+\n", "blue");
}

void tampilkanBarisBarang(Barang* barang, int index) {
    cout << "| " << setw(3) << index << " | " << setw(20) << barang->nama << " | " 
         << setw(10) << barang->jenis << " | " 
         << setw(6) << barang->jumlah << " |\n";
}

void tampilkanFooterTabel() {
    printWithColor("+-----+----------------------+------------+--------+\n", "blue");
}

int hitungTotalBarang(VapeStore* store) {
    int total = 0;
    for (int i = 0; i < store->jumlahBarang; i++) {
        total += store->barang[i].jumlah;
    }
    return total;
}

int hitungTotalBarangByJenis(VapeStore* store, string* jenis) {
    int total = 0;
    for (int i = 0; i < store->jumlahBarang; i++) {
        if (store->barang[i].jenis == *jenis) {
            total += store->barang[i].jumlah;
        }
    }
    return total;
}

void tampilkanInfoTotalBarang(VapeStore* store) {
    printWithColor("\n=== Informasi Total Barang ===\n", "cyan");
    cout << "Total semua barang: " << hitungTotalBarang(store) << endl;
    
    string jenis1 = "Device";
    string jenis2 = "Liquid";
    cout << "Total Device: " << hitungTotalBarangByJenis(store, &jenis1) << endl;
    cout << "Total Liquid: " << hitungTotalBarangByJenis(store, &jenis2) << endl;
}

void bubbleSortAscendingHuruf(Barang arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j].nama > arr[j+1].nama) {
                swap(arr[j], arr[j+1]);
            }
        }
    }
}

void selectionSortAscendingHuruf(Barang arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        int min_idx = i;
        for (int j = i+1; j < n; j++) {
            if (arr[j].nama < arr[min_idx].nama) {
                min_idx = j;
            }
        }
        swap(arr[min_idx], arr[i]);
    }
}

void bubbleSortDescendingAngka(Barang arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j].jumlah < arr[j+1].jumlah) {
                swap(arr[j], arr[j+1]);
            }
        }
    }
}

void selectionSortDescendingAngka(Barang arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        int max_idx = i;
        for (int j = i+1; j < n; j++) {
            if (arr[j].jumlah > arr[max_idx].jumlah) {
                max_idx = j;
            }
        }
        swap(arr[max_idx], arr[i]);
    }
}

int partition(Barang arr[], int low, int high) {
    string pivot = arr[high].nama;
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
        if (arr[j].nama < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}

void quickSortAscendingHuruf(Barang arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSortAscendingHuruf(arr, low, pi - 1);
        quickSortAscendingHuruf(arr, pi + 1, high);
    }
}

void menuSortingUser(VapeStore* store) {
    if (store->jumlahBarang == 0) {
        cout << "Tidak ada barang untuk diurutkan.\n";
        return;
    }

    printWithColor("\n=== Menu Sorting User ===\n", "yellow");
    cout << "1. Sorting Sesuai Abjad (A-Z)\n";
    cout << "2. Sorting dari jumlah terbesar - terkecil\n";
    cout << "3. Kembali\n";
    
    int pilihan;
    cout << "Pilihan: ";
    cin >> pilihan;

    Barang temp[100];
    for (int i = 0; i < store->jumlahBarang; i++) {
        temp[i] = store->barang[i];
    }

    switch (pilihan) {
        case 1:
        bubbleSortAscendingHuruf(temp, store->jumlahBarang);
        cout << "\nHasil Sorting sesuai abjad:\n";
        break;
        case 2:
        selectionSortDescendingAngka(temp, store->jumlahBarang);
        cout << "\nHasil Sorting dari jumlah angka terbesar ke terkecil:\n";
        break;
        case 3:
            return;
        default:
            cout << "Pilihan tidak valid!\n";
            return;
    }

    tampilkanHeaderTabel();
    for (int i = 0; i < store->jumlahBarang; i++) {
        tampilkanBarisBarang(&temp[i], i + 1);
    }
    tampilkanFooterTabel();
}

void menuSortingAdmin(VapeStore* store) {
    if (store->jumlahBarang == 0) {
        cout << "Tidak ada barang untuk diurutkan.\n";
        return;
    }

    printWithColor("\n=== Menu Sorting Admin ===\n", "cyan");
    cout << "1. Sorting Sesuai Abjad (A-Z):\n";
    cout << "2. Kembali\n";
    
    int pilihan;
    cout << "Pilihan: ";
    cin >> pilihan;

    Barang temp[100];
    for (int i = 0; i < store->jumlahBarang; i++) {
        temp[i] = store->barang[i];
    }

    switch (pilihan) {
        case 1:
            quickSortAscendingHuruf(temp, 0, store->jumlahBarang - 1);
            cout << "\nSorting Sesuai Abjad (A-Z):\n";
            break;
        case 2:
            return;
        default:
            printWithColor("Pilihan tidak valid!\n", "red");
            return;
    }

    tampilkanHeaderTabel();
    for (int i = 0; i < store->jumlahBarang; i++) {
        tampilkanBarisBarang(&temp[i], i + 1);
    }
    tampilkanFooterTabel();
}