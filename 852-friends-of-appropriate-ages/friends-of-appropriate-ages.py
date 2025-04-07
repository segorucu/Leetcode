class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        # sort ages
        # append array on the go and do bisection to find minimum age
        # empty the array that was less than 100 at the age 101.

        # 16 16 16
        ages.sort()
        # print(ages)
        ans = 0
        for k,v in groupby(ages):
            if k > 0.5 * k + 7:
                cnt = len(list(v))
                if cnt > 1:
                    ans += cnt * (cnt-1) // 2

        queue = deque()
        k = 0
        for i, age in enumerate(ages):

            minage = age / 2 + 7
            ind = bisect_right(queue, minage)
            cnt = 0
            if ind < len(queue):
                if queue[ind] == minage:
                    # print("1", ind, queue, minage)
                    beg = ind + 1
                else:
                    # print("2", ind, queue, minage)
                    beg = ind
                cnt = max(0,k-beg)
            ans += cnt
            k += 1
            
            queue.append(age)


        return ans