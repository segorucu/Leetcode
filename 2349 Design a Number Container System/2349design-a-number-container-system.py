from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.indextonum = collections.defaultdict(int)
        self.numtoindex = collections.defaultdict(SortedList)
        

    def change(self, index: int, number: int) -> None:
        if self.indextonum[index] == number:
            return
        elif self.indextonum[index] == 0:
            self.indextonum[index] = number
            self.numtoindex[number].add(index)
        else:
            prev = self.indextonum[index]
            self.numtoindex[prev].remove(index)
            self.numtoindex[number].add(index)
            self.indextonum[index] = number
        

    def find(self, number: int) -> int:
        if len(self.numtoindex[number]) > 0 and self.numtoindex[number][0] > 0:
            return self.numtoindex[number][0]
        else:
            return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)