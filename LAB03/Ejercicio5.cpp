#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <cstdlib>
#include <ctime>

using namespace std;

struct Producto {
    string codigo;
    string nombre;
    float precio;

    bool operator<=(const Producto& otro) const {
        return otro.precio <= precio;
    }
    bool operator<(const Producto& otro) const {
        return precio > otro.precio;
    }
};


// Funcion para leer el archivo y cargar los productos
vector<Producto> leerProductosDesdeArchivo(const string& nombreArchivo) {
    vector<Producto> productos;
    ifstream archivo(nombreArchivo);
    string linea;
    if (!archivo.is_open()) {
        cerr << "Error: No se pudo abrir el archivo " << nombreArchivo << endl;
        return productos;
    }
    while (getline(archivo, linea)) {
        stringstream ss(linea);
        string segmento;
        Producto p;
        try {
            getline(ss, p.codigo, ','); // Leer Codigo
            getline(ss, p.nombre, ','); // Leer Nombre
            getline(ss, segmento, ','); // Leer Precio
            p.precio = stof(segmento); // Convierte string a float
            productos.push_back(p);
        } catch (const exception& e) {
            cerr << "Advertencia: Linea con formato invalido saltada: " << linea << endl;
        }
    }
    archivo.close();
    return productos;
}

void mostrarProductos(const vector<Producto>& productos, const string& titulo) {
    cout << "\n--- " << titulo << " (" << productos.size() << " productos) ---" << endl;
    cout << left << setw(10) << "CODIGO"
         << setw(30) << "NOMBRE"
         << right << setw(15) << "PRECIO" << endl;
    cout << string(55, '-') << endl;
    
    cout << fixed << setprecision(2);

    for (const auto& p : productos) {
        cout << left << setw(10) << p.codigo
             << setw(30) << p.nombre
             << right << setw(15) << p.precio << endl;
    }
}

// Merge Sort 
void merge(vector<Producto>& arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    vector<Producto> L(n1);
    vector<Producto> R(n2);

    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    int i = 0, j = 0, k = l;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) { 
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}
void mergeSort(vector<Producto>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

// Quicksort 

int partition(vector<Producto>& arr, int low, int high) {
    Producto pivot = arr[high]; // Pivote fijo (último elemento)
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) { 
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}
void quickSort(vector<Producto>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Función Principal

int main() {
    vector<Producto> productos = leerProductosDesdeArchivo("productos.txt");

    if (productos.empty()) {
        cout << "No se cargaron productos. Asegurese de que 'productos.txt' exista y tenga datos validos." << endl;
        return 0;
    }


    // Ordenamiento con Merge Sort
    vector<Producto> merge_copy = productos;
    mergeSort(merge_copy, 0, merge_copy.size() - 1);
    mostrarProductos(merge_copy, "Lista Ordenada con Merge Sort (Mayor a Menor)");

    // Ordenamiento con Quicksort
    vector<Producto> quick_copy = productos;
    quickSort(quick_copy, 0, quick_copy.size() - 1);
    mostrarProductos(quick_copy, "Lista Ordenada con Quicksort (Mayor a Menor)");

    return 0;
}