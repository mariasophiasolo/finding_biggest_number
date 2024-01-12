# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Find The Biggest Number")
window.minsize(width=355, height=500)
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

poster = tk.PhotoImage (file="biggest.png")
poster_label = tk.Label(image=poster,borderwidth=0)
poster_label.place(x=0, y=0)
# print the output
number1 = tk.Entry(window, width=8)
number2 = tk.Entry(window, width=8)
number3 = tk.Entry(window, width=8)

number1.place(x=45, y=50)
number2.place(x=150, y=50)
number3.place(x=256,y=50)

find_button = tk.Button (window, text = "Find the Biggest Number", command=find_and_print_the_biggest_number)
find_button.place (x=30,y=140)

result_label = tk.Label(window, text="")
result_label.place(x=30, y=170)

window.mainloop()