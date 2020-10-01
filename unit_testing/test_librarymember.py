# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:43:15 2019

@author: catalin
"""

import unittest
from main_implementation.librarymember import LibraryMember
from main_implementation.physicalbook import PhysicalBook

class TestLibraryMember(unittest.TestCase):
    """Test class for library member """
    def testGetAndSetLibraryUser(self):
        """ Tests setNameMember and getNameMember functions"""
        user1= LibraryMember()
        user1.setNameMember("John")
        self.assertEqual(user1.getNameMember(), "John")
        
        
    def testPrintAllBorowedBooksByUser(self):
        user1= LibraryMember()
        """Tests printAllBorowedBooksByUser method"""
        user1.printAllBorowedBooksByUser()
        self.assertEqual(user1.listBooksBorrowed, [])
        user1.setMessages('Library closes at 2PM')
        self.assertEqual(user1.notifications, "Library closes at 2PM" )
        book2=PhysicalBook
        user1.addBook(book2)
        self.assertIn( [(book2)] ,user1.listBooksBorrowed)

        user1.printAllBorowedBooksByUser()
        user1.printLibraryMemberDetails()
        user1.numberOfBooksBorrowed()

#  
if __name__ == '__main__':
    unittest.main()