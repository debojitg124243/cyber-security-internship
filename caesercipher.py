print("=" * 55)
print("          CAESAR CIPHER ENCRYPTION TOOL")
print("=" * 55)

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


# Get input from the user
message = input("Enter your message: ")
shift = int(input("Enter the shift value (key): "))

# Encrypt the message
encrypted = caesar_cipher(message, shift)

# Decrypt the message
decrypted = caesar_cipher(encrypted, -shift)

# Display results
print("\n" + "=" * 55)
print("                    RESULT")
print("=" * 55)

print("Original Message :", message)
print("Shift Value      :", shift)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)

print("=" * 55)
