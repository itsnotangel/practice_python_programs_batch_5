# Prompt the user to enter their full name with incorrect casing.  
# Convert the input to snake_case and print.

fullname = input("Enter your full name in incorrect casing: ")
snake_case_name = '_'.join(fullname.lower().split())
print(snake_case_name)