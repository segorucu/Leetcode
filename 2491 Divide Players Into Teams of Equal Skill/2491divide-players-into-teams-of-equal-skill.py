class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        n = len(skill)
        half = n // 2
        sm = sum(skill)
        if sm % half != 0:
            return -1
        target = sm // half
        counter = {}

        ans = 0
        for i, val in enumerate(skill):
            search = target - val
            if search in counter:
                ans += (search * val)
                counter[search] -= 1
                if counter[search] == 0:
                    del counter[search]
            else:
                if val in counter:
                    counter[val] += 1
                else:
                    counter[val] = 1

        if len(counter) > 0:
            return -1
        return ans



        