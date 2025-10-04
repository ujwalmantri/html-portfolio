print("Welcome to the bill splitter!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

total_amount = bill + ( tip / 100 ) * bill
amount_per_person = round(total_amount/people, 2)

print(f'Each person should pay: ${amount_per_person}')