class Solution {
public:
    int minimumRecolors(string blocks, int k) {

        int whites = 0;
        for (int i = 0; i < k; ++i) {
            if (blocks[i] == 'W') ++whites; 
        }

        int ans = whites;
        int n = blocks.size();
        for (int i = k; i < n; ++i) {
            if (blocks[i] == 'W') ++whites;
            if (blocks[i-k] == 'W') --whites;
            ans = min(ans,whites);
        }

        return ans;
        
    }
};