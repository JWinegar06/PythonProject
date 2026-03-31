print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input(" What tip% would you like to leave? 10, 12, or 15? "))
party = int(input("How many in the party? "))
percent = tip / 100
amount = bill * percent
total = bill + amount
person = total / party
final = round(person, 2)
print(f"Each person should pay ${final} ")


