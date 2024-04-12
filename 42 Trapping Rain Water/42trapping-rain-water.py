class Solution:
    def trap(self, height: List[int]) -> int:

        height = [0] + height + [0]
        n = len(height)
        peaks = []
        for i in range(1,n-1):
            if height[i-1] <= height[i] and height[i] >= height[i+1]:
                peaks.append(i)

        if len(peaks) == 0:
            return 0
        p = 1
        contin = True
        while contin:
            contin = False
            p = 1
            while p < len(peaks)-1:
                if height[peaks[p]] <= height[peaks[p-1]] and height[peaks[p]] <= height[peaks[p+1]]:
                    peaks.pop(p)
                    contin = True
                else:
                    p += 1
            
        print(peaks)
        m = len(peaks)
        sm = 0
        for i in range(m-1):
            pre = peaks[i]
            nxt = peaks[i+1]
            hgt = min(height[pre],height[nxt])
            for j in range(pre+1,nxt):
                sm += max(0,hgt-height[j])

        return sm
        