import random

class Code:

    def __init__(self):
        self.random_num = random.randint(1000, 9999)

    def get_random_num(self):
        #print(self.random_num)
        return str(self.random_num)


