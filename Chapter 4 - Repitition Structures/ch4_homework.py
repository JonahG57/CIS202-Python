loop = True
ageLoop = True

while loop == True:
    while ageLoop == True:
        age = int(input("Enter your Age: "))
        if age > 0:
            ageLoop = False
        else:
            print("You did not enter a valid Age. Please try again.")

    if age < 6:
        print("You are too young for elementary school.")
    elif age >= 6 and age < 11:
        print("You are in Primary or Elementary School.")
    elif age >= 11 and age < 14:
        print("You are in Middle School.")
    elif age >= 14 and age < 19:
        print("You are in High School.")
    else:
        print("You are an adult. Choose your career path.")

    endLoop = input("Do you want to enter another age? (Y/N) ")
    if endLoop == "n" or endLoop == "N":
        print("Thank you, and Goodbye (:")
        loop = False
    elif endLoop == "y" or endLoop == "Y":
        print("Restarting:")
        ageLoop = True
    else:
        print("I did not understand, restarting Program.")
