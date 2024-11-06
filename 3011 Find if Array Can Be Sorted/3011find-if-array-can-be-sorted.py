class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        mp = {}
        union = 0
        unionlist = []
        for ind, num in enumerate(nums):
            i = 0
            while num > 0:
                if num % 2 == 1:
                    i += 1
                num = num >> 1
            if i in mp:
                unionlist.append(mp[i])
            else:
                union += 1
                unionlist.append(union)
                mp[i] = union
                
        n = len(nums)
        for it in range(n):
            issorted = True
            for i in range(1,n):
                if nums[i] < nums[i-1]:
                    issorted = False
                    if unionlist[i] == unionlist[i-1]:
                        nums[i], nums[i-1] = nums[i-1], nums[i]
                    else:
                        return False
            if issorted:
                break
        return issorted
            
        
        
        return True