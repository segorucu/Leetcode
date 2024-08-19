class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        n = len(energy)
        ans = -inf
        for i in range(1,k+1):
            curr = 0
            j = n-i
            while j >= 0:
                curr += energy[j]
                j -= k
                ans = max(ans, curr)

        return ans

        