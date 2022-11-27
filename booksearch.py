"""
Author: Jake Russell
Date: 9th December 2019

This python module is responsible for searching for a book title and
returning the relevant data for all books with this title
"""

import database

databaseName = "database.txt"


# Function for finding and returning books that meet a given input criteria
def SearchForBook():
    """This function is responsible for searching for and returning the
    desired book(s) in the library system
    """

    searchItem = input("Please enter the title of the book which you would "
                       "like to search for? ")
    foundBooks = database.SearchForBook(databaseName, searchItem)
    if len(foundBooks) > 0:
        for line in foundBooks:
            print(line, end="")
    else:
        print("No books with this title were found.")



