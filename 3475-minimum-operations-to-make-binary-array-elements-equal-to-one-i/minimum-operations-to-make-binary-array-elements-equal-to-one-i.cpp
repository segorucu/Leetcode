class Solution {
public:
    int minOperations(vector<int>& nums) {

        int zeros = 0;
        for (auto num : nums) if (num == 0) zeros++;

        int r = 0;
        int count = 0;
        while (zeros and r < nums.size()) {
            if (nums[r] == 0) {
                ++count;
                for (int p = 0; p < 3; p++){
                    if (r+p == nums.size()) return -1;
                    if (nums[r+p] == 0) zeros--;
                    else zeros++;
                    nums[r+p] = 1 - nums[r+p];
                }
                // for (int num : nums) {
                //     std::cout << num << " ";
                // }
                // std::cout << "\n";
            }
            ++r;
        }


        return count;
        
    }
};