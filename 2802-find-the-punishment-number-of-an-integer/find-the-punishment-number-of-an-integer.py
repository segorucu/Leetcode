class Solution:
    def punishmentNumber(self, n: int) -> int:

        def backtrack(num,goal,arr,i):
            if i == len(num):
                arr.append(i)
                prev = 0
                sm = 0
                for end in arr:
                    if len(num[prev:end]):
                        sm += int(num[prev:end])
                    prev = end
                arr.pop()
                if sm == goal:
                    return True
                else:
                    return False
            arr.append(i)
            if backtrack(num,goal,arr,i+1):
                return True
            arr.pop()
            if backtrack(num,goal,arr,i+1):
                return True

        
        ans = 0
        for i in range(1,n+1):
            num = str(i**2)
            goal = i
            if backtrack(num,goal,[],1):
                ans += i**2

        return ans

