class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {

        int ans = 0;
        int prev = -1;
        int n = colors.size();
        for (int i = 0; i < n+k-1; ++i) {
            if (prev < 0) prev = 1;
            else {
                if (colors[i%n] != colors[(i-1)%n]) {
                    ++prev; 
                }
                else {
                    if (prev >= k) ans += prev - k + 1;
                    prev = 1;
                }
            }   
        }
        if (prev - k >= 0) ans += prev - k + 1;

        return ans;
        
    }
};