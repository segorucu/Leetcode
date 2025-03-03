class Solution {
public:
    int minSwaps(vector<int>& data) {

        int ones = count(data.begin(),data.end(),1);
        int zeros = 0;
        int n = data.size();

        int r = 0;
        for (; r != ones; ++r) if (data[r] == 0) ++zeros;
        int ans = zeros;
        for (; r != n;++r) {
            if (data[r] == 0) ++zeros;
            if (data[r-ones] == 0) --zeros;
            ans = min(ans, zeros);

        }

        return ans;
        
    }
};