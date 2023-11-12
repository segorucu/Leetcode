class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        candidates = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            vi = nums[i]
            for j in range(i+1,n):
                vj = nums[j]
                if vj - vi <= vi:
                    candidates.append((vi,vj))
                else:
                    break
                    
        if len(candidates) == 0:
            return 0
        
        maxxor = 0
        for vi, vj in candidates:
            xor = 0
            mult = 1
            while vi > 0 or vj > 0:
                remi = vi % 2
                remj = vj % 2
                if remi != remj:
                    xor += mult
                vi = vi // 2
                vj = vj // 2
                mult *= 2
            if xor > maxxor:
                maxxor = xor
        return maxxor
            
                    
                
        