file = open("C:\\Users\\Jonah Baraw\\Desktop\\Calhoun\\Semester 1\\Python\\Chapter 7\\CH7numbers.txt", "r")
# I have to specify location because I have set up my python weird over the years
lines = file.readlines()

# Variables
sum = 0
avg = 0
numOfNum = 0
large = None
small = None
firstRun = True # To put the first number as a Variable for Large and Small to compare
numList = []

# Figruing out variables
for num in lines:
    num = int(num)
    sum += num
    avg += 1
    numOfNum += 1
    numList.append(num)

    # For large and small variables
    if firstRun == True:
        large = num
        small = num
        firstRun = False
    else:
        if num > large:
            large = num
        if num < small:
            small = num

finalAvg = sum//avg
numList.sort()

# Printing final products
print("The total of all numbers is: ", sum)
print("The average is: ", finalAvg)
print("The number of numbers is: ", numOfNum)
print("The largest number is: ", large)
print("The smallest number is: ", small)
print(numList)

file.close()