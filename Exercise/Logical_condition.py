age = int(input("Enter your Age\n"))
if age < 0 or age > 120:
    print("Invalid Age")
elif age < 18:
    print("you are minor")
elif age >= 18 and age < 65:
    print("You are adult")
else:
    print("You are Senior citizen")
