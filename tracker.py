# Project: Expense Tracker
# Installment: 3 - The Tracker Does Math
# Author: Mark Jayson D. Mendoza
# A simple expense tracker that talks to the user and does math.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("MAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t\t(coming soon)")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal = subtotal + amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal = subtotal + amount2

average = subtotal / 2

tax_percent = int(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print("-" * 40)
print("SUMMARY")
print(f" - {item1}:\t\t${amount1}")
print(f" - {item2}:\t\t${amount2}")
print(f"Subtotal:\t\t${subtotal:.2f}")
print(f"Average:\t\t${average:.2f}")
print(f"Tax ({float(tax_percent):.1f}%):\t\t${tax:.2f}")
print(f"Grand total:\t\t${total:.2f}")
print(f"Over budget?\t\t{over_budget}")
print(f"Left in budget:\t\t${left:.2f}")
print("-" * 40)

print(f"Made by: {name} | Installment 3")