# File name:    Exercise4_2.py
# Author:       Eerik Vainio
# Description:  3 classes for: Item, Suitcase and CargoHold.
#               Item can output their name and weight. Suitcase can
#               be filled with items until a max weight is reached,
#               and the items inside a suitcase can be accessed.
#               CargoHold works similarly to suitcases, but instead
#               of items, they hold suitcases. Items can be accessed
#               from CargoHold through suitcases.

class Item:
    def __init__(self, item_name: str, item_weight: int):
        self._name = item_name
        self._weight = item_weight

    def __str__(self):
        return f'{self._name} ({self._weight} g)'
    
    @property
    def name(self):
        return self._name
    
    @property
    def weight(self):
        return self._weight
    
    @name.setter
    def name(self, new_name):
        raise AttributeError("Unable to set value for 'name'")

    @weight.setter
    def weight(self, new_weight):
        raise AttributeError("Unable to set value for 'weight'")

class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.item_list = []
        self.total_weight = 0

    def __str__(self):
        if len(self.item_list) == 1:
            return (f'{len(self.item_list)} item ({self.total_weight} g)')
        else:
            return (f'{len(self.item_list)} items ({self.total_weight} g)')

    def add_item(self, new_item):
        if new_item.weight < (self.max_weight - self.total_weight):
            self.item_list.append(new_item)
            self.total_weight += new_item.weight

    def print_items(self):
        for x in self.item_list:
            print(x)

    def weight(self):
        return self.total_weight
    
    def heaviest_item(self):
        heaviest = None
        for x in self.item_list:
            if (heaviest == None or x.weight > heaviest.weight):
                heaviest = x

        return heaviest
    
class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight * 1000
        self.suitcase_list = []
        self.total_weight = 0
    
    def __str__(self):
        return (f'{len(self.suitcase_list)} suitcases, space for {int(self.max_weight / 1000)} kg')
    
    def add_suitcase(self, new_suitcase):
        if new_suitcase.total_weight < (self.max_weight - self.total_weight):
            self.suitcase_list.append(new_suitcase)
            self.total_weight += new_suitcase.total_weight
        
    def print_items(self):
        for x in self.suitcase_list:
            for y in x.item_list:
                print(y)


# Part 1
'''book = Item("ABC Book", 200)
phone = Item("Nokia 3210", 100)
print("Name of the book:", book.name)
print("Weight of the book:", book.weight)
print("Book:", book)
print("Phone:", phone)'''

'''book=Item("ABC Book",200)
book.weight=100
print(book.weight)'''

# Part 2
'''book=Item("ABC Book",200)
phone=Item("Nokia 3210",100)
brick=Item("Brick",400)
suitcase=Suitcase(500)
print(suitcase)
suitcase.add_item(book)
print(suitcase)
suitcase.add_item(phone)
print(suitcase)
suitcase.add_item(brick)
print(suitcase)'''

# Part 4
'''book=Item("ABC Book",200)
phone=Item("Nokia 3210",100)
brick=Item("Brick",400)
suitcase=Suitcase(1000)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)
print("The suitcase contains the following items:")
suitcase.print_items()
combined_weight=suitcase.weight()
print(f"Combined weight: {combined_weight} g")'''

# Part 5
'''book=Item("ABC Book",200)
phone=Item("Nokia 3210",100)
brick=Item("Brick",400)
suitcase=Suitcase(1000)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)
heaviest=suitcase.heaviest_item()
print(f"The heaviest item: {heaviest}")'''

# Part 6
'''cargo_hold=CargoHold(100)
print(cargo_hold)
book=Item("ABC Book",200)
phone=Item("Nokia 3210",100)
brick=Item("Brick",400)
adas_suitcase=Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)
peters_suitcase=Suitcase(1000)
peters_suitcase.add_item(brick)
cargo_hold.add_suitcase(adas_suitcase)
print(cargo_hold)
cargo_hold.add_suitcase(peters_suitcase)
print(cargo_hold)'''

# Part 7
book=Item("ABC Book",200)
phone=Item("Nokia 3210",100)
brick=Item("Brick",400)
adas_suitcase=Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)
peters_suitcase=Suitcase(1000)
peters_suitcase.add_item(brick)
cargo_hold=CargoHold(100)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)
print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()