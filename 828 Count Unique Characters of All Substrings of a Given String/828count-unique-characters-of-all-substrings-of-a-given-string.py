class Solution:
    def uniqueLetterString(self, s: str) -> int:

        alphabet = set(s)
        n = len(s)
        locations = {}
        for letter in alphabet:
            locations[letter] = collections.deque([-1])

        ans = 0
        for i in range(n):
            curr = s[i]
            locations[curr].append(i)
            while len(locations[curr]) > 2:
                locations[curr].popleft()

            for letter in alphabet:
                if len(locations[letter]) == 2:
                    ans += (locations[letter][1] - locations[letter][0])

        return ans