from heapq import heapify, heappop, heappush
class Solution:
    def minimizeStringValue(self, s: str) -> str:

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        freqs = collections.defaultdict(int)
        for a in alphabet:
            freqs[a] = 0
        s = list(s)
        tobefilled = []
        for i,a in enumerate(s):
            if a != "?":
                freqs[a] += 1
            else:
                tobefilled.append(i)

        m = len(tobefilled)
        stack = []
        for key,val in freqs.items():
            stack.append((val,key))
        heapify(stack)
        arr = []
        for i in range(m):
            fr, ch = heappop(stack)
            arr.append(ch)
            heappush(stack,(fr+1,ch))

        arr.sort()
        for i, ch in zip(tobefilled,arr):
            s[i] = ch
        
        return "".join(s)

        