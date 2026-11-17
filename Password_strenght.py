print("=== Simple Password Strength Checker ===")

password = input("Enter a password to check: ")

# Start with zero points
score = 0

# Track what we find using simple True/False flags
has_upper = False
has_lower = False
has_number = False
has_symbol = False

symbols = "!@#$%^&?"

# Check the password one letter at a time

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_number = True
    elif char in symbols:
        has_symbol = True
        
#Add points based on what we found
if len(password) >= 8:
    score = score + 1
else:
    print("- Tip: Make your password at least 8 characters long.")
if has_upper == True:
    score = score + 1
else:
    print("- Tip: Add at least one capital letter.")
if has_lower == True:
    score = score + 1
else:
   print("- Tip: Add at least one lowercase letter.")
if has_number == True:
   score = score + 1
else:
   print("- Tip: Add at least one number.")
if has_symbol == True:
   score = score + 1
else:
   print("- Tip: Add a symbol like ! or @ or #.")
   
#Show final result
print("\nYour Password Score:", score, "out of 5")

if score == 5:
    print("Result: Strong password!")
elif score >= 3:
    print("Result: Medium password.")
else:
   print("Result: Weak password.")
