from collections import defaultdict
import heapq
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = defaultdict(int)
        self.cuisines = defaultdict(list)
        self.n = len(foods)
        for food,cuisine,rating in zip(foods,cuisines,ratings):
            self.foods[food] = (cuisine,rating)
            heapq.heappush(self.cuisines[cuisine],(-rating,food)) 


    def changeRating(self, food: str, newRating: int) -> None:
        (cuisine,rating) = self.foods[food]
        self.foods[food] = (cuisine, newRating)
        heapq.heappush(self.cuisines[cuisine],(-newRating,food)) 
        # heapq.heapify(self.cuisines[cuisine])
        # print(self.cuisines[cuisine])
        
    def highestRated(self, cuisine: str) -> str:
        
        rat, food = self.cuisines[cuisine][0]
        rat *= -1
        while rat != self.foods[food][1]:
            heapq.heappop(self.cuisines[cuisine])
            rat, food = self.cuisines[cuisine][0]
            rat *= -1
        return self.cuisines[cuisine][0][1]

        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)