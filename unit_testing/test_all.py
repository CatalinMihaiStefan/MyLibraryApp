# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:32:57 2019

@author: catalin
"""


from main_implementation.library import Library
from main_implementation.librarymember import LibraryMember
from main_implementation.physicalbook import PhysicalBook
from main_implementation.electronicresources import ElectronicResources
from main_implementation.electronicdevice import ElectronicDevice

def test():
  """Test all the classes created, their methods and the connections between them. """  
  """first set all the parameters for all the objects"""
  device1 = ElectronicDevice()
  device1.setDeviceType('Kindle')
  device1.setLocationDevice('F2R4S12P1') #floor 2, row 4, shelf 12, position 1
  device1.setDeviceAvailability(True)

  device2 = ElectronicDevice()
  device2.setDeviceType('Tablet')
  device2.setLocationDevice('F2R4S12P2') #floor 2, row 4, shelf 12, position 2
  device2.setDeviceAvailability(False)

  device3 = ElectronicDevice()
  device3.setDeviceType('Laptop')
  device3.setLocationDevice('F2R4S12P3') #floor 2, row 4, shelf 12, position 3
  device3.setDeviceAvailability(True)

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

  ebook1 = ElectronicResources()
  ebook1.setListDevices([device1, device2])
  ebook1.setISBN(9780316485616)
  ebook1.setEBookTitle('The Night Fire')
  ebook1.setEBookAuthor('Harry Bosch')

  user1 = LibraryMember()
  user1.setNameMember('John Cusack')
  user1.setMemberID(31)

  user2 = LibraryMember()
  user2.setNameMember('Liv Tyler')
  user2.setMemberID(24)

  listResources = [book1, ebook1, book2, book3]
  mylibrary = Library()
  mylibrary.setLibraryName('The Library')
  mylibrary.setListOfLibraryResources(listResources)

  """Testing ElectronicResources methods"""
  print(ebook1.getEBookTitle())
  print(ebook1.getEBookAuthor())
  print(ebook1.getISBN())

  ebook1.printElectronicResourcesDetails()
  ebook1.addElectronicDevices(device3)
  ebook1.addElectronicDevices(device2)

  """Testing LibraryMember methods"""
  print(user1.getMemberID())
  print(user1.getNameMember())

  user1.printAllMessages()
  user1.printAllBorowedBooksByUser()
  user1.setMessages('Library closes at 2PM')
  user1.addBook(book1)
  user1.printAllBorowedBooksByUser()
  user1.printLibraryMemberDetails()
  user1.numberOfBooksBorrowed()

  """Testing PhysicalBook methods"""
  print(book2.getBookTitle())
  print(book2.getBookAuthor())
  print(book2.getISBN())
  print(book2.getLibraryUser())
  print(book2.checkBookAvailability())
  book2.printPhysicalBookDetails()

  """Testing ElectronicDevice methods"""
  print(device1.getLocationDevice())
  print(device1.getDeviceType())
  device1.printElectronicDevicesDetails()
  print(device1.checkAvailability())
  print(device2.checkAvailability())

  """Testing Library methods"""
  
  """testing if it prints all the resources in the catalogue"""
  mylibrary.printAllDetailsLibrary()
  
  """checks if resource is in library catalogue"""
  print(mylibrary.checkElementInLibrary(book2))
  print(mylibrary.checkElementInLibrary(book4))
  
  """testing if method to change the title of a resource works
  mylibrary.changeTitleResource(book3, 'The Sacred and the Profane: The Nature of Religion')"""
 
  """testing if it works adding a new resource"""
  mylibrary.addAResource(book5)
  
  
  """testing if it works adding an already existing resource """
  mylibrary.addAResource(book1)
  
  """testing if it works to search by ISBN"""
  mylibrary.searchByISBN(9780156792011)
  
  """testing if it works to search catalogue by author"""
  mylibrary.searchByAuthor('Jane Austen')
  print('----')
  mylibrary.searchByAuthor('Harry Bosch')
  print('----')
  mylibrary.searchByAuthor('Mircea Eliade')
  
  """testing to see if it works to remove a resource from catalogue and by position"""
  mylibrary.removeResource(book1)
  mylibrary.removeResourceByPosition(1)
  mylibrary.displayAllAvaiableBooks()
  
  """test if it displays the correct number of resources"""
  print(mylibrary.lengthOfResources())
  mylibrary.addAResource(book5)
  
  """tests if lendBookToMember works properly, if it throws the correct error messages"""
  mylibrary.lendBookToMember(user2, book5)
  mylibrary.lendBookToMember(user1, book5)
  mylibrary.lendBookToMember(user1, book2)
  
  """tests if returnBookToLibrary works"""
  mylibrary.returnBookToLibrary(book5, False, '')
  mylibrary.getMemberNamesWithBookBorrowed()
  
  """send notification to all library members"""
  mylibrary.messageToMembers('Please return books')
  user1.printAllMessages()
  mylibrary.printDetailsPhysicalBooks()
  mylibrary.printDetailsElectronicBooks()
