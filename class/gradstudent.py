#!/usr/bin/env python3
from student4 import Student

class GradStudent(Student):

    def __init__(self, name, major, stipend):
        super().__init__(name, major)
        self.stipend = stipend

    @property
    def stipend(self):
        return self._stipend
    
    @stipend.setter
    def stipend(self, stipend):
        self._stipend = stipend
    
    def __str__(self):
        return "{} {}".format(super().__str__(), self.stipend)