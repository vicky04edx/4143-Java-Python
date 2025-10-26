#fname = input("enter file name:")

with open("Frankenstein1.txt", encoding = "utf-8") as fin:
    sum = 0
    digitSum = 0
    for line in fin:
        s = line.strip()
        wordsLine = s.split()
        sum += len(wordsLine)

with open("Frankenstein1.txt", encoding = "utf-8") as fin:
    for char in line:
        s = line.strip()
        wordsLine = s.split()
        for char in line:
            digitSum += int(char)
            
with open("Frankenstein1.txt", encoding = "utf-8") as fin:
    for line in fin:
        if('monster' in line) or ('Monster' in line):
            print(line)


    print("Number of words: ",sum)
    print("Number of digits: ",digitSum)