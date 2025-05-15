#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double f(double x) {
    return x * x * x - x - 3;  // Contoh fungsi: x^3 - x - 3
}

void metodeSecant(double x0, double x1, double toleransi, int iterasiMaks) {
    double x2, f0, f1, error;
    int iterasi = 0;

    cout << fixed << setprecision(6);
    cout << "Iterasi\t\tx0\t\tx1\t\tx2\t\tf(x2)\t\tError\n";
    cout << "----------------------------------------------------------------------\n";

    do {
        f0 = f(x0);
        f1 = f(x1);

        x2 = x1 - f1 * ((x1 - x0) / (f1 - f0));

        error = fabs(x2 - x1);

        cout << iterasi + 1 << "\t\t" << x0 << "\t" << x1 << "\t" << x2 << "\t" << f(x2) << "\t" << error << "\n";

        x0 = x1;
        x1 = x2;

        iterasi++;
    } while (error > toleransi && iterasi < iterasiMaks);

    cout << "----------------------------------------------------------------------\n";

    if (error <= toleransi) {
        cout << "Akar ditemukan: " << x2 << " dengan toleransi " << toleransi << "\n";
    } else {
        cout << "Metode gagal konvergen dalam " << iterasiMaks << " iterasi.\n";
    }
}

int main() {
    double x0, x1, toleransi;
    int iterasiMaks;
    cout << "Masukkan tebakan awal x0: ";
    cin >> x0;
    cout << "Masukkan tebakan awal x1: ";
    cin >> x1;
    cout << "Masukkan toleransi error: ";
    cin >> toleransi;
    cout << "Masukkan jumlah iterasi maksimum: ";
    cin >> iterasiMaks;
    
    metodeSecant(x0, x1, toleransi, iterasiMaks);

    return 0;
}