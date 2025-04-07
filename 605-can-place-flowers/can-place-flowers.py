class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        add = 0
        N = len(flowerbed)
        for i,num in enumerate(flowerbed):
            leftcheck = False
            if i > 0:
                if flowerbed[i-1] == 0:
                    leftcheck = True
            else:
                leftcheck = True
            rightcheck = False
            if i == N-1:
                rightcheck = True
            else:
                if flowerbed[i+1] == 0:
                    rightcheck = True
                
            if leftcheck and rightcheck and flowerbed[i] == 0:
                flowerbed[i] = 1
                add += 1

        return add >= n