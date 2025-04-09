class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        


        s = list(s)
        ans = []
        def recurse(i):
            if i == len(s):
                ans.append("".join(s))
                return

            if s[i].isdigit():
                recurse(i+1)
            else:
                s[i] = s[i].lower()
                recurse(i+1)
                s[i] = s[i].upper()
                recurse(i+1)

        recurse(0)
        
        return ans

