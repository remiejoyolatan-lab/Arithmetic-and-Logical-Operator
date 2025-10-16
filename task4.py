# Task 4: The Movie Ticket Price Decider

age = 19
is_student = True

base_price = 12
discount = 0

# Apply discount rules
if age <= 12:
    discount = 3
elif age >= 65:
    discount = 4
elif is_student:
    discount = 2

final_price = base_price - discount

print("Age:", age)
print("Is student? (True/False):", is_student)
print(f"Your ticket price is ${final_price}.")