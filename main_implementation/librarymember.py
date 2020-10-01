# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:52:07 2019

@author: catalin
"""
from main_implementation.physicalbook import PhysicalBook


class LibraryMember:

    """ Class to represent a member of library. """

    def __init__(self):
        self.nameMember ="not set"
        self.memberID= 0
        self.listBooksBorrowed= []#the variables in the list need to be objects of type of physicalBook
        self.notifications= ""


    def setNameMember(self, name):
        """Sets the name of the library member"""
        self.nameMember= name

    def setMemberID(self, id):
        """Sets the id for the lirary member"""
        self.memberID= id

    def setMessages(self , newMessages):
        """Sets new message to concatenate to notifications."""
        assert type(newMessages) is str, "Format not supported,It needs to be a string"
        self.notifications= self.notifications+ newMessages

    def getNameMember(self):
        """Gets the name of the library member"""
        return self.nameMember

    def getMemberID(self):
        """"Gets the ID of the library member"""
        return self.memberID

    def printAllMessages(self):
        """ Prints all messages. """
        print("Messages for User:{}".format(self.notifications))

    def addBook(self, newBook):
        """Adds resource in list of borrowed books"""
        assert type(newBook) is PhysicalBook, "This book does not belong to PhysicalBook class"
        if newBook in self.listBooksBorrowed:
            print("the user already borrowed this book")
        else:
            self.listBooksBorrowed.append(newBook)

    def removeBook(self, Book):
        """Removes resource from list of borrowed books"""
        assert type(Book) is PhysicalBook, "This book does not belong to PhysicalBook class"
        if Book in self.listBooksBorrowed:
            self.listBooksBorrowed.remove(Book)
            print("the book was returned")
        else:
            print("the user did not borrow this book")

    def printAllBorowedBooksByUser(self):
        """ Prints resources and books borrowed."""
        for borrowedBook in self.listBooksBorrowed:
            borrowedBook.printPhysicalBookDetails()

    def printLibraryMemberDetails(self):
        """ Prints details of a member."""
        print("Library member {} - {}- has borrowed the following books:".format(self.memberID, self.nameMember))
        self.printAllBorowedBooksByUser()

    def numberOfBooksBorrowed(self):
        """ Returns number of borrowed books."""
        return len(self.listBooksBorrowed)
