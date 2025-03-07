class Solution {
public:
    vector<int> closestPrimes(int left, int right) {

        vector<bool> isPrime(right+1, true);
        vector<int> ans = {-1,-1};
        isPrime[0] = false;
        isPrime[1] = false;
        int maxval = int(sqrt(right)) + 1;

        for (int i = 2; i <= maxval; ++i) {
            if (isPrime[i]) {
                for (int j = 2*i; j <= right; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        int prev = -1;
        int minval = 1e9;
        for (int i = left; i <= right; ++i) {
            if (isPrime[i]) {
                if (prev > 0 and (i - prev < minval)) {
                    ans = {prev, i};
                    minval = i - prev;
                }
                prev = i;
            }
        }

        return ans;
        
    }
};