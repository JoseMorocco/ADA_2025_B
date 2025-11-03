#include <iostream>
#include <vector>
#include <algorithm> // Para std::sort

// Estructura para representar un objeto
struct Item {
    int weight;
    int value;
    double ratio; // Valor por unidad de peso

    Item(int w, int v) : weight(w), value(v) {
        ratio = static_cast<double>(value) / weight;
    }
};

// Función de comparación para ordenar los objetos por su ratio de valor/peso en orden descendente
bool compareItems(const Item& a, const Item& b) {
    return a.ratio > b.ratio;
}

double fractionalKnapsack(int W, std::vector<Item>& items) {
    std::sort(items.begin(), items.end(), compareItems);

    double total_value = 0.0;
    int current_weight = 0;

    for (const auto& item : items) {
        if (current_weight + item.weight <= W) {
            current_weight += item.weight;
            total_value += item.value;
        } else {
            int remaining_capacity = W - current_weight;
            total_value += item.ratio * remaining_capacity;
            current_weight += remaining_capacity; 
            break;
        }
    }
    return total_value;
}

int main() {
    int W = 4; // Capacidad de la mochila
    std::vector<Item> items;
    items.emplace_back(1, 1); // Objeto A: peso 1, valor 1
    items.emplace_back(3, 4); // Objeto B: peso 3, valor 4
    items.emplace_back(4, 5); // Objeto C: peso 4, valor 5

    double max_value = fractionalKnapsack(W, items);
    std::cout << "El valor máximo que se puede obtener en la mochila (fraccionaria) es: " << max_value << std::endl;
    // Para W=4:
    // A: 1/1 = 1.0
    // B: 4/3 = 1.33
    // C: 5/4 = 1.25
    // Orden: B, C, A
    // Tomar B (3kg, 4 valor) -> Queda 1kg. total 4.
    // Tomar 1/4 de C (1kg, 1.25 valor) -> Queda 0kg. total 4 + 1.25 = 5.25
    // Entonces, si solo consideramos los objetos del ejemplo, el resultado será 5.25.

    W = 10;
    std::vector<Item> items2;
    items2.emplace_back(10, 60);
    items2.emplace_back(20, 100);
    items2.emplace_back(30, 120);

    max_value = fractionalKnapsack(W, items2);
    std::cout << "El valor máximo para W=10, objetos {10,20,30} y valores {60,100,120} es: " << max_value << std::endl;
    // Ratios:
    // Item1: 60/10 = 6
    // Item2: 100/20 = 5
    // Item3: 120/30 = 4
    // Orden: Item1 (6), Item2 (5), Item3 (4)
    // Tomar 10/10 de Item1 (10kg, 60 valor) -> Queda 0kg. Total 60.

    return 0;
}