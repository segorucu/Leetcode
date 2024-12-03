class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        m = len(s)
        ans = []
        prev = 0
        for i in spaces:
            curr = s[prev:i]
            ans.append(curr)
            prev = i
        curr = s[prev:m]
        ans.append(curr)
        # print(ans)

        return (" ").join(ans)