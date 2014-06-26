from animal_class import *

class Cow(Animal):
    """A Sheep animal"""
    
    def __init__(self, name):
        super().__init__(2,4,5)
        self._type = "Cow"
        self._name = name


    def grow(self,food,water):
        if food >= self._water_need and water >= self._water_need:
            if self._status == "Baby" or self._status == "Small":
                self._weight += self._growth_rate * 0.6
            elif self._status == "Medium":
                self._weight += self._growth_rate * 0.4
            elif self._status == "Mature":
                self._weight += self._growth_rate * 0.5
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()


def main():
    cow_animal = Cow()
    print(cow_animal.report())
    manual_grow(cow_animal)
    print(cow_animal.report())
    manual_grow(cow_animal)
    print(cow_animal.report())
if __name__ == "__main__":
    main()        
