# # my_tuple = (1,2,[3,4])
# # my_tuple[2][0] = 5
# # print(my_tuple)

# myList = [4, 5, 6]
# yourList = ['a', 'b', 'c']
# theList = yourList + []
# theList.extend(['q', 'r', 's'])
# print(theList[4:])

# thistuple = tuple(("apple", "banana", "cherry"))
# print(thistuple)

grades = {"Alice": 90, "Bob": 85, "Cindy": 95}

for key, value in grades.items():
    print(key, value)

for value in grades.values():
    print(value)

for key in grades:
    print(key)