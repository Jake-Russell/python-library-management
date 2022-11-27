"""
Author: Jake Russell
Date: 9th December 2019

This python module is responsible for gathering the relevant information
required to create the book popularity graph. It is also responsible for
creating this graph and displaying this to the user.
"""

import database
import datetime
import matplotlib.pyplot as plt

logfileName = "logfile.txt"
databaseFileName = "database.txt"
logfileHeading = "Book ID     Book Title     Checkout Date     Return Date\n"
lineLength = 3


def ListBooks():
    """This function is responsible for creating the graph of book popularity"""

    results = GetBookCheckoutFrequency()
    checkoutFrequency = results[0]
    allBookTitles = results[1]

    plt.bar(allBookTitles, checkoutFrequency)
    plt.title("Book Popularity")
    plt.xlabel("Book Title")
    plt.ylabel("Checkout Frequency")
    plt.show()


def GetBookCheckoutFrequency():
    """This function is responsible for returning the list of the book
    checkout frequency and the list of book titles too

    Returns:
        bookPopularity ([int]): This is the list of the book checkout
            frequency - the number of times that each book has been checkout out
            from the library system
        bookTitles ([string]): This is the list of all of the book titles in
            the library system, sorted in accordance with the bookPopularity
            list
    """

    bookPopularity = []
    allDatabaseData = database.ExtractData(databaseFileName)
    allLogFileData = database.ExtractData(logfileName)

    for databaseLine in allDatabaseData:
        count = 0
        for logfileLine in allLogFileData:
            if databaseLine[1] == logfileLine[1]:
                count = count + 1
        bookPopularity.append(count)

    return BubbleSort(bookPopularity, database.GetAllBookTitles(
        databaseFileName))


def BubbleSort(bookPopularity, bookTitles):
    """This function is responsible for sorting first the bookPopularity list
    and then sorting the bookTitles list in accordance to this. For example,
    if the first list is in the order [3, 2, 1, 5, 4], once sorted, index 3
    of the first list becomes index 0, so hence index 3 of list 2 becomes
    index 0 as well.

    Args:
        bookPopularity ([int]): This is the unsorted list of book popularities
        bookTitles ([string]): This is the unsorted list of book titles

    Returns:
        bookPopularity ([int]): This is the sorted list of book popularities
        bookTitles ([string]): This is the sorted list of book titles in
            accordance to the order of the bookPopularity list
    """
    length = len(bookPopularity)
    for i in range(length):
        for j in range(0, length-i-1):
            if bookPopularity[j] > bookPopularity[j+1]:
                bookPopularity[j], bookPopularity[j+1] = bookPopularity[j+1],\
                                                         bookPopularity[j]
                bookTitles[j], bookTitles[j+1] = bookTitles[j+1], bookTitles[j]
    bookPopularity.reverse()
    bookTitles.reverse()
    return bookPopularity, bookTitles


def CheckoutLogData(bookIDInput):
    """This function is responsible for creating and writing the new checkout
    data to the logfile

    Args:
        bookIDInput (int): This is the ID of the book which is being checkout
            out from the library system
    """
    checkoutLogData = [bookIDInput, database.GetBookTitle(databaseFileName,
                       bookIDInput), GetCurrentTime(), "0\n"]

    allLogData = database.ExtractData(logfileName)
    allLogData.append(checkoutLogData)
    database.WriteData(allLogData, logfileName, logfileHeading, lineLength)


def ReturnLogData(bookIDInput):
    """This function is responsible for creating and writing the new return
    data to the logfile

    Args:
        bookIDInput (int): This is the ID of the book which is being returned
            to the library system
    """

    allLogData = database.ExtractData(logfileName)
    for line in allLogData:
        for i in range(len(line)):
            if line[0] == str(bookIDInput) and line[3] == "0\n":
                line[3] = (GetCurrentTime() + "\n")
    database.WriteData(allLogData, logfileName, logfileHeading, lineLength)


def GetCurrentTime():
    """This function is responsible for returning the current date and time

    Returns:
        checkoutTime (string): This is the current date and time, used for
            creating and writing the checkout / return data
    """

    checkoutTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return checkoutTime


if __name__ == "__main__":
    # Test GetBookCheckoutFrequency
    results = GetBookCheckoutFrequency()
    bookPopularity = results[0]
    assert len(bookPopularity) == 10, "Expected 10 different book " \
                                      "popularities, received " + \
                                      str(len(bookPopularity))

    # Test BubbleSort
    results = BubbleSort([3, 2, 1, 5, 4], [10, 9, 8, 7, 6])
    result1 = results[0]
    result2 = results[1]
    assert result1 == [5, 4, 3, 2, 1], "Expected sorted list to be [1, 2, 3, \
                                       4, 5], however, it was returned as " +\
                                       str(result1)
    assert result2 == [7, 6, 10, 9, 8], "Expected sorted list to be [6, 7, 8, \
                                        9, 10], however, it was returned as " +\
                                        str(result2)
    # Note that result2 is expected in the order [7, 6, 10, 9, 8] because
    # this is the corresponding order in which result1 is returned. Once
    # sorted, index 3 of result1 becomes index 0, so hence index 3 of result2
    # becomes index 0 as well.
