class Solution {
public:
    int numberOfSubstrings(string s) {

        unordered_map<char, int> counter;
        int l = 0, ans = 0;
        int n = s.size();
        for (int r = 0; r < n; ++r) {
            counter[s[r]]++;
            if (counter.size() < 3) continue;
            while (counter[s[l]] > 1) {
                counter[s[l]]--;
                l++;
            }
            ans += l + 1;
        }



        return ans;
        
    }
};