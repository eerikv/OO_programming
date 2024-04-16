# File name:    Exercise_work.py
# Author:       Eerik Vainio
# Description:  A workout tracker application.

import os
import pickle

# Workout classes
class Workout:
    def __init__(self):
        self.duration = self.date = self.distance = self.avgBpm = self.topBpm = '0'

    def __str__(self):
        return(f"{self.name : <15}{self.date[6:8]+'.'+self.date[4:6]+'.'+self.date[:4] : >15}{self.duration[:2]+'h '+self.duration[3:4]+'m '+self.duration[5:6]+'s' : >15}{self.distance+'m' : >15}{self.avgBpm : >15}{self.topBpm : >15}") 

    def SetDate(self, date):
        self.date = date.replace('-', '')

    def SetDuration(self, duration):
        self.duration = duration.replace('-', '')

    def SetDistance(self, distance):
        self.distance = distance

    def SetAvgBpm(self, bpm):
        self.avgBpm = bpm

    def SetTopBpm(self, bpm):
        self.topBpm = bpm

class Running(Workout):
    def __init__(self):
        super().__init__()
        self.name = 'Running'
    

class Cycling(Workout):
    def __init__(self):
        super().__init__()
        self.name = 'Cycling'

class Swimming(Workout):
    def __init__(self):
        super().__init__()
        self.name = 'Swimming'

class WeightTraining(Workout):
    def __init__(self):
        super().__init__()
        self.name = 'Weight Training'

class OtherWorkout(Workout):
    def __init__(self, name):
        super().__init__()
        self.name = name

class Workouts:
    def __init__(self):
        self.listOfWorkouts = []

    def ListWorkouts(self):
        os.system('cls')

        filterUserInput = None

        while filterUserInput == None:
            filterChoiceUserInput = input('Do you want to filter the list by workout type? (Y/N): ')
            if filterChoiceUserInput.casefold() == 'y':
                while True:
                    filterUserInput = input('Give a filtering keyword: ')
                    if len(filterUserInput) > 0 and filterUserInput.isalpha():
                        break
                    print(f'"{filterUserInput} is not a valid filtering keyword')
            elif filterChoiceUserInput.casefold() == 'n':
                break
            else:
                print(f'"{filterChoiceUserInput}" is not a valid command')

        os.system('cls')

        print('Select the ordering of the list\n')
        print('0: Date\n1: Duration\n2: Distance\n3: Average BPM\n4: top BPM\n\nQ: Go back to menu')

        while True:
            userInput = input('\nCommand: ')
            if userInput.isnumeric():
                if int(userInput) <= 4:
                    break
            elif userInput.casefold() == "q":
                break
            print(f'"{userInput}" is not a valid command')

        if userInput.casefold() != "q":
            os.system('cls')
            
            match(userInput):
                case('0'):
                    print('Selected ordering by: Date\n\nChoose sorting type:\n0: newest-oldest\n1: oldest-newest')
                case('1'):
                    print('Selected ordering by: Duration\n\nChoose sorting type:\n0: shortest-longest\n1: longest-shortest')
                case('2'):
                    print('Selected ordering by: Distance\n\nChoose sorting type:\n0: shortest-longest\n1: longest-shortest')
                case('3'):
                    print('Selected ordering by: Average BPM\n\nChoose sorting type:\n0: lowest-highest\n1: highest-lowest')
                case('4'):
                    print('Selected ordering by: Top BPM\n\nChoose sorting type:\n0: lowest-highest\n1: highest-lowest')

            while True:
                sortingUserInput = input('\nCommand: ')
                if sortingUserInput == '0' or sortingUserInput == '1':
                    break
                print(f'"{sortingUserInput}" is not a valid command')

            os.system('cls')

            match(userInput):
                case('0'):
                    self.ListWorkoutsDate(filterUserInput, bool(int(sortingUserInput)))
                case('1'):
                    self.ListWorkoutsDuration(filterUserInput, bool(int(sortingUserInput)))
                case('2'):
                    self.ListWorkoutsDistance(filterUserInput, bool(int(sortingUserInput)))
                case('3'):
                    self.ListWorkoutsAvgBpm(filterUserInput, bool(int(sortingUserInput)))
                case('4'):
                    self.ListWorkoutsTopBpm(filterUserInput, bool(int(sortingUserInput)))

            input('\nPress Enter to continue...')

    def ListWorkoutsDate(self, filter, descending):
        descending = not descending

        if descending:
            print(f"{'Name' : <15}{'Date v' : >15}{'Duration' : >15}{'Distance' : >15}{'Avg BPM' : >15}{'Top BPM' : >15}")
        else:
            print(f"{'Name' : <15}{'Date ^' : >15}{'Duration' : >15}{'Distance' : >15}{'Avg BPM' : >15}{'Top BPM' : >15}")

        newList = sorted(self.listOfWorkouts, key=lambda x: int(x.date), reverse=descending)
        for x in newList:
            if filter == None:
                print(x)
            else:
                if filter.casefold() in x.name.casefold():
                    print(x)

    def ListWorkoutsDuration(self, filter, descending):
        if descending:
            print(f"{'Name' : <15}{'Date' : >15}{'Duration v' : >15}{'Distance' : >15}{'Avg BPM' : >15}{'Top BPM' : >15}")
        else:
            print(f"{'Name' : <15}{'Date' : >15}{'Duration ^' : >15}{'Distance' : >15}{'Avg BPM' : >15}{'Top BPM' : >15}")

        newList = sorted(self.listOfWorkouts, key=lambda x: int(x.duration), reverse=descending)
        for x in newList:
            if filter == None:
                print(x)
            else:
                if filter.casefold() in x.name.casefold():
                    print(x)
    
    def ListWorkoutsDistance(self, filter, descending):
        if descending:
            print(f"{'Name' : <15}{'Date' : >15}{'Duration' : >15}{'Distance v' : >15}{'Avg BPM' : >15}{'Top BPM' : >15}")
        else:
            print(f"{'Name' : <15}{'Date' : >15}{'Duration' : >15}{'Distance ^' : >15}{'Avg BPM' : >15}{'Top BPM' : >15}")

        newList = sorted(self.listOfWorkouts, key=lambda x: int(x.distance), reverse=descending)
        for x in newList:
            if filter == None:
                print(x)
            else:
                if filter.casefold() in x.name.casefold():
                    print(x)

    def ListWorkoutsAvgBpm(self, filter, descending):
        if descending:
            print(f"{'Name' : <15}{'Date' : >15}{'Duration' : >15}{'Distance' : >15}{'Avg BPM v' : >15}{'Top BPM' : >15}")
        else:
            print(f"{'Name' : <15}{'Date' : >15}{'Duration' : >15}{'Distance' : >15}{'Avg BPM ^' : >15}{'Top BPM' : >15}")

        newList = sorted(self.listOfWorkouts, key=lambda x: int(x.avgBpm), reverse=descending)
        for x in newList:
            if filter == None:
                print(x)
            else:
                if filter.casefold() in x.name.casefold():
                    print(x)

    def ListWorkoutsTopBpm(self, filter, descending):
        if descending:
            print(f"{'Name' : <15}{'Date' : >15}{'Duration' : >15}{'Distance' : >15}{'Avg BPM' : >15}{'Top BPM v' : >15}")
        else:
            print(f"{'Name' : <15}{'Date' : >15}{'Duration' : >15}{'Distance' : >15}{'Avg BPM' : >15}{'Top BPM ^' : >15}")

        newList = sorted(self.listOfWorkouts, key=lambda x: int(x.topBpm), reverse=descending)
        for x in newList:
            if filter == None:
                print(x)
            else:
                if filter.casefold() in x.name.casefold():
                    print(x)

# Program functions
def AskDate():
    while True:
        date = input('Set the date of the workout (YYYY-MM-DD): ')
        if len(date) == 10:
            if date[:3].isnumeric() and date[4] == "-" and date[5:6].isnumeric() and date[7] == "-" and date[8:].isnumeric():
                if int(date[:4]) > 0 and int(date[:4]) <= 2024 and int(date[5:7]) > 0 and int(date[5:7]) <= 12 and int(date[8:]) > 0 and int(date[8:]) <= 31:
                    break
        print(f'"{date}" is not a valid date in the format YYYY-MM-DD')
    return(date)

def AskDuration():
    while True:
        duration = input('Set a duration of the workout (HH-MM-SS): ')
        if len(duration) == 8:
            if duration[:1].isnumeric() and duration[2] == "-" and duration[3:4].isnumeric() and duration[5] == "-" and duration[6:].isnumeric():
                if int(duration[:1]) >= 0 and int(duration[3:4]) >= 0 and int(duration[3:4]) < 60 and int(duration[6:]) >= 0 and int(duration[6:]) < 60:
                    break
        print(f'"{duration}" is not a valid duration')
    return(duration)

def AskAvgBpm():
    while True:
        avgBpm = input('Set the average BPM during the workout: ')
        if avgBpm.isnumeric():
            break
        print(f'"{avgBpm} is not a valid input for the average BPM')
    return(avgBpm)

def AskTopBpm():
    while True:
        topBpm = input('Set the top BPM during the workout: ')
        if topBpm.isnumeric():
            break
        print(f'"{topBpm} is not a valid input for the top BPM')
    return(topBpm)

def AskDistance():
    while True:
        distance = input('Set the distance of the workout (m): ')
        if distance.isnumeric():
            break
        print(f'"{distance} is not a valid distance')
    return(distance)

def AddWorkout():
    os.system('cls')

    print('Add a new workout\n')
    print('Select the type of the workout:')
    for i in range(len(workoutTypesList)):
        print(f'{i}: {workoutTypesList[i]}')
    print('\nQ: Go back to menu')

    while(True):
        userInput = input("\nCommand: ")
        if userInput.isnumeric():
            if int(userInput) <= len(workoutTypesList):
                break
        elif userInput.casefold() == 'q':
            break
        else:
            print(f'"{userInput}" is not a valid command')

    if userInput.casefold() != "q":
        os.system('cls')

        match(userInput):
            case('0'):
                print('Adding a workout: Running\n')
                workouts.listOfWorkouts.append(Running())
            case('1'):
                print('Adding a workout: Cycling\n')
                workouts.listOfWorkouts.append(Cycling())
            case('2'):
                print('Adding a workout: Swimming\n')
                workouts.listOfWorkouts.append(Swimming())
            case('3'):
                print('Adding a workout: Weight training\n')
                workouts.listOfWorkouts.append(WeightTraining())
            case('4'):
                while True:
                    workoutUserInput = input('Give a name for the workout: ')
                    if len(workoutUserInput) > 0 and all(chr.isalpha() or chr.isspace() for chr in workoutUserInput):
                        break
                    print(f'"{workoutUserInput}" is not a valid name for the workout')
                    print(f'Adding a workout: {workoutUserInput}\n')
                workouts.listOfWorkouts.append(OtherWorkout(workoutUserInput))

        workouts.listOfWorkouts[-1].SetDate(AskDate())

        workouts.listOfWorkouts[-1].SetDuration(AskDuration())

        if userInput != '3':
            workouts.listOfWorkouts[-1].SetDistance(AskDistance())

        while True:
            bpmUserInput = input('Do you want to add BPM information? (Y/N) ')
            if bpmUserInput.casefold() == 'y':
                workouts.listOfWorkouts[-1].SetAvgBpm(AskAvgBpm())
                workouts.listOfWorkouts[-1].SetTopBpm(AskTopBpm())
                break
            elif bpmUserInput.casefold() == 'n':
                break
            print(f'"{bpmUserInput}" is not a valid command')

        match(userInput):
            case('0'):
                print('New workout data has been added for: Running!')
            case('1'):
                print('New workout data has been added for: Cycling!')
            case('2'):
                print('New workout data has been added for: Swimming!')
            case('3'):
                print('New workout data has been added for: Weight training!')
            case('4'):
                print(f'New workout data has been added for: {workoutUserInput}!')

        input('\nPress Enter to continue...')

# Main program function
def Main():
    if os.path.getsize('exerciselist.pkl') > 0:
        with open('exerciselist.pkl', 'rb') as inp:
            unpickler = pickle.Unpickler(inp)
            workouts.listOfWorkouts = unpickler.load()

    while True:
        os.system('cls')

        for i in range(len(mainMenuOptions)):
            if i == len(mainMenuOptions)-1:
                print(f'\nQ: {mainMenuOptions[i]}')
            else:
                print(f'{i}: {mainMenuOptions[i]}')
        while True:
            userInput = input("\nCommand: ")
            if userInput.isnumeric():
                if int(userInput) <= len(mainMenuOptions):
                    break
            elif userInput.casefold() == "q":
                break
            print(f'"{userInput}" is not a valid command')

        match(userInput):
            case('0'):
                AddWorkout()
            case('1'):
                workouts.ListWorkouts()
            case('q'):
                with open('exerciselist.pkl', 'wb') as outp:
                    pickle.dump(workouts.listOfWorkouts, outp, pickle.HIGHEST_PROTOCOL)
                break


# Initializing variables
workoutTypesList = ['Running', 'Cycling', 'Swimming', 'Weight training', 'Other workout']
workoutList = []
mainMenuOptions = ['Add new workout', 'List workouts', 'Quit']
activeOption = 0
workouts = Workouts()

# Main program
if __name__ == "__main__":
    Main()