class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {
        int maxh = 0;
        int n = heights.size();
        vector<int> arr;

        for (int i = n-1; i >= 0; i--){
            if (heights[i] > maxh){
                maxh = heights[i];
                arr.push_back(i);
            }
        }

        reverse(arr.begin(),arr.end());
        return arr;
        
    }
};