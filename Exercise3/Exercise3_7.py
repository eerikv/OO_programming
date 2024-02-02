# File name:    Exercise3_7.py
# Author:       Eerik Vainio
# Description:  User can create persons and add them to the room. User can check
#               various information about the room, and remove the shortest
#               person in the room.

class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.shortest_person = None

class Room:
    def __init__(self):
        self.list_of_persons = []
        self.total_height = 0

    def add(self, person: Person):
        self.list_of_persons.append(person)
        self.total_height += person.height
        shortest_height = None
        for person in self.list_of_persons:
            if (shortest_height == None or person.height < shortest_height):
                shortest_height = person.height
                self.shortest_person = person

    def is_empty(self):
        if (len(self.list_of_persons) == 0):
            return True
        else:
            return False
        
    def print_contents(self):
        print(f'There are {len(self.list_of_persons)} persons in the room, and their combined height is {self.total_height} cm.')
        for person in self.list_of_persons:
            print(f'{person.name} ({person.height} cm)')
    
    def shortest(self):
        return self.shortest_person.name
    
    def remove_shortest(self):
        self.list_of_persons.remove(self.shortest_person)
        self.total_height -= self.shortest_person.height
        return self.shortest_person



room = Room()
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 175))

removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")
print()
11
room.print_contents()

