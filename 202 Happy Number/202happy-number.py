class Solution:
    def isHappy(self, n: int) -> bool:
        
        def do(k):
            sm = 0
            while k > 0:
                k, rem = divmod(k,10)
                sm = sm + rem**2
            return sm

        visited = set()
        visited.add(n)
        while n != 1:
            n = do(n)
            if n in visited:
                return False
            visited.add(n)

        return True