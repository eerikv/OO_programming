# File name:    Exercise4_4.py
# Author:       Eerik Vainio
# Description:  Classes for ComputerGame, GameWarehouse and GameMuseum.
#               ComputerGame has a name, published and year. GameWarehouse
#               can contain games, and GameMuseum inherits GameWarehouse,
#               but only contains games released before 1990.

class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games
    
class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        new_list = []
        for x in self._GameWarehouse__games:
            if (x.year < 1990):
                new_list.append(x)
        
        return new_list

museum=GameMuseum()
museum.add_game(ComputerGame("Pacman","Namco",1980))
museum.add_game(ComputerGame("GTA 2","Rockstar",1999))
museum.add_game(ComputerGame("Bubble Bobble","Taito",1986))
for game in museum.list_games():
    print(game.name)
