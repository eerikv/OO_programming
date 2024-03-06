# File name:    Exercise3_8.py
# Author:       Eerik Vainio
# Description:  User can create a recording, and set or get its
#               length.

class Recording:
    def __init__(self, __length: int):
        self.__length = __length

    # Getter method for __length
    @property
    def length(self):
        return self.__length
    
    # Setter method for __length
    @length.setter
    def length(self, l):
        self.__length = l

the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)
