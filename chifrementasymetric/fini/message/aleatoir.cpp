#include <iostream>
#include <ctime>

using namespace std;

// Paramètre : nombre de chiffres
int nombre_de_chiffres = 100;

// Renvoie un entier "aléatoire" basé sur clock()
unsigned long long random_seed() {
    return static_cast<unsigned long long>(clock());
}

// Modulo exponentiation : (base^exp) % mod
unsigned long long puissance_modulaire(unsigned long long base, unsigned long long exp, unsigned long long mod) {
    unsigned long long res = 1;
    base = base % mod;
    while (exp > 0) {
        if (exp % 2 == 1)
            res = (res * base) % mod;
        exp = exp / 2;
        base = (base * base) % mod;
    }
    return res;
}

// Test de primalité Miller-Rabin
bool miller_rabin(unsigned long long n, int k = 5) {
    if (n < 2)
        return false;
    if (n == 2 || n == 3)
        return true;
    if (n % 2 == 0)
        return false;

    // Trouver d et r tels que n-1 = 2^r * d
    unsigned long long d = n - 1;
    int r = 0;
    while (d % 2 == 0) {
        d /= 2;
        r++;
    }

    for (int i = 0; i < k; ++i) {
        unsigned long long a = 2 + random_seed() % (n - 3);
        unsigned long long x = puissance_modulaire(a, d, n);
        if (x == 1 || x == n - 1)
            continue;
        bool continue_outer = false;
        for (int j = 0; j < r - 1; ++j) {
            x = (x * x) % n;
            if (x == n - 1) {
                continue_outer = true;
                break;
            }
        }
        if (continue_outer)
            continue;
        return false;
    }
    return true;
}

// Génère un nombre impair aléatoire de n chiffres
unsigned long long random_impair(int chiffres) {
    unsigned long long debut = 1;
    for (int i = 1; i < chiffres; ++i)
        debut *= 10;
    unsigned long long fin = debut * 10 - 1;

    unsigned long long n = debut + (random_seed() % (fin - debut + 1));
    if (n % 2 == 0) n++; // Forcer impair
    if (n > fin) n = debut + 1; // Recycle si dépasse
    return n;
}

// Génère un nombre premier de n chiffres
unsigned long long generer_nombre_premier_chiffres(int chiffres) {
    while (true) {
        unsigned long long candidat = random_impair(chiffres);
        if (miller_rabin(candidat))
            return candidat;
    }
}

int main() {
    unsigned long long premier = generer_nombre_premier_chiffres(nombre_de_chiffres);
    cout << premier << endl;
    return 0;
}
