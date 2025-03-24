class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        int lastdate = 0;
        int total = 0;

        sort(meetings.begin(), meetings.end(), [](const vector<int>& a, const vector<int>& b) {
            return tie(a[0], a[1]) < tie(b[0], b[1]);
    });
        total = meetings[0][0] - 1;
        lastdate = meetings[0][1];
        for (int i = 1; i < meetings.size(); ++i){
            int beg = meetings[i][0];
            int end = meetings[i][1];
            if (beg > lastdate + 1) {
                total += beg - lastdate - 1;
            }
            lastdate = max(lastdate, end);
        }
        if (days > lastdate) total += days - lastdate;


        return total;
    }
};