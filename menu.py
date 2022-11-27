"""
Author: Jake Russell
Date: 9th December 2019

This python module is responsible for creating the Tkinter menu and
handling the different button operations that the user can do
"""

import booksearch, bookcheckout, bookreturn, booklist
import tkinter, sys

# Initialise and Create Tkinter Window
menuWindow = tkinter.Tk()
menuWindow.geometry("500x500")
menuWindow.title("Library System Menu")
label = tkinter.Label(menuWindow, text="Welcome to The Library System "
                                       "Menu").pack()

# Creating All Menu Buttons Required
buttonBookSearch = tkinter.Button(menuWindow, text="Book Search",
                                  command=lambda: buttonFunction(
                                      "booksearch")).pack()
buttonBookCheckout = tkinter.Button(menuWindow, text="Book Checkout",
                                    command=lambda: buttonFunction(
                                        "bookcheckout")).pack()
buttonBookReturn = tkinter.Button(menuWindow, text="Book Return",
                                  command=lambda: buttonFunction(
                                      "bookreturn")).pack()
buttonBookList = tkinter.Button(menuWindow, text="Book List",
                                command=lambda:buttonFunction(
                                    "booklist")).pack()
buttonQuit = tkinter.Button(menuWindow, text="Quit",
                            command=lambda: buttonFunction("quit")).pack()


# Function Responsible for Dealing with Different Button Presses
def buttonFunction(args):
    """This function is responsible for handling different button presses in
    the main window"""

    if args == "booksearch":
        booksearch.SearchForBook()
    elif args == "bookcheckout":
        if bookcheckout.CheckoutBook():
            print("Book Successfully Checked Out")
        else:
            print("Sorry, this book is already checked out by another member")
    elif args == "bookreturn":
        if bookreturn.ReturnBook():
            print("Book Successfully Returned")
        else:
            print("Sorry, this book is already checked in")
    elif args == "booklist":
        booklist.ListBooks()
    else:
        sys.exit()


menuWindow.mainloop()
