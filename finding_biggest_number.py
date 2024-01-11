# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Find The Biggest Number")
window.minsize(width=500, height=500)
window.configure(background="black")
window.resizable(False,False)

def find_and_print_the_biggest_number():
    # ask the user to input 3 numbers
    first_number = int(number1.get())
    second_number = int(number2.get())
    third_number = int(number3.get())

    # find the biggest among the 3 numbers using the if-else statement
    if first_number >= second_number and first_number >= third_number:
        biggest_number = first_number
    elif second_number >= third_number:
        biggest_number = second_number
    else:
        biggest_number = third_number
    
    # Display the result
    result_label.config(text=f"The biggest number is: {biggest_number}")

# print the output
number1 = tk.Entry(window, width=10)
number2 = tk.Entry(window, width=10)
number3 = tk.Entry(window, width=10)
 
find_button = tk.Button (window, text = "Find the Biggest Number", command=find_and_print_the_biggest_number)

result_label = tk.Label(window, text="")

number1.grid(row=0, column=0, padx=5, pady=5)
number2.grid(row=0, column=1, padx=5, pady=5)
number3.grid(row=0, column=2, padx=5, pady=5)
find_button.grid(row=1, column=0, columnspan=3, pady=10)
result_label.grid(row=2, column=0, columnspan=3)

window.mainloop()