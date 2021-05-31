class Hybrid_Car(object):
    def __init__(self, make, manufacturer, year, efficiency, price):
        self.make = make
        self.manufacturer = manufacturer
        self.year = year
        self.efficiency = efficiency
        self.price = price

    # Changing the information printed for a given object
    def __str__(self):
        return "{} {}, {} {} mpg, {} CAD".format(self.manufacturer, self.make, self.year, self.efficiency, self.price)

    def __repr__(self):
        return "{} {}, {} {} mpg, {} CAD".format(self.manufacturer, self.make, self.year, self.efficiency, self.price)

    # Overloading the comparison operators depending on the desired metric to compare
    def __lt__(self, other):
        return self.efficiency < other.efficiency

    def __le__(self, other):
        return self.efficiency <= other.efficiency

    def __gt__(self, other):
        return self.efficiency > other.efficiency

    def __ge__(self, other):
        return self.efficiency >= other.efficiency

    def __ne__(self, other):
        return self.efficiency != other.efficiency

    def __eq__(self, other):
        return self.efficiency == other.efficiency




