class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        ans = 0
        m = len(arr1)
        n = len(arr2)
        
        vis1 = set()
        for a in arr1:
            while a > 0:
                vis1.add(a)
                a = a // 10
                
        vis2 = set()
        for a in arr2:
            while a > 0:
                vis2.add(a)
                a = a // 10
                
          
        for a in vis2:
            if a > ans and a in vis1:
                ans = a
                
                
        c = 0
        while ans > 0:
            c += 1
            ans = ans // 10
            
        return c
            