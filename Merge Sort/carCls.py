class Hybrid_Car(object):
    def __init__(self, make, manufacturer, year, efficiency, price):
        self.make = make
        self.manufacturer = manufacturer
        self.year = year
        self.efficiency = efficiency
        self.price = price

    # Changing the information printed for a given object
    def __str__(self):
        return "{} {}, {} {}, CAD".format(self.manufacturer, self.make, self.year, self.price)

    # Overloading the comparison operators depending on the desired metric to compare




