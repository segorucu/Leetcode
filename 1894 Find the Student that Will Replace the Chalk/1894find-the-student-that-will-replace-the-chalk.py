class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        

        sm = sum(chalk)
        k = k % sm

        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]

        
