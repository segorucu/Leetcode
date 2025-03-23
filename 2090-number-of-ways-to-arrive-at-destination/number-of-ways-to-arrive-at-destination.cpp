class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        unordered_map <int, vector<tuple<int,long long>>> graph;
        vector<long long> distance(n, LLONG_MAX);
        vector<int> dp(n,0);
        distance[0] = 0;
        dp[0] = 1;

        for (const auto&road: roads){
            int u = road[0];
            int v = road[1];
            long long w = road[2];
            graph[u].push_back({v,w});
            graph[v].push_back({u,w});
        }

        dijkstra(n, distance, dp, graph);

        
        return dp[n-1];
    }

    void dijkstra(int n, vector<long long> &distance, vector<int> &dp, unordered_map <int, vector<tuple<int,long long>>> &graph){

        priority_queue<tuple<long long, int>, vector<tuple<long long, int>>, greater<>> minHeap;
        minHeap.push({0,0});
        long long MOD = pow(10,9)+7;

        while (!minHeap.empty()){
            auto [dist, node] = minHeap.top();
            minHeap.pop();

            for (const auto [neigh,weight] :graph[node]){
                long long temp_dist = dist + weight;
                if (temp_dist < distance[neigh]){
                    distance[neigh] = temp_dist;
                    minHeap.push({temp_dist, neigh});
                    dp[neigh] = dp[node];
                }
                else if (temp_dist == distance[neigh]){
                    dp[neigh] = (dp[neigh] + dp[node]) % MOD;
                }
            }
        }

        return;
    }
};