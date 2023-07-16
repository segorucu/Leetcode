from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads) <= 1:
            return len(roads)

        freq = defaultdict(list)
        adj = defaultdict(list)
        for a,b in roads:
            adj[a].append(b)
            adj[b].append(a)


        for i in range(n):
            freq[len(adj[i])].append(i)

        keylist = sorted(freq.keys())

        
        if len(freq[keylist[-1]]) == 1:
            for key in freq[keylist[-2]]:
                if freq[keylist[-1]][0] not in adj[key]:
                    return keylist[-1] + keylist[-2]
            else:
                return keylist[-1] + keylist[-2] -1
        else:
            for i in range(len(freq[keylist[-1]])):
                key1 = freq[keylist[-1]][i]
                for j in range(i+1,len(freq[keylist[-1]])):
                    key2 = freq[keylist[-1]][j]
                    if key1 not in adj[key2]:
                        return 2*keylist[-1]
            else:
                return 2*keylist[-1]-1

