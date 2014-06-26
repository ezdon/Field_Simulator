from animal_class import *

class Sheep(Animal):
    """A Sheep animal"""
    
    def __init__(self, name):
        super().__init__(2,4,5)
        self._type = "Sheep"
        self._name = name


    def grow(self,food,water):
        if food >= self._water_need and water >= self._water_need:
            if self._status == "Baby" or self._status == "Small":
                self._weight += self._growth_rate * 1.8
            elif self._status == "Medium":
                self._weight += self._growth_rate * 1.6
            elif self._status == "Mature":
                self._weight += self._growth_rate * 1.2
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()


def main():
    sheep_animal = Sheep()
    print(sheep_animal.report())
    manual_grow(sheep_animal)
    print(sheep_animal.report())
    manual_grow(sheep_animal)
    print(sheep_animal.report())
if __name__ == "__main__":
    main()        
