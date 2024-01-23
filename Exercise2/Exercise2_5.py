# File name:    Exercise2_5.py
# Author:       Eerik Vainio
# Description:  From multiple people, finds the person with the smallest average
#               results.

# Loops through all arguments, and finds the one with the smallest average result
def smallest_average(*persons):
    smallest_result = smallest_person = None
    for x in persons:
        average_result = calculate_average([x["result1"], x["result2"], x["result3"]])

        if(smallest_result == None or average_result < smallest_result):
            smallest_result = average_result
            smallest_person = x
    
    return smallest_person

# Function to calculate average value
def calculate_average(results):
    total = 0

    for x in results:
        total += x

    return(total / len(results))


person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
print(smallest_average(person1, person2, person3))