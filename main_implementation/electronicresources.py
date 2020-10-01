# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:52:07 2019

@author: catalin
"""
from main_implementation.electronicdevice import ElectronicDevice

class ElectronicResources:

    """ Class to represent the electronic resources"""

    def __init__(self):
        self.listDevices= [] # contains variables of type ElectronicDevices
        self.ISBN= 0
        self.ebookTitle= "not set"
        self.ebookAuthor= "not set"


    def setListDevices(self, list):
        """Sets the list of devices"""
        self.listDevices = list

    def setISBN(self, isbn):
        """Sets the ISBN for a resource"""
        self.ISBN= isbn

    def setEBookTitle(self, title):
        """Sets the title of ebook"""
        self.ebookTitle= title

    def setEBookAuthor(self, author):
        """Sets the author of ebook"""
        self.ebookAuthor= author


    def getISBN(self):
        """Gets the ISBN of ebook"""
        return self.ISBN

    def getEBookTitle(self):
        """Gets the title of ebook"""
        return self.ebookTitle

    def getEBookAuthor(self):
        """Gets the author of ebook"""
        return self.ebookAuthor


    def printElectronicResourcesDetails(self):
        """ Prints the list of electronic resource details"""
        print("{}, by {}, ISBN:{}. This electronic resource can be accessed on:".format(self.ebookTitle,self.ebookAuthor,self.ISBN))
        for device in self.listDevices:
            device.printElectronicDevicesDetails()

    def addElectronicDevices(self, device):
        """ Adds a electronic device from ElectronicDevice class"""
        assert type(device) is ElectronicDevice, "This is not an ElectronicDevice type object"
        if device in self.listDevices:
            print("The device is already in list")
        else:
            self.listDevices.append(device)
            print("Device added successfully")
