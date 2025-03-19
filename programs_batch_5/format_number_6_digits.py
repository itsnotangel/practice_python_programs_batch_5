# Prompt the user to enter a number between 0 and 1000.
# Format the number to be displayed (6-digit value).
# Add leading zeros to ensure the number has exactly 6 digits.

number = int(input("Enter a number (0-1000): "))
formatted_number = f"{number:06}"
print(formatted_number)