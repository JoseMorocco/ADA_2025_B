#include <iostream>
#include <vector>

int fibonacci(int n) {
    if (n < 0) { 
        return -1; 
    }
    if (n <= 1) {
        return n; 
    }
    std::vector<int> dp(n + 1); 
    dp[0] = 0; 
    dp[1] = 1; 
    for (int i = 2; i <= n; ++i) {
        dp[i] = dp[i - 1] + dp[i - 2]; 
    }
    return dp[n]; 
}

int main() {
    int n;
    std::cout << "Ingrese el número n para calcular Fibonacci(n): ";
    std::cin >> n;
    int result = fibonacci(n);
    if (result != -1) {
        std::cout << "El " << n << "-ésimo número de Fibonacci es: " << result << std::endl;
    } else {
        std::cout << "Número de entrada inválido." << std::endl;
    }
    return 0;
}