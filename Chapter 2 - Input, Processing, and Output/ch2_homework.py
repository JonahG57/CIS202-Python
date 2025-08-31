# Variables
tax = 0.08
subTotal = float(input("Groceries Amount: ")) # Grocery Amount
salesTax = subTotal * tax # $30 * 0.08
total = subTotal + salesTax # $30 + Sales Tax

print(f"Subtotal: {subTotal:.2f}")
print(f"Sales Tax: {salesTax:.2f}")
print(f"Total: {total:.2f}")