# Task 5: Secure System Login Simulator

# Correct credentials
correct_username = "remie joy"
correct_password = "olatan"
is_2fa_enabled = True
correct_2fa_code = "101010"

# User input
input_username = input("Enter username: ")
input_password = input("Enter password: ")
two_fa = input("Is 2FA enabled? (y/n): ")

# Check 2FA
if two_fa.lower() == 'y':
    input_2fa_code = input("Enter 2FA code: ")
else:
    input_2fa_code = ""

# Login condition
if (input_username == correct_username and
    input_password == correct_password and
    ((two_fa.lower() != 'y') or (input_2fa_code == correct_2fa_code))):
    print("Login successful!")
else:
    print("Login failed!")