class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        elif n == m * k:
            return max(bloomDay)

        mp = []
        for i, a in enumerate(bloomDay):
            mp.append((a,i))
        mp.sort()

        if k == 1:
            return mp[m-1][0]

        def check(mid):
            cutoff = mp[mid][0]
            count = 0
            j = 0
            for i in range(n):
                if bloomDay[i] <= cutoff:
                    j += 1
                else:
                    j = 0
                if j == k:
                    j = 0
                    count += 1
            return count



        left = m*k-1
        right = n-1
        while left <= right:
            mid = (left+right) // 2
            if check(mid) >= m:
                right = mid - 1
            else:
                left = mid + 1
        
        return mp[left][0]
        