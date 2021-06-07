# File containing the object definitions for the node that will be used for the AVL trees.
class carNode(object):
    def __init__(self,make,manufacturer,year,mpg,price,mode):
        self.make=make
        self.manufacturer=manufacturer
        self.year=year
        self.mpg=mpg
        self.price=price
        self.mode = mode
        self.parent = None
        self.rightC = None
        self.leftC = None
        self.height = 0
    # Depending on the selection made, overload the comparison operators accordingly
    def __le__(self,other):
        if self.mode == 'mpg':
            return self.mpg <= other.mpg
        elif self.mode == 'price':
            return self.price <= other.price

    def __lt__(self,other):
        if self.mode == 'mpg':
            return self.mpg < other.mpg
        elif self.mode == 'price':
            return self.price < other.price
        
    def __gt__(self,other):
        if self.mode == 'mpg':
            return self.mpg > other.mpg
        elif self.mode == 'price':
            return self.price > other.price
    
    def __ge__(self,other):
        if self.mode == 'mpg':
            return self.mpg >= other.mpg
        elif self.mode == 'price':
            return self.price >= other.price

    def __repr__(self):
        return "{},{},{},{},{}".format(self.manufacturer,self.make,self.mpg,self.year,self.price)
    # Define a class method to set the right left and parent pointers for the current node
    def set_leftC(self,leftPntr):
        self.leftC = leftPntr

    def set_rightC(self,rightPntr):
        self.rightC = rightPntr

    def set_parent(self,parentPntr):
        self.parent = parentPntr
