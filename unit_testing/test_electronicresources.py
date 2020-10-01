# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:51:07 2019

@author: catalin
"""
import sys
import io
import unittest
from main_implementation.electronicresources import ElectronicResources
from main_implementation.electronicdevice import ElectronicDevice

class TestElectronicResources(unittest.TestCase):
    """Test class for ElectronicResources """
    def testgetISBN(self):
        """Test setISBN and getISBN functions"""
        ebook1 = ElectronicResources()
        #ebook1.setListDevices([device1, device2])
        ebook1.setISBN(9780316485616)
        #ebook1.setEBookTitle('The Night Fire')
        #ebook1.setEBookAuthor('Harry Bosch')
        self.assertEqual(ebook1.getISBN(),9780316485616)

    def testgetEBookTitle(self):
        """Tests setEBookTitle and getEBookTitle Functions"""
        ebook1 = ElectronicResources()
        ebook1.setEBookTitle('The Night Fire')
        self.assertEqual(ebook1.getEBookTitle(), 'The Night Fire')

    def testgetEBookAuthor(self):
        """Tests setEBookAuthor and getEBookAuthor functions"""
        ebook1 = ElectronicResources()
        ebook1.setEBookAuthor('Harry Bosch')
        self.assertEqual(ebook1.getEBookAuthor(), 'Harry Bosch')


#    def printElectronicResourcesDetails(self):
#        """ Prints the list of electronic resource details"""
#        print("{}, by {}, ISBN:{}. This electronic resource can be accessed on:".format(self.ebookTitle,self.ebookAuthor,self.ISBN))
#        for device in self.listDevices:
#            device.printElectronicDevicesDetails()
#             
    def testaddElectronicDevices(self):
        """ Adds a electronic device from ElectronicDevice class"""
        device1 = ElectronicDevice()
        device1.setDeviceType('Kindle')
        device1.setLocationDevice('F2R4S12P1') #floor 2, row 4, shelf 12, position 1
        device1.setDeviceAvailability(True)
        
        device2 = ElectronicDevice()
        device2.setDeviceType('Tablet')
        device2.setLocationDevice('F2R4S12P2') #floor 2, row 4, shelf 12, position 2
        device2.setDeviceAvailability(False)   
        
        ebook1 = ElectronicResources()
        ebook1.setListDevices([device1])
        ebook1.setISBN(9780316485616)
        ebook1.setEBookTitle('The Night Fire')
        ebook1.setEBookAuthor('Harry Bosch')
        ebook1.addElectronicDevices(device2)
       
        #unit test for console print from StackOverflow
        output = io.StringIO()                  # Create StringIO object
        sys.stdout = output                     #  and redirect stdout.
        ebook1.addElectronicDevices(device1)
        print ('Captured', output.getvalue())

if __name__ == '__main__':
    unittest.main()