class Solution {
public:
    int minimumRecolors(string blocks, int k) {

        int whites = 0;
        int ans = 1e7;
        int n = blocks.size();
        for (int i = 0; i < n; ++i) {
            if (blocks[i] == 'W') ++whites;
            if (i >= k and blocks[i-k] == 'W') --whites;
            if (i >= k-1) ans = min(ans,whites);
        }

        return ans;
        
    }
};