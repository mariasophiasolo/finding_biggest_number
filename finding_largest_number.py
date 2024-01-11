# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# pseudocode



# ask the user to input 3 numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

# find the largest among the 3 numbers using the if-else statement
if first_number >= second_number and first_number >= third_number:
    largest_number = first_number
elif second_number >= third_number:
    largest_number = second_number
else:
    largest_number = third_number

# print the output
print("The largest nnumber: ", largest_number)