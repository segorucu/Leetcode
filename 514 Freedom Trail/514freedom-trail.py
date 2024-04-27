from functools import cache
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        n = len(ring)

        @cache
        def goleft(currloc,goal):
            lefti = currloc
            left = 0
            while ring[lefti] != goal:
                lefti -= 1
                lefti = lefti % n
                left += 1
            return lefti, left

        @cache
        def goright(currloc,goal):
            righti = currloc
            right = 0
            while ring[righti] != goal:
                righti += 1
                righti = righti % n
                right += 1
            return righti, right

        @cache
        def backtrack(keyi,currloc):
            if keyi == len(key):
                return 0

            lefti, left = goleft(currloc,key[keyi])
            first = backtrack(keyi+1,lefti)
            righti, right = goright(currloc,key[keyi])
            second = backtrack(keyi+1,righti)
            return min(first+left,second+right)

        
        ans = backtrack(0,0)

        return ans + len(key)