"""
Author: Jake Russell
Date: 9th December 2019

This python module is responsible for containing all of the common modules
which are related to the database.
"""


def ExtractData(filename):
    """This function is responsible for extracting the data from the required
    file and storing it in a 2-D array

    Args:
        filename (string): This is the filename of the file to be used

    Returns:
        data ([[string]]): This is the 2-D array of all data in the file
    """

    file = open(filename, "r")
    data = []
    for line in file:
        dataLine = line.split("     ")
        data.append(dataLine)
    del(data[0])
    return data


def WriteData(allFileData, filename, fileHeading, lineLength):
    """This function is responsible for writing data to the required file

    Args:
        allFileData ([[string]]): This is the 2-D array of all data in the file
        filename (string): This is the filename of the file to write data to
        fileHeading (string): This is the file heading of the file which
            data is to be written to
        lineLength (int): This is the line length of the file which data is
            to be written to
    """

    file = open(filename, "r+")
    file.truncate(0)
    file.write(fileHeading)
    for line in allFileData:
        for i in range(len(line)):
            file.write(str(line[i]))
            if i < lineLength:
                file.write("     ")

    file.close()


def IsBookAvailable(filename, bookIDInput):
    """This function is responsible for checking whether the book is
    available to be checked out or not

    Args:
        filename (string): This is the filename of the file to be used
        bookIDInput (int): This is the book ID to be checked for

    Returns:
        bool: This is used to determine whether the book is available to be
            checked out or not
    """

    file = open(filename, "r")

    for line in file:
        dataLine = line.split("     ")
        bookID = dataLine[0]
        memberID = dataLine[4]

        if memberID == "0\n" and bookID == str(bookIDInput):
            file.close()
            return True

    file.close()
    return False


def IsBookIDValid(filename, bookIDInput):
    """This function is responsible for checking whether or not the
    inputted book ID is a valid ID in the library system

    Args:
        filename (string): This is the filename of the file to be used
        bookIDInput (int): This is the book ID to check for in the file

    Returns:
        bool: This is used to determine whether the book ID is a valid ID in
            the library system or not
    """

    file = open(filename, "r")

    for line in file:
        dataLine = line.split("     ")
        bookID = dataLine[0]

        if bookID == str(bookIDInput):
            file.close()
            return True

    file.close()
    return False


def GetAllBookTitles(filename):
    """This function is responsible for returning all of the book titles from
    the file, and storing them in an array

    Args:
        filename (string): This is the filename of the file to be used

    Returns:
        bookTitles ([string]): This is the array of all book titles in the
            library system
    """

    file = open(filename, "r")
    bookTitles = []
    for line in file:
        dataLine = line.split("     ")
        bookTitle = dataLine[1]

        if bookTitle != "Title":
            bookTitles.append(bookTitle)

    file.close()
    return bookTitles


def GetBookTitle(filename, bookIDInput):
    """This function is responsible for returning the book title of a single
    book, given this book's ID

    Args:
        filename (string): This is the filename of the file to be used
        bookIDInput (int): This is the book ID to be used to get the relevant
            book title

    Returns:
        bookTitle (string): This is the book title found in the file,
            given that book's ID
    """

    file = open(filename, "r")

    for line in file:
        dataLine = line.split("     ")
        bookID = dataLine[0]
        bookTitle = dataLine[1]

        if bookID == str(bookIDInput):
            file.close()
            return bookTitle
    file.close()


def SearchForBook(filename, searchItem):
    """This function is responsible for searching for a book(s) in the file
    based on it's title, and returning all relevant information

    Args:
        filename (string): This is the filename of the file to be used
        searchItem (string): This is the book title to search for in the file

    Returns:
        foundBooks ([string]): This is the list of books with the given
        title, and their respective data
    """

    file = open(filename, "r")

    foundBooks = []
    for line in file:
        dataItem = line.split("     ")
        if dataItem[1].__contains__(searchItem):
            foundBooks.append(line)

    file.close()
    return foundBooks


if __name__ == "__main__":
    # Test ExtractData
    data = ExtractData("database.txt")
    assert len(data) == 10, "Expected database to be length 10, but it was " \
                            "actually length " + str(len(data))

    # Test IsBookAvailable
    # These tests are fragile because somebody using the system could affect
    # the outcome of these tests.
    bookAvailable = IsBookAvailable("database.txt", 1)
    assert not bookAvailable, "Expected book ID 1 to be checked out, but it " \
                              "was not"
    bookAvailable = IsBookAvailable("database.txt", 2)
    assert bookAvailable, "Expected book ID 2 to not be checked out, but it " \
                          "was"

    # Test IsBookIDValid
    validBookID = IsBookIDValid("database.txt", 1)
    assert validBookID, "Expected book ID 1 to be a valid book ID, " \
                        "but it was not"
    validBookID = IsBookIDValid("database.txt", 14)
    assert not validBookID, "Expected book ID 14 to be an invalid book ID, " \
                            "but it was not"

    # Test GetAllBookTitles
    allBookTitles = GetAllBookTitles("database.txt")
    assert len(allBookTitles) == 10, "Expected 10 book titles, received " + \
                                     str(len(allBookTitles))

    # Test GetBookTitle
    bookTitle = GetBookTitle("database.txt", 1)
    assert bookTitle == "Book_1", "Expected book title 'Book_1', received " +\
                                  bookTitle

    # Test SearchForBook
    foundBooks = SearchForBook("database.txt", "Book_1")
    assert len(foundBooks) == 2, "Expected 2 books, received " + str(len(
        foundBooks))







