# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:52:07 2019

@author: catalin
"""

import unittest
from main_implementation.physicalbook import PhysicalBook
from main_implementation.librarymember import LibraryMember

class TestPhysicalBook(unittest.TestCase):
    """Test class for physical book. """

    def testGetAndSetBookTitle(self):
        """Tests the setBookTitle and getBookTitle functions."""
        book1=PhysicalBook()
        self.assertEqual(book1.getBookTitle(), "not set")
        book1.setBookTitle("Pride and Prejudice")
        self.assertEqual(book1.getBookTitle(), "Pride and Prejudice")


    def testGetAndSetBookAuthor(self):
        """Tests setBookAuthor and getBookAuthor functions"""
        book1=PhysicalBook()
        self.assertEqual(book1.getBookAuthor(),"not set")
        book1.setBookAuthor("Jane Austen")
        self.assertEqual(book1.getBookAuthor(), "Jane Austen")


    def testGetAndSetLibraryUser(self):
        """Tests setLibraryUser and getLibraryUser functions"""
        book1= PhysicalBook()
        self.assertIsNone(book1.getLibraryUser())
        book1.setLibraryUser("John")
        self.assertEqual(book1.getLibraryUser(), "John")

    def testSetDamages(self):
        """Tests setDamages and getDamages functions"""
        book1= PhysicalBook()
        book1.setDamages("Front cover bent at right corner")
        self.assertEqual(book1.getDamages(), ":Front cover bent at right corner")
        book1.setDamages("Second page scribbled")
        self.assertEqual(book1.getDamages(), ":Front cover bent at right corner:Second page scribbled" )


    def testCheckBookAvailability(self):
        """ Tests checkBookAvailability function """
        book1= PhysicalBook()
        self.assertEqual(book1.checkBookAvailability(), True)
        member1 = LibraryMember()
        book1.setLibraryUser(member1)
        self.assertEqual(book1.checkBookAvailability(), False)


#    def testPrintPhysicalBookDetails(self):
#        """ Tests printPhysicalBookDetails , not working"""
#        book1 = PhysicalBook()
#        book1.setISBN(9781503290563)
#        book1.setLibraryUser(None)
#        book1.setDamages('Back cover right corner: scribbled')
#        book1.setBookTitle('Pride and Prejudice')
#        book1.setBookAuthor('Jane Austen')
#        self.assertEqual(book1.printPhysicalBookDetails(), "Pride and Prejudice, by Jane Austen ISBN:9781503290563, with the following damages::Back cover right corner: scribbled" +"\n"+
#                         "This book is available")
        

if __name__ == '__main__':
    unittest.main()