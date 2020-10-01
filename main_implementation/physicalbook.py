# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:52:07 2019

@author: catalin
"""

class PhysicalBook:

    """ Class to represent a physical book."""

    def __init__(self):
        self.ISBN= 0
        self.libraryUser= None # object of type LibraryMember class
        self.damagesBook= ""
        self.bookTitle= "not set"
        self.bookAuthor= "not set"


    def setISBN(self, ISBN):
        """Sets the ISBN of PhysicalBook"""
        self.ISBN = ISBN

    def setLibraryUser(self, libraryUser):
        """ Sets library user"""
        self.libraryUser= libraryUser

    def setDamages(self, newDamages):
        """ Sets any damages for book"""
        assert type(newDamages) is str, "Error :not a text"
        self.damagesBook= self.damagesBook +':'+ newDamages

    def setBookTitle(self, title):
        """Sets the title of PhysicalBook"""
        self.bookTitle= title

    def setBookAuthor(self, author):
        """Sets the author of PhysicalBook"""
        self.bookAuthor= author


    def getISBN(self):
        """Gets the ISBN of PhysicalBook"""
        return self.ISBN

    def getBookTitle(self):
        """Gets the title of PhysicalBook"""
        return self.bookTitle

    def getBookAuthor(self):
        """Gets the author of PhysicalBook"""
        return self.bookAuthor

    def getLibraryUser(self):
        """ Gets library user"""
        return self.libraryUser
    
    def getDamages(self):
        """ Gets book damages"""
        return self.damagesBook


    def checkBookAvailability(self):
        """ Checks if the book is available """
        if self.libraryUser== None:
            return True
        else:
            return False

    def printPhysicalBookDetails(self):
        """ Prints the details of a book"""
        print("{}, by {} ISBN:{}, with the following damages:{} ".format(self.bookTitle, self.bookAuthor, self.ISBN, self.damagesBook))
        if self.checkBookAvailability() is True:
            print("This book is available")
        else:
            print("This book is not available")
