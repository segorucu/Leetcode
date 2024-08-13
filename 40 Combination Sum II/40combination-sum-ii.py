from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = Counter(candidates)
        n = len(candidates)
        ans = []
        def backtrack(sm, counter, curr, start):
            if sm == target:
                # curr = sorted(curr)
                # if curr not in ans:
                ans.append(curr[:])
                return
            if sm > target:
                return
            for i in range(start,len(counter)):
                cand = counter[i][0]
                if counter[i][1] > 0:
                    counter[i][1] -= 1
                    curr.append(cand)
                    backtrack(sm + cand, counter, curr, i)
                    counter[i][1] += 1
                    curr.pop()

        counter = [[c, counter[c]] for c in counter]
        backtrack(0, counter, [], 0)

        return ans
        