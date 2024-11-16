class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        data = collections.defaultdict(list)
        for user, time, site in zip(username, timestamp, website):
            data[user].append((time,site))
        

        for key, val in list(data.items()):
            if len(val) < 3:
                del data[key]
            else:
                data[key].sort()
        # print(data)
        
        freq = collections.defaultdict(set)
        def backtrack(user,i,lst):
            if i == len(data[user]):
                return
            lst.append(data[user][i][1])
            if len(lst) == 3:
                freq[tuple(lst)].add(user)
            else:
                backtrack(user,i+1,lst)
            lst.pop()
            backtrack(user,i+1,lst)


        for user in data.keys():
            backtrack(user,0,[])

        maxval = 0
        for key, val in freq.items():
            maxval = max(maxval,len(val))

        ans = []
        for key,val in freq.items():
            if len(val) == maxval:
                ans.append(key)

        ans.sort()
        # print(ans)
        return ans[0]

