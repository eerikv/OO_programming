# File name:    Exercise4_3.py
# Author:       Eerik Vainio
# Description:  A class for LaptopComputer which inherits a
#               Computer class. The computer can be assigned
#               a model and speed, and the laptop can additionally
#               be assigned a weight.

class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed
    
class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight):
        super().__init__(model, speed)
        self.weight = weight

    def __str__(self):
        return (f'{self.model}, {self.speed} MHz, {self.weight} kg')
    
laptop=LaptopComputer("NoteBook Pro15",1500,2)
print(laptop)