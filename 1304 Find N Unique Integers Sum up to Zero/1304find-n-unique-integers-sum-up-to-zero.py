class Solution:
    def sumZero(self, n: int) -> List[int]:
        rem = n % 2
        w = n // 2
        ans = []
        for i in range(-w,0,1):
            ans.append(i)
        if rem == 1:
            ans.append(0)
        for i in range(1,w+1,1):
            ans.append(i)

        return ans
        