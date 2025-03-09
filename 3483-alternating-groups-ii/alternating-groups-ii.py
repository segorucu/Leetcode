class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        

        ans = 0
        n = len(colors)
        prev = None
        for i in range(n+k-1):
            if not prev:
                prev = 1
            else:
                if colors[i%n] != colors[(i-1)%n]:
                    prev += 1
                else:
                    if prev >= k:
                        ans += prev - k + 1
                    prev = 1
            # print(i%n,prev)
        if prev >= k:
            ans += prev- k + 1

        return ans
