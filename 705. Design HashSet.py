class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=[]
        

    def add(self, key: int) -> None:
        if key not in self.l:
            self.l.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.l:
            self.l.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.l:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)