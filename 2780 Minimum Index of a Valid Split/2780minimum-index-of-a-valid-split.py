class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        counter = collections.Counter(nums)

        x = Counter(nums).most_common(1)[0][0]
        n = len(nums)
    
        prefix = n*[0]
        if nums[0] == x:
            prefix[0] = 1
        for i in range(1,n):
            num = nums[i]
            if num == x:
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]

        for i in range(0,n-1):
            leftlength = i + 1
            rightlength = n - leftlength
            if prefix[i] * 2 > leftlength and (prefix[-1] - prefix[i]) * 2 > rightlength:
                return i

        return -1