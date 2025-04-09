class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        
        anywhere = ["0", "1", "8"]
        symmetric = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}

        if n % 2:
            starti = n // 2
        else:
            starti = n // 2 - 1

        minval = 10 ** (n-1)
        if n == 1:
            minval = 0
        maxval = 10 ** n
        
        ans = []
        def recurse(i):
            if i == -1:
                # print(curr)
                txt = "".join(curr)
                # print(minval, maxval, txt)
                if minval <= int(txt) < maxval:
                    ans.append(txt)
                return

            if n % 2 and i == n // 2:
                for k in anywhere:
                    curr[i] = k
                    recurse(i-1)
            else:
                for k,v in symmetric.items():
                    curr[i] = k
                    idiff = starti - i
                    if n % 2:
                        curr[starti+idiff] = v
                    else:
                        curr[starti+idiff+1] = v
                    recurse(i-1)

        curr = n*[None]
        recurse(starti)
        return ans

        