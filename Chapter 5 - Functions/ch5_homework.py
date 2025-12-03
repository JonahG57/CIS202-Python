# Functions
def calculate_average(score1, score2, score3, score4):
    final_score = score1 + score2 + score3 + score4
    average = final_score / 4
    return average

def determine_letter_grade(average):
    if average >= 90:
        return "A"
    if average >= 80 and average <= 89:
        return "B"
    if average >= 70 and average <= 79:
        return "C"
    if average >= 60 and average <= 69:
        return "D"
    else:
        return "F"

def display_grade_info(name, average, letter_grade):
    print(f"Student: {name}")
    print(f"Average: {average}")
    print(f"Letter Grade: {letter_grade}")
    print("")

def main():
    # Student Info
    name = input("Enter student name: ")
    score1 = float(input("Enter test score: "))
    score2 = float(input("Enter test score: "))
    score3 = float(input("Enter test score: "))
    score4 = float(input("Enter test score: "))
    print("-------------------------")

    average = calculate_average(score1, score2, score3, score4)
    grade = determine_letter_grade(average)
    display_grade_info(name, average, grade)

print("Grade Calculator")
print("====================")
# Loop for How Many Students to Process
loop = int(input("How many students do you want to process? "))
while loop != 0:
    main()
    loop -= 1