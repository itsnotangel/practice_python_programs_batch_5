# Prompt the user to enter their full name with leading spaces.  
# Remove the leading spaces and print the cleaned name.  

fullname = input("Enter your fullname: ")
formatted_name = fullname.lstrip()
print (formatted_name)