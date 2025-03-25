class Solution {
public:
    bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
        int m = rectangles.size();
        vector<tuple<int,int>> xdim;
        vector<tuple<int,int>> ydim;
        

        for (const auto &rectangle: rectangles){
            auto xs = rectangle[0];
            auto ys = rectangle[1];
            auto xe = rectangle[2];
            auto ye = rectangle[3];
            xdim.push_back({xs,xe});
            ydim.push_back({ys,ye});
        }
        sort(xdim.begin(),xdim.end());
        sort(ydim.begin(),ydim.end());

        int count = 0;
        int end = get<1>(xdim[0]);
        for (int i = 1 ; i < m; ++i){
            if (get<0>(xdim[i]) >= end) ++count;
            end = max(end, get<1>(xdim[i]));
        }
        if (count > 1) return true;

        count = 0;
        end = get<1>(ydim[0]);
        for (int i = 1 ; i < m; ++i){
            if (get<0>(ydim[i]) >= end) ++count;
            end = max(end, get<1>(ydim[i]));
        }
        if (count > 1) return true;


        return false;
        
    }
};