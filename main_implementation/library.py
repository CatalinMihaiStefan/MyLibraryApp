# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:52:07 2019

@author: catalin
"""
from main_implementation.physicalbook import PhysicalBook
from main_implementation.electronicresources import ElectronicResources
from main_implementation.librarymember import LibraryMember

class Library:

    """Class to represent the library. """

    def __init__(self):

        self.listOfLibraryResources= []# the objects in this list are of type phusicalBook or electricResources
        self.libraryName= "not set" #Name of catalogue.

    def setListOfLibraryResources(self, list):
        """Sets the catalogue of the library"""
        self.listOfLibraryResources = list

    def setLibraryName(self, name):
        """Sets the name of the library"""
        self.libraryName= name

    def getLibraryName(self):
        """Gets the name of the library"""
        return self.libraryName


    def printAllDetailsLibrary(self):
        """Prints all the details of list  """

        print("All the resources in the library are:")
        for resource in self.listOfLibraryResources:
            if isinstance(resource, PhysicalBook):
                resource.printPhysicalBookDetails()
                print('-------')
            elif isinstance(resource, ElectronicResources):
                resource.printElectronicResourcesDetails()
                print('-------')

    def checkElementInLibrary(self, resourceX):
        """Checks if resourceX is in the catalogue list. """
        if resourceX in self.listOfLibraryResources:
            return True
        else:
            return False

    def changeTitleResource(self, resourceY, newTitle):
        """ Change the title of resourceY"""
        if self.checkElementInLibrary(resourceY)== False:
            print("This resource does not exist in list")
        else:
            resourceY.setBookTitle(newTitle)# create setNewTitle function

    def searchByISBN(self, ISBN):
        "Search in the list of library for ISBN"

        n=0
        for resourceZ in self.listOfLibraryResources:
            if isinstance(resourceZ,PhysicalBook):
                if resourceZ.getISBN() == ISBN: #create function getISBN in PhysicalBook class
                    resourceZ.printPhysicalBookDetails()
                    n+=1
            elif isinstance(resourceZ,ElectronicResources):
                if resourceZ.getISBN() == ISBN:
                    resourceZ.printElectronicResourcesDetails()
                    n+=1
        if n==0:
            print("No resources found with this ISBN")
        else:
            print("number of resources with the same ISBN:{}".format(n))

    def searchByAuthor(self, author):
        """ Search in the list for author of resource """
        assert type(author) is str, "This is not a string type"
        n=0
        for resourceZ in self.listOfLibraryResources:
            if isinstance(resourceZ,PhysicalBook):
                if resourceZ.getBookAuthor()== author: #create function getAuthor in PhysicalBook and ElectronicResources class
                    resourceZ.printPhysicalBookDetails()
                    n=n+1
            if isinstance(resourceZ,ElectronicResources):
                if resourceZ.getEBookAuthor()== author: #create function getAuthor in PhysicalBook and ElectronicResources class
                    resourceZ.printElectronicResourcesDetails()
                    n=n+1
        if n==0:
            print("No resources found with this author")
        else:
            print("Number of resources with the same author:{}".format(n))

    def removeResource(self, resourceToDelete):
        """Removes resource you want to be deleted """
        if isinstance(resourceToDelete, PhysicalBook) or isinstance(resourceToDelete, ElectronicResources):
            if self.checkElementInLibrary(resourceToDelete):
                self.listOfLibraryResources.remove(resourceToDelete)
                print('Item removed')
            else:
                print("Item not found")
        else:
            print("Resource not of type PhysicalBook or ElectronicResources ")

    def removeResourceByPosition(self, resourcePosition):
        """Removes resource at the wanted position. """
        assert type(resourcePosition) is int, "position should be of type int"
        if resourcePosition> len(self.listOfLibraryResources):
            print("Resource position does not exist")
        else:
            self.listOfLibraryResources.remove(self.listOfLibraryResources[resourcePosition])
            print("Item deleted")

    def displayAllAvaiableBooks(self):
        """Prints all the available resources and books in the list of library."""
        for resource in self.listOfLibraryResources:
            if isinstance(resource,PhysicalBook):
                if resource.checkBookAvailability():
                    resource.printPhysicalBookDetails()
            elif isinstance(resource,ElectronicResources):
                resource.printElectronicResourcesDetails()

    def lengthOfResources(self):
        """Returns the number of resources and books in the catalogue."""
        return len(self.listOfLibraryResources)

    def addAResource(self, resource):
        """Adds a resource or book in the catalogue."""
        if isinstance(resource,PhysicalBook) or isinstance(resource,ElectronicResources):
            if resource in self.listOfLibraryResources:
                print("Book already in library")
            else:
                self.listOfLibraryResources.append(resource)
                print('Book added to the catalogue')

    def lendBookToMember(self, member, book):
        """It assigns a book or a resource to a library member."""
        assert type(member) is LibraryMember, "person is not type libraryMember"
        if isinstance(book,PhysicalBook) or isinstance(book,ElectronicResources):
            if self.checkElementInLibrary(book):
                if book.checkBookAvailability():
                    if member.numberOfBooksBorrowed()<5:
                       member.addBook(book)
                       book.setLibraryUser(member)
                    else:
                        print("The user has borrowed more the 5 books")
                else:
                    print("Book is currently borrowed by another member")

            else:
                 print("Book does not exist in catalogue")

    def returnBookToLibrary(self, book, damage, messageDamage):
        """It returns a book from a library member and changes the availability of the book or sets any damages"""
        if self.checkElementInLibrary(book):
            book.getLibraryUser().removeBook(book)
            book.setLibraryUser(None)
            if damage is True :
                book.setDamages(messageDamage)
                print("Book returned with damages" )
            else:
                print("Book returned without any damages")
        else:
            print("Book does not exist in catalogue")

    def getMemberNamesWithBookBorrowed(self):
        """Gets all members who borrowed books"""
        listMemberBorrow=[]
        for book in self.listOfLibraryResources:
            if isinstance(book, PhysicalBook):
                if book.checkBookAvailability()==False:
                    listMemberBorrow.append(book.getLibraryUser().getNameMember())
        return listMemberBorrow

    def getMemberWithBookBorrowed(self):
        """Gets all members who borrowed books"""
        listMemberBorrow=[]
        for book in self.listOfLibraryResources:
            if isinstance(book, PhysicalBook):
                if book.checkBookAvailability()==False:
                    listMemberBorrow.append(book.getLibraryUser())
        return listMemberBorrow

    def messageToMembers(self, message):
        """Sets any messages for members who borrowed a book"""
        for member in self.getMemberWithBookBorrowed():
            member.setMessages(message)
            print("Mesage to {} has been sent".format(member.getNameMember()))

    def printDetailsPhysicalBooks(self):
        """Prints all the books and resources in the catalogue."""
        for resource in self.listOfLibraryResources:
            if isinstance(resource, PhysicalBook):
                resource.printPhysicalBookDetails()

    def printDetailsElectronicBooks(self):
        """Prints the electronic resources in the catalogue."""
        for resource in self.listOfLibraryResources:
            if isinstance(resource, ElectronicResources):
                resource.printElectronicResourcesDetails()
