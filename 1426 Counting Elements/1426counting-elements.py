class Solution:
    def countElements(self, arr: List[int]) -> int:
        dct = {}
        for i in arr:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
          
        sm = 0
        for key, val in dct.items():
            if key+1 in dct:
                sm += val
         
        return sm
        