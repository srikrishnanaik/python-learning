#!/usr/bin/env python3
class Student:

    def __init__(self, name, major):
        self.name = name
        self.major = major
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property