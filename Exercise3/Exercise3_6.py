# File name:    Exercise3_6.py
# Author:       Eerik Vainio
# Description:  Lets user create presents, and add them to a box.
#               User can query for the weight of all the presents in the box.

# Present class for individual presents. Presents have a name and weight.
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name} ({self.weight})'

# Box class for a box of presents. Can output the total weight.
class Box:
    def __init__(self):
        self.weight = 0

    def add_present(self, present: Present):
        self.weight += present.weight
        
    def total_weight(self):
        return self.weight


book = Present("Ta-Nehisi Coates: The Water Dancer", 200)
box = Box()
box.add_present(book)
print(box.total_weight())
cd = Present("Pink Floyd: Dark Side of the Moon", 50)
box.add_present(cd)
print(box.total_weight())