class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        

        mp = defaultdict(set)
        for tri in allowed:
            mp[tri[0:2]].add(tri[-1])


        def permute(bottom):
            if len(bottom) == 1:
                return [""]
            
            ans = []
            nxt = permute(bottom[1:])
            for val in mp[bottom[0:2]]:
                for suffix in nxt:
                    curr = val + suffix
                    ans.append(curr)
            return ans


        permutations = permute(bottom)
                
        ans = [False]
        def backtrack(bottom):
            if len(bottom) == 1:
                return True

            permutations = permute(bottom)
            ans = False
            for option in permutations:
                ans = ans or backtrack(option)
            return ans

        return backtrack(bottom)

