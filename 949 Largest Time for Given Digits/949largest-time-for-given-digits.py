class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:

        
        hour = -1
        currmx = -1
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for m in range(4):
                        if i != j and i != k and i != m and j != k and j != m and k != m:
                            candh = arr[i] * 10 + arr[j]
                            candm = arr[k] * 10 + arr[m]
                            if 0 <= candh <= 23 and 0 <= candm <= 59:
                                tot = candh * 60 +candm
                                if tot > currmx:
                                    # print(i,j,k,m)
                                    currmx = tot
                                    hour = candh
                                    minutes = candm
                                    # print(hour,minutes)
        
        if hour == -1:
            return ""

        if hour < 10:
            hour = "0" + str(hour)
        else:
            hour = str(hour)

        if minutes < 10:
            minutes = "0" + str(minutes)
        else:
            minutes = str(minutes)

        return hour + ":" + minutes
                    
        