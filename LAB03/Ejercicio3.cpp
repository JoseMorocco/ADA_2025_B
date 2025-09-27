#include <iostream>
#include <algorithm> 
#include <cstdlib>   
#include <ctime>  
#include <chrono>   

using namespace std;
using namespace std::chrono;

const int N = 100000;

// 1. Quicksort (Usando Pivote Aleatorio para mayor eficiencia)
void swapPivot(float arr[], int index, int high) {
    swap(arr[index], arr[high]);
}
int partition(float arr[], int low, int high) {
    float pivot = arr[high];
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
int partitionAleatorio(float arr[], int low, int high) {
    int random_index = low + (rand() % (high - low + 1));
    swapPivot(arr, random_index, high);
    return partition(arr, low, high);
}
void quickSort(float arr[], int low, int high) {
    if (low < high) {
        int pi = partitionAleatorio(arr, low, high); 
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// 2. Búsqueda Binaria

int busquedaBinaria(float arr[], int l, int r, float x) {
    while (l <= r) {
        int m = l + (r - l) / 2;
        
        if (arr[m] == x)
            return m;
        
        if (arr[m] < x)
            l = m + 1;
        
        else // arr[m] > x
            r = m - 1;
    }
    return -1;
}

// 3. Búsqueda Secuencial 

int busquedaSecuencial(float arr[], int n, float x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x)
            return i;
    }
    return -1;
}

// 4. Funciones de Ayuda

// Genera un arreglo de 'size' con números aleatorios
void generateRandomArray(float arr[], int size) {
    for (int i = 0; i < size; ++i) {
        arr[i] = (float)(rand() % 20000) / 100.0f; 
    }
}

// Mide el tiempo en nanosegundos 
long long measureTimeNanos(void (*func)()) {
    auto start = high_resolution_clock::now();
    func();
    auto stop = high_resolution_clock::now();
    return duration_cast<nanoseconds>(stop - start).count();
}

// 5. Función Principal (main)

int main() {
    srand(time(0)); 
    
    float arr[N];
    generateRandomArray(arr, N);
    
    float elementoBuscado = arr[rand() % N]; 
    
    cout << "--- Analisis de Complejidad de Busqueda (N=" << N << ") ---\n" << endl;
    cout << "Elemento Buscado: " << elementoBuscado << endl;
    
    // A. BÚSQUEDA BINARIA (ORDENAMIENTO + BÚSQUEDA)
    cout << "\n1. Proceso de Busqueda Binaria (Requiere Ordenamiento)" << endl;
    
    auto start_sort = high_resolution_clock::now();
    quickSort(arr, 0, N - 1);
    auto stop_sort = high_resolution_clock::now();
    long long tiempo_ordenamiento = duration_cast<milliseconds>(stop_sort - start_sort).count();
    
    cout << "   - Tiempo de Ordenamiento (Quicksort): " << tiempo_ordenamiento << " ms" << endl;
    
    auto start_bin = high_resolution_clock::now();
    int index_bin = busquedaBinaria(arr, 0, N - 1, elementoBuscado);
    auto stop_bin = high_resolution_clock::now();
    long long tiempo_busqueda_bin = duration_cast<nanoseconds>(stop_bin - start_bin).count();

    cout << "   - Tiempo de Busqueda Binaria: " << tiempo_busqueda_bin << " ns" << endl;
    cout << "   - Resultado: " << (index_bin != -1 ? "Encontrado" : "No Encontrado") << endl;
    
    long long tiempo_total_ms = tiempo_ordenamiento; // Dominado por el ordenamiento
    cout << "\n   -> COMPLEJIDAD TOTAL (Ordenamiento + Busqueda): " 
         << tiempo_total_ms << " ms (Aproximado)" << endl;

    cout << "\n------------------------------------------------------------" << endl;

    // B. BÚSQUEDA SECUENCIAL (SIN ORDENAMIENTO PREVIO)

    // Re-generamos el arreglo 
    float arr_seq[N];
    generateRandomArray(arr_seq, N);
    arr_seq[N / 2] = elementoBuscado; // Aseguramos que el elemento esté presente
    
    cout << "2. Proceso de Busqueda Secuencial (No Requiere Ordenamiento)" << endl;

    auto start_seq = high_resolution_clock::now();
    int index_seq = busquedaSecuencial(arr_seq, N, elementoBuscado);
    auto stop_seq = high_resolution_clock::now();
    long long tiempo_busqueda_seq = duration_cast<nanoseconds>(stop_seq - start_seq).count();

    cout << "   - Tiempo de Busqueda Secuencial: " << tiempo_busqueda_seq << " ns" << endl;
    cout << "   - Resultado: " << (index_seq != -1 ? "Encontrado" : "No Encontrado") << endl;

    cout << "\n   -> COMPLEJIDAD TOTAL (Solo Busqueda): " 
         << tiempo_busqueda_seq << " ns" << endl;

    return 0;
}