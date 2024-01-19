# File name:    Exercise2_9.py
# Author:       Eerik Vainio
# Description:  A class Pet, and a function that can be called to create an
#               instance of that class.

class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

# Returns a new instance of the Pet object
def new_pet(name: str, species: str, year_of_birth: int):
    return Pet(name, species, year_of_birth)

fluffy = new_pet("Fluffy", "dog", 2017)
print(fluffy.name)
print(fluffy.species)
print(fluffy.year_of_birth)