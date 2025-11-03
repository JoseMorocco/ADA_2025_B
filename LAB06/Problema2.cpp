// Código C++
#include <iostream>
#include <vector>
#include <algorithm> 

const int INF = 1e9; 

int minCostPath(const std::vector<std::vector<int>>& cost, int start, int end) {
    int numStations = cost.size();
    std::vector<int> dp(numStations, INF);

    dp[start - 1] = 0; 

    for (int i = start - 1; i < end; ++i) {
        if (dp[i] == INF) continue; 

        for (int j = i + 1; j < numStations; ++j) {
            if (cost[i][j] != INF) { 
                dp[j] = std::min(dp[j], dp[i] + cost[i][j]);
            }
        }
    }
    return dp[end - 1];
}

int main() {
    std::vector<std::vector<int>> cost = {
        {INF, 3,   2,   INF, INF}, 
        {INF, INF, INF, 4,   INF}, 
        {INF, INF, INF, INF, 2  }, 
        {INF, INF, INF, INF, 3  }, 
        {INF, INF, INF, INF, INF}  
    };

    int start_station = 1;
    int end_station = 5;

    int min_cost = minCostPath(cost, start_station, end_station);

    if (min_cost == INF) {
        std::cout << "No se encontró un camino de " << start_station << " a " << end_station << std::endl;
    } else {
        std::cout << "El camino de menor costo de la estación " << start_station
                  << " a la estación " << end_station << " es: " << min_cost << std::endl;
    }
    return 0;
}