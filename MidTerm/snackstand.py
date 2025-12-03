print("Campus Snack Stand")
print("------------------")

# Prices of items
price_A = 1.25 # Bottled Water
price_B = 1.75 # Granola Bar
price_C = 2.50 # Fruit Cup

# Reciept Variables
subtotal = 0.0
code = "STUDENT"
disPercent = 0.1
tax = 0.085
loop = True

# Loop for Choices
while loop == True:
    choice = input("Enter item code (A=Water $1.25, B=Granola $1.75, C=Fruit $2.50): ")
    quantity = int(input("Enter quantity: "))
    if choice == 'a' or choice == 'A':
        price = price_A * quantity
        subtotal = price + subtotal
    elif choice == 'b' or choice == 'B':
        price = price_B * quantity
        subtotal = price + subtotal
    elif choice == 'c' or choice == 'C':
        price = price_C * quantity
        subtotal = price + subtotal
    else:
        print("Your choice was not recognised, please try again")

    # Another Item
    anotherItem = input("Add another item? (Y/N): ")
    if anotherItem == 'N' or anotherItem == 'n':
        loop = False

# Promo Code Correct?
print("If you are a student you get a 10% discount using discount code STUDENT")
print('')
promo = input("Enter Promo Code for discount or press Enter to skip: ")
if promo == code:
    discount = subtotal * disPercent
    subtotal = subtotal - discount
else:
    discount = 0.00

# Tax Amount
salesTax = subtotal * tax
total = subtotal + salesTax

# Receipt
print('')
print("----- RECEIPT -----")
print(f"Subtotal before discount: ${subtotal:.2f}")
print(f"Discount (10%):          -${discount:.2f}")
print(f"Tax (8.5%):               ${salesTax:.2f}")
print(f"TOTAL DUE:                ${total:.2f}")
print("Thank you!")