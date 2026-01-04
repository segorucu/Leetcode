class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        # print(counter)
        ans = 0
        for num, count in counter.items():
            n = math.ceil(pow(num,0.5))
            divisors = {1, num}
            for i in range(2,n+1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
            if len(divisors) == 4:
                ans += sum(divisors) * count

        return ans