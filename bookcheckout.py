"""
Author: Jake Russell
Date: 9th December 2019

This python module is responsible for getting user input for the required
information for checking out the desired book, and checking this book out of
the library system
"""

import booklist, database

databaseName = "database.txt"
databaseHeading = "ID     Title     Author     Purchase Date     Member ID\n"
lineLength = 4


def CheckoutBook():
    """This function is responsible for attempting to check the desired book
    out of the library system

    Returns:
        bool: This is used to determine whether the book has been checkout out
        successfully or not
    """

    results = ValidateInput()
    memberIDInput = results[0]
    bookIDInput = results[1]

    if database.IsBookAvailable(databaseName, bookIDInput):
        allBookData = database.ExtractData(databaseName)
        for dataLine in allBookData:
            if dataLine[0] == str(bookIDInput):
                dataLine[4] = str(memberIDInput) + "\n"
        database.WriteData(allBookData, databaseName, databaseHeading,
                           lineLength)
        booklist.CheckoutLogData(bookIDInput)
        return True

    else:
        return False


def ValidateInput():
    """This function is responsible for taking and validating user input for
    the member ID and book ID

    Returns:
        memberIDInput (int): This is the inputted and validated member ID
        bookIDInput (int): This is the inputted and validated book ID
    """

    validInput = False
    while not validInput:
        try:
            memberIDInput = int(input("Please enter the 4 Digit Member ID: "))
            bookIDInput = int(input("Please enter the Book ID: "))
            if len(str(memberIDInput)) != 4:
                print("The Member ID should be a 4 digit number.")
            elif not database.IsBookIDValid(databaseName, bookIDInput):
                print("Invalid input. A book with this ID is not in the "
                      "library")
            else:
                validInput = True
        except ValueError:
            print("Invalid input. Both the Member ID and Book ID should be "
                  "numbers.")
    return memberIDInput, bookIDInput
