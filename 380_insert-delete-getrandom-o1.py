import random


# I had misread the question at first. I thought the question asked me to randomise so that all numbers come up exactly the same number of times.
class RandomizedSet:

    def __init__(self):
        self.randomise = []
        self.val_index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.val_index_map:
            return False
        self.randomise.append(val)
        self.val_index_map[val] = len(self.randomise) - 1
        return True

    """
    Revision 2:
    I had the same idea about the question as my previous iterations when solving this question for the first time. Not about the interpretation of the randomise function but execution of it using pointer.
    I knew O(1) could be done by swapping but I imagined using pointers and checks. But this is a neat and simple trick.
    Why keep the last one at all when pop takes O(1) time.
    This is about the only thing which remained missing in my algo this time I tried to figure it out.
    I don't know how true it is but I feel like the Einstein who cut two doors for his cats. In view of the larger question I missed out on a detail so simple that I cut two doors when one larger could have suffised.
    """
    def remove(self, val: int) -> bool:
        if val not in self.val_index_map:
            return False
        index = self.val_index_map[val]
        self.val_index_map[self.randomise[-1]] = index
        self.randomise[-1], self.randomise[index] = self.randomise[index], self.randomise[-1]
        self.randomise.pop()
        del self.val_index_map[val]
        return True

    def getRandom(self) -> int:
        return self.randomise[random.randint(0, len(self.randomise) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.insert(10))
    print(obj.insert(20))
    print(obj.insert(30))
    print(obj.insert(40))
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())
