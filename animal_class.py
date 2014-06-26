import random
class Animal:
    """Animals on a field"""

    def __init__(self, growth_rate, water_need, food_need):
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Generic"
        self._name = "Not named"
        
    def needs(self):
        return {'food need':self._food_need, 'water need':self._water_need}
    
    def report(self):
        return {'name':self._name, 'type':self._type, 'status':self._status, 'days growing':self._days_growing, 'weight':self._weight}

    def _update_status(self):
        if self._weight > 12:
            self._status = "Fully grown"
        elif self._weight > 8:
            self._status = "Mature"
        elif self._weight > 4:
            self._status = "Medium"
        elif self._weight > 2:
            self._status = "Small"
        elif self._weight == 0:
            self._status = "Baby"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()

def manual_grow(animal):
    valid = False
    while not valid:
        try:
            food = int(input('Please enter a food value 1 - 10: '))
            if 1 <= food <= 10:
                valid = True
            else:
                print('Value entered not valid')
        except ValueError:
            print('Value entered not valid')                
    valid = False
    while not valid:
        try:
            water = int(input('Please enter a water value 1 - 10: '))
            if 1 <= water <= 10:
                valid = True
            else:
                print('Value entered not valid')
        except ValueError:
            print('Value entered not valid')
    animal.grow(food,water)
    
def auto_grow(animal, days):
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

        
def display_menu():
    print('1. Grow animal manually over 1 day')
    print('2. Grow animal automatically over 30 days')
    print("3. Report animal's status")
    print('0. Exit test program')
    print()
    print('Please select an option from the menu')
    
def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input('Option selection: '))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print('Please enter a valid option')
        except ValueError:
            print('Please enter a valid option')
    return choice

def manage_animal(animal):
    print('This is the animal management program')
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print('Thank you for using the crop management program')   
                
def main():
    new_animal = Animal(1,5,8)
    manage_animal(new_animal)


if __name__ == "__main__" :
    main()
        
