from SLLQueue import SLLQueue
from DLList import DLList
import numpy as np

class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)

    def add(self, x : object)  :
        super().add(x)

    def remove(self) -> object:
        if self.n == 0:
            return None
        x = super().remove()
        return x

    def max(self):
        # Initialize max value at the head
        head = self.head
        if self.head is None:
            raise Exception()
        else:
            max_value = head.x
            # Go through every element of queue, and if the element is greater than current max, it
            # becomes the current max
            while head is not None:
                if head.x > max_value:
                    max_value = head.x
                head = head.next
        return max_value

    def getBestSelling(self):
        print(self.max())
