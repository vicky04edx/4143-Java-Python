def typeOfNum (num):
    sum = 0

    for i in range (1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return 'p'
    elif sum > num:
        return 'a'
    else:
        return 'd'
def sumNum(num):
    if num <= 0:
        return 0
    else:
        return num + sumNum(num-1)


num1 = int(input("Enter a number: "))

print(typeOfNum(num1))
print(sumNum(num1))

