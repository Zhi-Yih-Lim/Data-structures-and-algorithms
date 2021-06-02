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

    if self.mode == 'mpg':
        # Depending on the selection made, overload the comparison operators accordingly
        def __le__(self,other):
            return self.mpg <= other.mpg

        def __lt__(self,other):
            return self.mpg < other.mpg

        def __gt__(self,other):
            return self.mpg > other.mpg

        def __ge__(self,other):
            return self.mpg >= other.mpg

        def __ne__(self,other):
            return self.mpg != other.mpg

        def __eq__(self,other):
            return self.mpg == other.mpg
    
    elif self.mode == 'price':

        def __le__(self,other):
            return self.price <= other.price

        def __lt__(self,other):
            return self.price < other.price

        def __gt__(self,other):
            return self.price > other.price

        def __ge__(self,other):
            return self.price >= other.price

        def __ne__(self,other):
            return self.price != other.price

        def __eq__(self,other):
            return self.price == other.price

    # Define a class method to set the right left and parent pointers for the current node
    def set_leftC(self,leftPntr):
        self.leftC = leftPntr

    def set_rightC(self,rightPntr):
        self.rightC = rightPntr

    def set_parent(self,parentPntr):
        self.parent = parentPntr
