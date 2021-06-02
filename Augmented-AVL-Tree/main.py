# Using the similar car example outlined in "Merge Sort" code, but implmentation using Augemented AVL Trees to sort the vehicles instead of Merge Sort.
import numpy as np
from node import carNode

# Instantiate a set to store the different hybrid car objects
carSet = {}

# Start adding the cars
carSet.add(Hybrid_Car("LC 500h", "Lexus", 2020, 30, 98485))
carSet.add(Hybrid_Car("745e xDrive iPerformance", "BMW", 2020, 22, 96545))
carSet.add(Hybrid_Car("ES 300h", "Lexus", 2020, 44, 42785))
carSet.add(Hybrid_Car("Prius", "Toyota", 2020, 56, 25155))
carSet.add(Hybrid_Car("Ioniq", "Hyundai", 2020, 57, 24175))
carSet.add(Hybrid_Car("Avalon Hybird", "Toyota", 2020, 44, 37805))
carSet.add(Hybrid_Car("Accord Hybird", "Honda", 2020, 48, 26400))
carSet.add(Hybrid_Car("Camry Hybird", "Toyota", 2020, 52, 29205))
carSet.add(Hybrid_Car("Insight", "Honda", 2020, 52, 23860))

print(carSet)


