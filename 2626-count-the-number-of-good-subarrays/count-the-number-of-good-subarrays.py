class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        l = 0
        r = 0
        n = len(nums)
        counter = Counter()            
        ans = 0
        pairs = 0
        while r < n:
            counter[nums[r]] += 1
            pairs += (counter[nums[r]] - 1)
            if pairs < k:
                r += 1
            else:
                newpairs = pairs - counter[nums[l]] + 1
                # print(newpairs, k)
                while newpairs >= k:
                    pairs = newpairs
                    counter[nums[l]] -= 1
                    l += 1
                    newpairs = pairs - counter[nums[l]] + 1
                    
                ans += l+1
                r += 1

        return ans

        # nums = [3,1,4,3,2,2,4], k = 2
        # l = 2
        # r = 6
        # n = 7
        # ans = 0
        # pairs = 2
        # newpairs = 2
        # counter = [3: 1, 4: 2, 2: 2]
        # ans 1