import numpy as np
from carCls import Hybrid_Car
from sort import MergeSort


# (Algorithm)
# In merge sort, an array is recursively divieded into two until a single element in reached, moving up from the single element back to the main array, the elements are sorted and merged togehter
# using the "two finger method" (i.e. elements from the left and right sorted arrays are individually compared against one another).

# (Complexity)
# Dividing an array of size n down to its individual elements require O(lg[n]) work done.
# At each level moving up the tree from the leaves, the total number of comparisons per node increases, but the total number of node decreases
# The total number of leaves at of the tree is n at the bottom layer. As we progress up the tree, the number of nodes decreases by 1/2.
# This means that the total number of nodes decreases from n -> n/2 -> n/4 -> n/8 -> n/16 -> ... -> 1
# Each layer moving up the tree, the total work required to merge the elements of each layer is n in total (with the first layer being the sorted layer).
# The complexity of merging the elements will then be O(n) * O(lg[n]) => (Total # of merges performed per layer) * (Total # of layers)
# The complesity of merge sort will then be O(n) + O(n*lg[n]) which results in O(n*lg[n]) worst case.

# (Auxiliary memory)
# At each level, merge sort requires n auxiliary space to store the sorted sub-arrays

# (Code)
# Will attempt to implement a merge sort on class objects
# The class objects should have their comparison operators overloaded to reflect the criteria they would like to have compared.
# For this exercise, I will instantiate class objects that store the "mpg" values of different hybird cars available in the market (as of 2021) and attempt to sort them according to their fuel efficiency

# Instantiating a list to store the various car objects
carLst = []

# Start appending cars
carLst.append(Hybrid_Car("LC 500h", "Lexus", 2020, 30, 98485))
carLst.append(Hybrid_Car("745e xDrive iPerformance", "BMW", 2020, 22, 96545))
carLst.append(Hybrid_Car("ES 300h", "Lexus", 2020, 44, 42785))
carLst.append(Hybrid_Car("Prius", "Toyota", 2020, 56, 25155))
carLst.append(Hybrid_Car("Ioniq", "Hyundai", 2020, 57, 24175))
carLst.append(Hybrid_Car("Avalon Hybird", "Toyota", 2020, 44, 37805))
carLst.append(Hybrid_Car("Accord Hybird", "Honda", 2020, 48, 26400))
carLst.append(Hybrid_Car("Camry Hybird", "Toyota", 2020, 52, 29205))
carLst.append(Hybrid_Car("Insight", "Honda", 2020, 52, 23860))

# Prompt the user to select a parameter to compare

variant = None

while variant == None:
    variant = input("Parameter to sort : [P] Price or [mpg] Miles Per Gallon :")

    if variant != "P" and variant != "mpg":
        print("Invalid selection, please enter \"P\" for price or \"mpg\" for miles per gallon")
        variant = None

# Perform the merge sort based on the criteria selected
sortedLst = MergeSort(unsortedList=carLst,parameters=variant)

for car in sortedLst:
    print(car)
    