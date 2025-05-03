class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        occurences = defaultdict(set)
        for i, (top,bottom) in enumerate(zip(tops,bottoms)):
            occurences[top].add(i)
            occurences[bottom].add(i)

        options = set()
        n = len(tops)
        for k,v in occurences.items():
            if len(v) == n:
                options.add(k)
                break

        if len(options) == 0:
            return -1

        ans = n
        for opt in options:
            one = n
            for top in tops:
                if top == opt:
                    one -= 1
            two = n
            for bottom in bottoms:
                if bottom == opt:
                    two -= 1
            ans = min(ans,one,two)

        return ans