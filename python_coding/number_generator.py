"""
You are given:

A string digits → this is the layout of numbers 0–9 on a straight keyboard
Example: "8123456790"
So 8 is at index 0, 1 at index 1, 2 at index 2, etc.

A string num → the number you want to type
Example: "210"

absolute difference in index positions between two consecutive digits determines the time taken to type them.

Return the number of milliseconds it takes to type num
"""

st = "2451387690"

num = "578"


def count_time(st, num):
    index_map = {dig: idx for idx, dig in enumerate(st)}
    timetaken = 0
    for i in range(1, len(str(num))):
        timetaken += abs(index_map[num[i]] - index_map[num[i - 1]])
    return timetaken


count_time(st, num)
