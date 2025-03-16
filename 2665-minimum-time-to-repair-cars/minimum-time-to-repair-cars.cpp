class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {

        long long left = 0;
        long long right = 0;
        right = 1e14;

        auto good = [&] (long long val) {
            long long tot = 0;
            for (auto rank:ranks) {
                tot += sqrt(val/rank);
            }
            return tot >= cars;
        };

        long long res = 0;
        while (left <= right){
            long long mid = (left+right)/2;
            // cout << left << " " << right << " " << mid << "\n";
            if (good(mid)) {
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