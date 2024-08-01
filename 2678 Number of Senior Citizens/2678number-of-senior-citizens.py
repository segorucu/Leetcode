class Solution:
    def countSeniors(self, details: List[str]) -> int:

        ans = 0
        for person in details:
            age = int(person[-4:-2])
            if age > 60:
                ans += 1

        return ans
        