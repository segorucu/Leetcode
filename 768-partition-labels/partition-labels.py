class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        

        lastoccurence = defaultdict(int)
        for i,a in enumerate(s):
            lastoccurence[a] = i

        size = 0
        end = 0
        ans = []
        for i,a in enumerate(s):
            size += 1
            end = max(end,lastoccurence[a])
            if i == end:
                ans.append(size)
                size = 0

        return ans
        