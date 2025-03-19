# Prompt the user to enter a complete statement.  
# Count the number of words in the input and print.

statement = input("Enter a complete statement: ")
word_count = len(statement.split())
print(word_count)
