# Challenge Problem (Bonus): Shipping Cost Calculator with Rules

# Inputs
weight = float(input("Weight (lbs): "))
destination = input("Destination (domestic/international): ").lower()
membership = input("Membership (standard/premium): ").lower()

# Base cost
cost = 10

# Overweight rule
if weight > 20:
    cost += 5

# International rule
if destination == "international":
    cost *= 2

# Premium discount and exemption
if membership == "premium":
    # Premium customers get 20% off and skip international surcharge
    cost *= 0.8

# Display result
print(f"\nFinal Shipping Cost: ${cost:.2f}")

details = "(Details: Base $10"
if weight > 20:
    details += " + Overweight $5"
if membership == "premium":
    details += ", Premium 20% discount applied"
if destination == "international" and membership == "premium":
    details += ", International fee waived"
details += ".)"

print(details)