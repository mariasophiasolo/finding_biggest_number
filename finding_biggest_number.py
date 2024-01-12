# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

import tkinter as tk
from tkinter import messagebox

def find_and_print_the_biggest_number():
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
    result_label.config (text=f"The Biggest Number Is:\n {biggest_number}")

# Creating the main window
window = tk.Tk()
window.title("Find The Biggest Number")
window.minsize(width=355, height=500)
window.configure(background="black")
window.resizable(False,False)

# Image
poster = tk.PhotoImage (file="math.png")
poster_label = tk.Label(image=poster,borderwidth=0)
poster_label.place(x=0, y=0)

# Header
number_label = tk.Label(window, text="P L E A S E  E N T E R  T H R E E  N U M B E R S", bg="black", fg="khaki1", font=("Glacial Indifference", 10))
number_label.place(x=25, y=360)

# Entry number
number1 = tk.Entry(window, width=8)
number2 = tk.Entry(window, width=8)
number3 = tk.Entry(window, width=8)
number1.place(x=45, y=385)
number2.place(x=150, y=385)
number3.place(x=256,y=385)

# Find button
find_button = tk.Button (window, text = "FIND", font=("Glacial Indifference", 10, "bold"), fg="khaki1", bg="black", command=find_and_print_the_biggest_number)
find_button.place (x=155,y=460)

# Printing result
result_label = tk.Label(window, text="The Biggest Number Is:", font=("Glacial Indifference", 10, "bold"), fg="khaki1", bg="black",)
result_label.place(x=102, y=420)

window.mainloop()