"""
Author: Jake Russell
Date: 9th December 2019

This python module is responsible for getting user input for the required
information for returning the desired book, and returning this book out of
the library system
"""

import booklist, database

databaseName = "database.txt"
databaseHeading = "ID     Title     Author     Purchase Date     Member ID\n"
lineLength = 4


def ReturnBook():
    """This function is responsible for attempting to return the desired book
    to the library system

    Returns:
        bool: This is used to determine whether the book has been returned
        successfully or not
    """

    bookIDInput = ValidateInput()
    if not database.IsBookAvailable(databaseName, bookIDInput):
        allBookData = database.ExtractData(databaseName)
        for dataLine in allBookData:
            if dataLine[0] == str(bookIDInput):
                dataLine[4] = "0\n"

        database.WriteData(allBookData, databaseName, databaseHeading,
                               lineLength)
        booklist.ReturnLogData(bookIDInput)
        return True

    else:
        return False


def ValidateInput():
    """This function is responsible for taking and validating user input for
    the book ID

    Returns:
        bookIDInput (int): This is the inputted and validated book ID
    """

    validInput = False
    while not validInput:
        try:
            bookIDInput = int(input("Please enter the Book ID: "))
            if database.IsBookIDValid(databaseName, bookIDInput):
                validInput = True
            else:
                print("Invalid input. A book with this ID is not in the "
                      "library")
        except ValueError:
            print("Invalid input. The Book ID should be numerical value.")
    return bookIDInput
