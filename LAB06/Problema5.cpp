#include <iostream>
#include <vector>

int countWaysToClimbStairs(int n) {
    if (n < 0) {
        return 0; 
    }
    if (n == 0) {
        return 1; 
    }

    std::vector<int> dp(n + 1);
    dp[0] = 1; 

    for (int i = 1; i <= n; ++i) {
        dp[i] = 0;
        if (i - 1 >= 0) {
            dp[i] += dp[i - 1];
        }
        if (i - 2 >= 0) {
            dp[i] += dp[i - 2];
        }
        if (i - 3 >= 0) {
            dp[i] += dp[i - 3];
        }
    }
    return dp[n];
}

int main() {
    int n;
    std::cout << "Ingrese el número de escalones: ";
    std::cin >> n;
    std::cout << "Número de formas de llegar al escalón " << n << ": " << countWaysToClimbStairs(n) << std::endl;

    std::cout << "Para 1 escalón: " << countWaysToClimbStairs(1) << std::endl;
    std::cout << "Para 2 escalones: " << countWaysToClimbStairs(2) << std::endl;
    std::cout << "Para 3 escalones: " << countWaysToClimbStairs(3) << std::endl;
    std::cout << "Para 4 escalones: " << countWaysToClimbStairs(4) << std::endl;


    return 0;
}