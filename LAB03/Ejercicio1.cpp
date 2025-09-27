#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

struct Estudiante {
    string codigo;
    string nombre;
    float promedioPonderado;

    bool operator<=(const Estudiante& otro) const {
        return promedioPonderado <= otro.promedioPonderado;
    }
};

void merge(vector<Estudiante>& arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    vector<Estudiante> L(n1);
    vector<Estudiante> R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }

    while (i < n1) {
        arr[k++] = L[i++];
    }

    while (j < n2) {
        arr[k++] = R[j++];
    }
}

void mergeSort(vector<Estudiante>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}

void ingresarEstudiantes(vector<Estudiante>& estudiantes) {
    int numEstudiantes;
    cout << "Ingrese el numero de estudiantes a registrar: ";
    cin >> numEstudiantes;
    cin.ignore();

    if (numEstudiantes <= 0) return;

    cin.ignore();

    cout << "\n--- Ingreso de Registros ---" << endl;
    for (int i = 0; i < numEstudiantes; ++i) {
        Estudiante e;
        cout << "\nEstudiante #" << i + 1 << endl;

        cout << "   Codigo: ";
        getline(cin, e.codigo);

        cout << "   Nombre: ";
        getline(cin, e.nombre);

        cout << "   Promedio ponderado (float): ";
        while (!(cin >> e.promedioPonderado)) {
            cout << "Entrada invalida. Por favor, ingrese un numero para el promedio: ";
            cin.clear(); 
            cin.ignore(10000, '\n'); 
        }
        cin.ignore(); 
        
        estudiantes.push_back(e);
    }
}

void mostrarEstudiantes(const vector<Estudiante>& estudiantes) {
    cout << "\n--- Lista de Estudiantes Ordenada por Promedio Ponderado ---" << endl;
    cout << left << setw(10) << "CODIGO"
         << setw(30) << "NOMBRE"
         << right << setw(15) << "PROMEDIO" << endl;
    cout << string(55, '-') << endl;
    
    cout << fixed << setprecision(2);

    for (const auto& e : estudiantes) {
        cout << left << setw(10) << e.codigo
             << setw(30) << e.nombre
             << right << setw(15) << e.promedioPonderado << endl;
    }
}

// --- Función principal ---
int main() {
    vector<Estudiante> estudiantes; 

    ingresarEstudiantes(estudiantes);

    if (estudiantes.empty()) {
        cout << "\nNo se ingresaron estudiantes. El programa finaliza." << endl;
        return 0;
    }

    mergeSort(estudiantes, 0, estudiantes.size() - 1);

    mostrarEstudiantes(estudiantes);

    return 0;
}