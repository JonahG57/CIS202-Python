file = open("C:\\Users\\Jonah Baraw\\Desktop\\Calhoun\\Semester 1\\Python\\Chapter 6 - File Processing\\EXnumbers.txt", "r")
lines = file.readlines()

avg = 0
sumit = 0

for num in lines:
    sumit += int(num)
    avg += 1

average = sumit//avg

print("The total of all numbers is: ", sumit)
print("The average is: ", average)

file.close()