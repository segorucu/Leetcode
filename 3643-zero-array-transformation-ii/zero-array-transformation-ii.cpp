class Solution {
public:
    

    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int N = nums.size();

        auto good = [&] (int k) {
            vector<int> diff(N+1,0);
            int l, r, v;

            for (int i = 0; i < k; ++i) {
                l = queries[i][0];
                r = queries[i][1];
                v = queries[i][2];
                diff[l] += v;
                diff[r+1] -= v;
                }

            int curr = 0;
            for (int i = 0; i < N; ++i) {
                curr += diff[i];
                if (nums[i] > curr) return false;
            }

            return true;
            };

        int T = queries.size();
        int l = 0;
        int r = T+1;
        while (l < r) {
            int mid = (l+r) / 2;
            if (good(mid)) r = mid;
            else l = mid + 1;
        }

        if (l == T+1) return -1;
        return l;
        
    }
};