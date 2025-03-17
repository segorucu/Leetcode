class Solution {
public:
    bool canPermutePalindrome(string s) {

        unordered_map<char,int> counter;

        for (auto a:s) {
            counter[a] += 1;
        }

        int odd = 0;
        for (const auto &[key,val] : counter ) if (val % 2) odd += 1;

        return odd <= 1;
        
    }
};