class MyCircularDeque:

    def __init__(self, k: int):
        self.elements = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        if len(self.elements) == self.size:
            return False
        
        self.elements.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.elements) == self.size:
            return False
        
        self.elements.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.elements) == 0:
            return False
        
        self.elements.pop(0)
        return True

    def deleteLast(self) -> bool:
        if len(self.elements) == 0:
            return False
        
        self.elements.pop()
        return True

    def getFront(self) -> int:
        if len(self.elements) == 0:
            return -1
        return self.elements[0]

    def getRear(self) -> int:
        if len(self.elements) == 0:
            return -1
        return self.elements[-1]

    def isEmpty(self) -> bool:
        return len(self.elements) == 0

    def isFull(self) -> bool:
        return len(self.elements) == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()