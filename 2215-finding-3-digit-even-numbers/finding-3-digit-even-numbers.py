class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        digits.sort()
        digits = Counter(digits)
        keys = list(sorted(digits.keys()))
        for k,v in digits.items():
            digits[k] = min(v,3)

        ans = []
        curr = []
        def backtrack(i):
            if i == 3:
                val = ""
                for digit in curr:
                    val += str(digit)
                val = int(val)
                ans.append(val)
                return

            for k in keys:
                if i == 0 and k == 0:
                    continue
                if i == 2 and k % 2 == 1:
                    continue
                if digits[k] <= 0:
                    continue
                digits[k] -= 1
                curr.append(k)
                backtrack(i+1)
                curr.pop()
                digits[k] += 1

        backtrack(0)
        # ans = list(ans)
        # ans.sort()
        return ans
                    

            

