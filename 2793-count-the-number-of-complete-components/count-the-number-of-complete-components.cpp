class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {

        set<int> visited;
        int count = 0;
        unordered_map<int,vector<int>> graph;
        set<int> curr;

        for (const auto edge : edges) {
            int a = edge[0];
            int b = edge[1];
            graph[a].push_back(b);
            graph[b].push_back(a);
        }

        function <void(int)> dfs = [&](int i){
            for (int j: graph[i]){
                if(visited.count(j)) continue;
                visited.insert(j);
                curr.insert(j);
                dfs(j);
                
            }
        };

        for (int i = 0; i < n; ++i){
            if (visited.count(i)) continue;
            visited.insert(i);
            curr = {};
            curr.insert(i);
            dfs(i);
            int n = curr.size();
            bool component = true;
            for (auto k: curr){
                if (graph[k].size() != n-1) {
                    component = false;
                    break;
                }
            }
            if (component) count++;
        }



        return count;
        
    }
};