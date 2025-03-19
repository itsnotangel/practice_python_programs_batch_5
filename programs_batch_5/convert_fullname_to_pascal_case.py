# Prompt the user to enter their full name with incorrect casing.  
# Convert the input to Pascal Case and print.  

fullname = input("Enter your full name in incorrect casing: ")
pascal_case_format = fullname.title().replace(" ", "")
print(pascal_case_format)
