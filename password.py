print("====================================")
print("      PASSWORD STRENGTH CHECKER")
print("====================================")

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for character in password:
    if character.isupper():
        has_upper = True
    elif character.islower():
        has_lower = True
    elif character.isdigit():
        has_digit = True
    else:
        has_special = True

score = 0

if len(password) >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

print("\n---------- RESULT ----------")

if score == 5:
    print("Password Strength: STRONG")
elif score >= 3:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: WEAK")

print("\nPassword requirements:")

if len(password) >= 8:
    print("✓ At least 8 characters")
else:
    print("✗ Use at least 8 characters")

if has_upper:
    print("✓ Contains an uppercase letter")
else:
    print("✗ Add an uppercase letter")

if has_lower:
    print("✓ Contains a lowercase letter")
else:
    print("✗ Add a lowercase letter")

if has_digit:
    print("✓ Contains a number")
else:
    print("✗ Add a number")

if has_special:
    print("✓ Contains a special character")
else:
    print("✗ Add a special character")

print("----------------------------")
