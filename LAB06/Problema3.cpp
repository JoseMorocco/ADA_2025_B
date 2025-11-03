// Código C++
#include <iostream>
#include <vector>
#include <algorithm> // Para std::max

int knapsack01(int W, const std::vector<int>& weights, const std::vector<int>& values) {
    int n = weights.size();
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(W + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int w = 1; w <= W; ++w) {
            if (weights[i - 1] <= w) {
                dp[i][w] = std::max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    return dp[n][W];
}

int main() {
    int W_ej1 = 4; // Capacidad de la mochila
    std::vector<int> weights_ej1 = {1, 3, 4}; // Pesos de los objetos A, B, C
    std::vector<int> values_ej1 = {1, 4, 5};  // Valores de los objetos A, B, C

    int max_value_ej1 = knapsack01(W_ej1, weights_ej1, values_ej1);
    std::cout << "Para W=" << W_ej1 << ", el valor máximo (0/1) es: " << max_value_ej1 << std::endl; 

    int W_ej2 = 7;
    std::vector<int> weights_ej2 = {1, 3, 4, 5};
    std::vector<int> values_ej2 = {1, 4, 5, 7};
    int max_value_ej2 = knapsack01(W_ej2, weights_ej2, values_ej2);
    std::cout << "Para W=" << W_ej2 << ", el valor máximo (0/1) es: " << max_value_ej2 << std::endl; 

    return 0;
}