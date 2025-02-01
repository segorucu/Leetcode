class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        counter = {}
        for i in range(k):
            if nums[i] in counter:
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1

        ans = []
        for i in range(k,n):
            ans.append(len(counter.keys()))
            key = nums[i-k]
            counter[key] -= 1
            if counter[key] == 0:
                del counter[key]
            key = nums[i]
            if key in counter:
                counter[key] += 1
            else:
                counter[key] = 1
        ans.append(len(counter.keys()))

        return ans

