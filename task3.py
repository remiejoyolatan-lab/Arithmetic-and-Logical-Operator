# Task 3: Unit Conversion Challenge

inches = int(input("Enter the number of inches: "))
feet = inches // 12
remaining_inches = inches % 12

print(f"{inches} inches is equal to {feet} feet and {remaining_inches} inches.")