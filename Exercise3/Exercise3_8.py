# File name:    Exercise3_8.py
# Author:       Eerik Vainio
# Description:  User can create a recording, and set or get its
#               length.

class Recording:
    def __init__(self, _length: int):
        self._length = _length

    # Getter method for _length
    @property
    def length(self):
        return self._length
    
    # Setter method for _length
    @length.setter
    def length(self, l):
        self._length = l

the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)
