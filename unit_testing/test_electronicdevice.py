# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:50:24 2019

@author: catalin
"""

import unittest
from main_implementation.electronicdevice import ElectronicDevice

class TestElectronicDevice(unittest.TestCase):
    """Test class for ElectronicDevice """
    def testgetLocationDevice(self):
        """Test setLocationDevice and getLocationDevice functions ."""
        device1 = ElectronicDevice()
        device1.setLocationDevice('F2R4S12P1') #floor 2, row 4, shelf 12, position 1
        
        self.assertEqual(device1.getLocationDevice(), 'F2R4S12P1')
     

    def testgetDeviceType(self):
        """Tests setDeviceType and getDeviceType functions."""
        device1 = ElectronicDevice()
        device1.setDeviceType('Kindle')
      
        self.assertEqual(device1.getDeviceType(), 'Kindle')


    def testcheckAvailability(self):
        """Tests setDeviceAvailability and checkAvailability functions . """
        device1 = ElectronicDevice()
        device2 = ElectronicDevice()
        device1.setDeviceAvailability(True)
        device2.setDeviceAvailability(False)
        self.assertTrue(device1.checkAvailability())
        self.assertFalse(device2.checkAvailability())
      


if __name__ == '__main__':
    unittest.main()