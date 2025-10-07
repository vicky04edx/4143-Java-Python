'''
This program will ask the user for a number and then print out the 
sum from 1 until the number entered
'''

# num = int(input("Enter a number: "))
#sum = 0

# for i in range(1, num+1):
#     sum += i 
# print(sum)
####################################################
# if num == 0:
#     print("The number is zero")
# elif num % 2 == 0:
#     if num > 0:
#         print("The number is positive and even")
#     else:
#         print (" negative and even")
# else:
#     if num > 0:
#         print("The number is positive and odd")
#     else:
#         print (" negative and odd")
###################################################
# for i in range (1, num+1):
#     print(i, i*i)
# if (name == lastname):
#     print("Your name and Last name are the same")
# else:
#     print("Name and lastname are different")
###################################################
numPeople = int(input("How many people are coming? enter a number: "))
numPizzas = int(input("How many pizzas are u ordering? enter a number: "))

slices = numPizzas * 8
result = slices // numPeople
leftovers = slices % numPeople
print("there is going to be", result, "slices per person")
print("there is going to be", leftovers, "leftover slices")















