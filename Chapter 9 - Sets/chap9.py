file = open("C:\\Users\\jonah\\OneDrive\\Desktop\\Calhoun\\Semester 1\\Python\\Chapter 9 - Sets\\Text2.txt", "r")
lines = file.readlines()

unique = set()

for line in lines:
    words = line.split()
    unique.update(words)

print(unique)