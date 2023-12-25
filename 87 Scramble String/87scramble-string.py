from functools import cache
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        @cache
        def valid(s1,s2):
            return sorted(s1) == sorted(s2)

        @cache
        def backtrack(s1,s2):

            if len(s1) == 1:
                return s1 == s2

            for i in range(1,len(s1)):
                if valid(s1[:i], s2[:i]):
                    left = backtrack(s1[:i],s2[:i])
                    right = backtrack(s1[i:],s2[i:])
                    if left and right:
                        return True
                if valid(s1[:i], s2[-i:]):
                    left = backtrack(s1[:i],s2[-i:])
                    right = backtrack(s1[i:],s2[:-i])
                    if left and right:
                        return True
            return  False


        return backtrack(s1,s2)