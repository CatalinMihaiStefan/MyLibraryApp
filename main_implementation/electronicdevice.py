# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:52:07 2019

@author: catalin
"""

class ElectronicDevice:

    """ Class to represent the electronic device"""

    def __init__(self):
        self.deviceAvailability= True
        self.locationDevice= "not set"
        self.deviceType="not set"


    def setDeviceAvailability(self, availability):
        """Sets the availability of the device."""
        self.deviceAvailability = availability

    def setLocationDevice(self, location):
        """Sets the location of device."""
        self.locationDevice= location

    def setDeviceType(self, type):
        """Sets the type of device, i.e. computer, tablet."""
        self.deviceType= type


    def getLocationDevice(self):
        """Gets the location of device"""
        return self.locationDevice

    def getDeviceType(self):
        """Gets the type of device, i.e. computer, tablet."""
        return self.deviceType


    def printElectronicDevicesDetails(self):
        """ Prints the electronic device details."""
        print("The location of the {} is:{} " .format(self.deviceType, self.locationDevice))
        if self.deviceAvailability== True:
            print("Device is available")
        else:
            print("Device not available")

    def checkAvailability(self):
        """Checks the availability of the device. """
        if self.deviceAvailability== True:
            return True
        else:
            return False
