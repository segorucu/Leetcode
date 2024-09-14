class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        ans = []
        def recurse(curr,i):
            if i == n:
                ans.append(curr)
                return

            if not curr or (curr and curr[-1] == "1"):
                recurse(curr+"0",i+1)
            recurse(curr+"1",i+1)
        
        recurse("",0)
        return ans