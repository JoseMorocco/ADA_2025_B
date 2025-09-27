#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>  
#include <ctime>    
#include <chrono>   

using namespace std;
using namespace std::chrono;

const int N = 10000; 

// A. Insertion Sort
void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// B. Selection Sort
void selectionSort(int arr[], int n) {
    int i, j, min_idx;
    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        swap(arr[min_idx], arr[i]);
    }
}


// C. Merge Sort 
void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    int *L = new int[n1];
    int *R = new int[n2];

    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
    
    delete[] L;
    delete[] R;
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

// D. Quicksort (Usando Pivote Aleatorio)
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
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
int partitionAleatorio(int arr[], int low, int high) {
    int random_index = low + (rand() % (high - low + 1));
    swap(arr[random_index], arr[high]); // Mueve el pivote al final
    return partition(arr, low, high);
}
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partitionAleatorio(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void generateAndCopyArray(int original[], int copy[], int size) {
    for (int i = 0; i < size; ++i) {
        original[i] = rand() % 100000; // Números aleatorios
    }
    copy_n(original, size, copy);
}

double measureTime(void (*sortFunc)(int[], int, int), int arr[], int size) {
    auto start = high_resolution_clock::now();
    sortFunc(arr, 0, size - 1);
    auto stop = high_resolution_clock::now();
    return duration_cast<milliseconds>(stop - start).count();
}

// Sobrecarga para Selection/Insertion Sort (solo necesita el tamaño n)
double measureTimeSimple(void (*sortFunc)(int[], int), int arr[], int size) {
    auto start = high_resolution_clock::now();
    sortFunc(arr, size);
    auto stop = high_resolution_clock::now();
    return duration_cast<milliseconds>(stop - start).count();
}

// Función Principal (main)

int main() {
    srand(time(0)); 
    
    // Arreglos de prueba
    int arr_original[N];
    int arr_copy[N];
    
    // Almacena los resultados
    double time_mergesort, time_quicksort, time_insertion, time_selection;

    cout << "--- Comparacion de Rendimiento (N=" << N << " elementos aleatorios) ---\n" << endl;
    
    generateAndCopyArray(arr_original, arr_copy, N);

    // 1. Quicksort
    copy_n(arr_original, N, arr_copy);
    time_quicksort = measureTime(quickSort, arr_copy, N);
    cout << "Quicksort (O(n log n)): \t" << time_quicksort << " ms" << endl;
    
    // 2. Mergesort
    copy_n(arr_original, N, arr_copy);
    time_mergesort = measureTime(mergeSort, arr_copy, N);
    cout << "Merge Sort (O(n log n)): \t" << time_mergesort << " ms" << endl;
    
    cout << "------------------------------------------" << endl;

    // 3. Insertion Sort
    copy_n(arr_original, N, arr_copy);
    time_insertion = measureTimeSimple(insertionSort, arr_copy, N);
    cout << "Insertion Sort (O(n^2)): \t" << time_insertion << " ms" << endl;
    
    // 4. Selection Sort
    copy_n(arr_original, N, arr_copy);
    time_selection = measureTimeSimple(selectionSort, arr_copy, N);
    cout << "Selection Sort (O(n^2)): \t" << time_selection << " ms" << endl;

    cout << "\nEl desempeño de los algoritmos O(n^2) es notablemente inferior para N=10,000." << endl;
    
    return 0;
}