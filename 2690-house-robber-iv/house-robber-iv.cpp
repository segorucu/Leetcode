class Solution {
public:
    int minCapability(vector<int>& nums, int k) {

        int n = nums.size();
        int left = *min_element(nums.begin(),nums.end());
        int right = *max_element(nums.begin(),nums.end());

        auto good = [&] (int val) {
            vector<int> dp(n,0);
            if (nums[0] <= val) {
                dp[0] = 1;
                if (n == 1) return dp[0] >= k;
                dp[1] = 1;
            }
            if (n > 1 and nums[1] <= val) dp[1] = 1;
            for (int i = 2; i < n; ++i) {
                int add = 0;
                if (nums[i] <= val) add = 1;
                dp[i] = max(dp[i-1],dp[i-2]+add);
            }
            return dp[n-1] >= k;
        };

        int res = 0;
        while (left <= right) {
            int mid = (left+right) / 2;
            if (good(mid)){
                res = mid;
                right = mid-1;
            }
            else {
                left = mid+1;
            }

        }


        return res;
        
    }
};