# File name:    Exercise2_6.py
# Author:       Eerik Vainio
# Description:  Prints out the years from multiple date objects.

from datetime import date

# Creates a new list with the years from all of the date objects
def list_years(dates: list):
    new_list = []

    for x in dates:
        new_list.append(x.year)

    new_list.sort()
    return new_list

date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)