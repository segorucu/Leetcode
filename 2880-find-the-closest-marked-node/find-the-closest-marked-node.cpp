class Solution {
public:
    int minimumDistance(int n, vector<vector<int>>& edges, int s, vector<int>& marked) {
        unordered_map<int,vector<tuple<int,int>>> graph;
        vector<int> distance(n,INT_MAX);

        for (const auto &edge: edges) {
            graph[edge[0]].push_back({edge[1],edge[2]});
        }

        dijkstra(n, s, graph, distance);

        int ans = INT_MAX;
        for (auto i: marked){
            ans = min(ans, distance[i]);
        }
        return (ans == INT_MAX) ? -1: ans;
    }

    void dijkstra(int n, int s, unordered_map<int,vector<tuple<int,int>>> &graph, vector<int> &distance){
        distance[s] = 0;
        priority_queue<tuple<int, int>, vector<tuple<int, int>>, greater<>> minHeap;
        minHeap.push({0,s});
        unordered_set<int> visited;

        while(!minHeap.empty()){
            auto [dist, node] = minHeap.top();
            minHeap.pop();
            visited.insert(node);
            for (auto [neigh, weight]: graph[node]){
                if (!visited.count(neigh)){
                    auto temp_dist = distance[node] + weight;
                    if (temp_dist < distance[neigh]){
                        distance[neigh] = temp_dist;
                        minHeap.push({temp_dist,neigh});
                    }
                }
            }
        }
        return;
    }
};