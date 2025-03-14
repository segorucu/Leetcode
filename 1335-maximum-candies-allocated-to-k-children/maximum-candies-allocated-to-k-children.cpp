class Solution {
public:
    int maximumCandies(vector<int>& candies, long long k) {

        auto good = [&] (int val) {
            long long count = 0;
            if (val == 0) return true;
            for (int i = 0; i < candies.size(); ++i){
                count += (candies[i] / val);
                if (count >= k) return true;
            }
            return false;
        };

        long long l = 1;
        long long r = accumulate(candies.begin(), candies.end(), 0LL) / k;
        int res = 0;

        while (l <= r) {
            long long mid = (l+r) / 2;
            if (good(mid)) {
                res = mid;
                l = mid+1;
            }
            else {
                r = mid-1;
            }
        }

        return res;
        
    }
};