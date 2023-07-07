class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        if n <= 1:
            return n
        
        # Mazimize true's
        left = ans = err = 0
        for right in range(n):
            if answerKey[right] == "F":
                err += 1
                while err > k:
                    if answerKey[left] == "F":
                        err -= 1
                    left += 1
            ans = max(ans,right-left+1)

        # Mazimize false's
        left = err = 0
        for right in range(n):
            if answerKey[right] == "T":
                err += 1
                while err > k:
                    if answerKey[left] == "T":
                        err -= 1
                    left += 1
            ans = max(ans,right-left+1)

        return ans


        

