class CombinationIterator:


    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.len = combinationLength
        self.curr = 0
        self.arr = []
        def recurse(i, curr):
            if len(curr) == self.len:
                self.arr.append(curr)
                return

            if i == len(self.characters):
                return

            curr += self.characters[i]
            recurse(i+1,curr)
            curr = curr[0:-1]
            recurse(i+1,curr)

        recurse(0,"")        

    def next(self) -> str:
        tmp = self.arr[self.curr]
        self.curr += 1
        return tmp

        
    def hasNext(self) -> bool:
        if self.curr == len(self.arr):
            return False
        return True
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()