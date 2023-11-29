class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        n = len(s)
        ans = []
        def backtrack(start,curr):
            if len(curr) == 4:
                char = curr[-1] + s[start:]
                val = int(char)
                if len(char) > 1 and char[0] == "0":
                    return
                if val > 255:
                    return
                curr[-1] = char
                ip = '.'.join(curr[:])
                ans.append(ip)
                return

            if start == n:
                return
            
            char = s[start]
            if start == 0:
                curr.append(char)
                backtrack(start+1,curr)
                return
            
            last = curr[-1]
            if last[0] == "0":
                curr.append(char)
                backtrack(start+1,curr)
                curr.pop()
                return
            else:
                val = int(last+char)
                if val > 255:
                    curr.append(char)
                    backtrack(start+1,curr)
                    curr.pop()
                    return

            curr[-1] = last + char
            backtrack(start+1,curr)
            curr[-1] = last
            curr.append(char)
            backtrack(start+1,curr)
            curr.pop()
            return
        
        backtrack(0,[])
        return ans
        