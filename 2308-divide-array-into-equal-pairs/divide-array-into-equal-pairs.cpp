class Solution {
public:
    bool divideArray(vector<int>& nums) {
        unordered_map<int,int> counter;

        for (auto num:nums){
            if (counter.find(num) == counter.end()) counter[num] = 1;
            else counter[num] += 1;
        }

        for (const auto& [key,val]: counter) if (val % 2) return false;

        return true;
    }
};