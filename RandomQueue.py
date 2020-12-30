import numpy as np
import random 
from ArrayQueue import ArrayQueue

class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> np.object :
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        try:
            # if the array is empty raise an exception
            if self.n == 0:
                raise IndexError()
            # generate random index between 0 and n-1
            randomIndex = random.randint(0, self.n-1)
            # Swap first element in array with element at the randomIndex
            self.a[(self.j + randomIndex) % len(self.a)], self.a[self.j] \
            = self.a[self.j], self.a[(self.j + randomIndex) % len(self.a)]
            # Remove first element in queue
            return super().remove()
        except IndexError:
            print('Index out of range!')
     




