from sortedcontainers import SortedList

#https://leetcode.com/problems/design-a-food-rating-system/discuss/2324652/Python-with-Sorted-Set    ----- This solution has sorted it differently see this for a different approach
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.d=defaultdict(SortedList)
        self.foodie=defaultdict(list)
        for i in range(len(foods)):
            self.d[cuisines[i]].add([ratings[i],foods[i]])
            self.foodie[foods[i]]=[cuisines[i],ratings[i]]
    def changeRating(self, food: str, newRating: int) -> None:
        c,r=self.foodie[food]
        self.d[c].remove([r,food])
        self.d[c].add([newRating,food])
        self.foodie[food]=[c,newRating]
        #print(self.d)

    def highestRated(self, cuisine: str) -> str:
        m=self.d[cuisine][-1][0]
        for i in range(len(self.d[cuisine])-1,-1,-1):
            if self.d[cuisine][i][0]<m:
                return self.d[cuisine][i+1][1]
        if self.d[cuisine][0][0]==m:
            return self.d[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)