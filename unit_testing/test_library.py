# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:52:19 2019

@author: catalin
"""

import unittest
from main_implementation.library import Library
from main_implementation.librarymember import LibraryMember
from main_implementation.physicalbook import PhysicalBook


class TestLibrary(unittest.TestCase):
    """Test class for Library """
    def testcheckElementInLibrary(self):
        """Checks if resourceX is in the catalogue list. """
        
        book1 = PhysicalBook()
        book1.setISBN(9781503290563)
        book1.setLibraryUser(None)
        book1.setDamages('Back cover right corner: scribbled')
        book1.setBookTitle('Pride and Prejudice')
        book1.setBookAuthor('Jane Austen')


        book2 = PhysicalBook()
        book2.setISBN(9781853261756)
        book2.setLibraryUser(None)
        book2.setDamages('Front cover right corner: bent')
        book2.setBookTitle('The Idiot')
        book2.setBookAuthor('Fyodor Dostoevsky')

        book3 = PhysicalBook()
        book3.setISBN(9780156792011)
        book3.setLibraryUser(None)
        book3.setBookTitle('The Sacred and the Profane')
        book3.setBookAuthor('Mircea Eliade')

        book4 = PhysicalBook()
        book4.setISBN(9789739432108)
        book4.setLibraryUser(None)
        book4.setDamages('Second page right corner: bent')
        book4.setBookTitle('Poems and Prose')
        book4.setBookAuthor('Mihai Eminescu')

        book5 = PhysicalBook()
        book5.setISBN(9780156792011)
        book5.setLibraryUser(None)
        book5.setBookTitle('The Sacred and the Profane')
        book5.setBookAuthor('Mircea Eliade')
        
        listResources = [book1, book2, book3]
        mylibrary = Library()
        mylibrary.setLibraryName('The Library')
        mylibrary.setListOfLibraryResources(listResources)
        
        self.assertTrue(mylibrary.checkElementInLibrary(book1))
        self.assertFalse(mylibrary.checkElementInLibrary(book5))
     
        
    def testlengthOfResources(self):
        """Returns the number of resources and books in the catalogue."""
        book1 = PhysicalBook()
        book1.setISBN(9781503290563)
       
        book2 = PhysicalBook()
        book2.setISBN(9781853261756)
        

        book3 = PhysicalBook()
        book3.setISBN(9780156792011)
       
        book4 = PhysicalBook()
        book4.setISBN(9789739432108)
       
        book5 = PhysicalBook()
        book5.setISBN(9780156792011)
       
        
        listResources = [book1, book2, book3]
        mylibrary = Library()
        mylibrary.setLibraryName('The Library')
        mylibrary.setListOfLibraryResources(listResources)
        
        self.assertEqual(mylibrary.lengthOfResources(), len(listResources))
        
        
    def testgetMemberNamesWithBookBorrowed(self):
        """Gets all members who borrowed books"""
        user1 = LibraryMember()
        user1.setNameMember('John Cusack')
        user1.setMemberID(31)
        
        user2 = LibraryMember()
        user2.setNameMember('Liv Tyler')
        user2.setMemberID(24)
        
        book1 = PhysicalBook()
        book1.setISBN(9781503290563)
       
        book2 = PhysicalBook()
        book2.setISBN(9781853261756)
        

        book3 = PhysicalBook()
        book3.setISBN(9780156792011)
       
        book4 = PhysicalBook()
        book4.setISBN(9789739432108)
       
        book5 = PhysicalBook()
        book5.setISBN(9780156792011)
       
        
        listResources = [book1, book2, book3, book4, book5]
        mylibrary = Library()
        mylibrary.setLibraryName('The Library')
        mylibrary.setListOfLibraryResources(listResources)
        
        #also verifies .lendBookToMember function
        mylibrary.lendBookToMember(user2, book5)
        mylibrary.lendBookToMember(user1, book3)
       
        
        self.assertEqual(mylibrary.getMemberNamesWithBookBorrowed(), ['John Cusack', 'Liv Tyler'])
        
        
#  
if __name__ == '__main__':
    unittest.main()