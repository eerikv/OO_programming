# File name:    Exercise4_1.py
# Author:       Eerik Vainio
# Description:  An object that inspects a list, and can return the
#               item that appears the most times in the list, and
#               the number of items that appear atleast twice.

class ListHelper:
    def greatest_frequency(my_list: list):
        greatest_index = None
        greatest_number = 0
        for item in my_list:
            if my_list.count(item) > greatest_number:
                greatest_index = my_list.index(item)
                greatest_number = my_list.count(item)
            
    
        return my_list[greatest_index]
    
    def doubles(my_list: list):
        found_items = []
        for item in my_list:
            if my_list.count(item) >= 2 and not item in found_items:
                found_items.append(item)
        
        return len(found_items)
                

numbers =[1,1,2,1,3,3,4,5,5,5,6,5,5,5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))