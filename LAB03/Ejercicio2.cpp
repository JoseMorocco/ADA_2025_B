#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <chrono> 
using namespace std;
using namespace std::chrono;

// Genera un arreglo de 'size' con números aleatorios (Caso Promedio)
void generateRandomArray(float arr[], int size) {
    srand(time(0));
    for (int i = 0; i < size; ++i) {
        arr[i] = (float)(rand() % 1000) / 10.0f;
    }
}

// Genera un arreglo ya ordenado (Peor Caso para Pivote Fijo)
void generateSortedArray(float arr[], int size) {
    for (int i = 0; i < size; ++i) {
        arr[i] = (float)i + 0.5f;
    }
}

// Mide y muestra el tiempo de ejecución
double measureTime(void (*sortFunc)(float[], int, int), float arr[], int size) {
    auto start = high_resolution_clock::now();
    sortFunc(arr, 0, size - 1);
    auto stop = high_resolution_clock::now();
    
    auto duration = duration_cast<milliseconds>(stop - start);
    return duration.count();
}

void printArray(float arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " "; 
    cout << endl;
}

// 2. Funciones de Quicksort

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
void quickSortFijo(float arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSortFijo(arr, low, pi - 1);
        quickSortFijo(arr, pi + 1, high);
    }
}

int partitionAleatorio(float arr[], int low, int high) {
    int random_index = low + (rand() % (high - low + 1));
    swapPivot(arr, random_index, high); 
    return partition(arr, low, high);
}
void quickSortAleatorio(float arr[], int low, int high) {
    if (low < high) {
        int pi = partitionAleatorio(arr, low, high);
        quickSortAleatorio(arr, low, pi - 1);
        quickSortAleatorio(arr, pi + 1, high);
    }
}
void swapPivot(float arr[], int index, int high) {
    swap(arr[index], arr[high]);
}

// 3. Función Principal (main)
int main() {

    float arr1[] = {5.1f, 1.3f, 4.2f, 8.7f, 2.0f, 6.9f};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);

    cout << "--- Quicksort con Pivote Fijo ---" << endl;
    cout << "Arreglo original: ";
    printArray(arr1, n1);

    quickSortFijo(arr1, 0, n1 - 1);

    cout << "Arreglo ordenado: ";
    printArray(arr1, n1);
    
    cout << "\n-----------------------------------" << endl;

    // Se usa una copia del arreglo para probar el pivote aleatorio
    float arr2[] = {5.1f, 1.3f, 4.2f, 8.7f, 2.0f, 6.9f};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    
    cout << "--- Quicksort con Pivote Aleatorio ---" << endl;
    cout << "Arreglo original: ";
    printArray(arr2, n2);

    quickSortAleatorio(arr2, 0, n2 - 1);

    cout << "Arreglo ordenado: ";
    printArray(arr2, n2);
    srand(time(0)); 
    
    const int N = 10000; 
    
    float arrA_random[N];
    float arrB_random[N];
    float arrC_sorted[N];
    float arrD_sorted[N];
    
    double tiempoFijo, tiempoAleatorio;

    cout << "--- Analisis de Rendimiento de Quicksort (N=" << N << ") ---\n" << endl;

    generateRandomArray(arrA_random, N);
    copy(arrA_random, arrA_random + N, arrB_random); 
    cout << "1. PRUEBA CON ARREGLO ALEATORIO (Caso Promedio):\n";
    
    tiempoFijo = measureTime(quickSortFijo, arrA_random, N);
    cout << "   -> Pivote Fijo: " << tiempoFijo << " ms" << endl;
    
    tiempoAleatorio = measureTime(quickSortAleatorio, arrB_random, N);
    cout << "   -> Pivote Aleatorio: " << tiempoAleatorio << " ms" << endl;
    
    cout << "\n------------------------------------------------------------\n";

    generateSortedArray(arrC_sorted, N);
    copy(arrC_sorted, arrC_sorted + N, arrD_sorted); 

    cout << "2. PRUEBA CON ARREGLO ORDENADO (Peor Caso):\n";
    
    tiempoFijo = measureTime(quickSortFijo, arrC_sorted, N);
    cout << "   -> Pivote Fijo: " << tiempoFijo << " ms" << endl; 
    
    tiempoAleatorio = measureTime(quickSortAleatorio, arrD_sorted, N);
    cout << "   -> Pivote Aleatorio: " << tiempoAleatorio << " ms" << endl;
    
    return 0;
}