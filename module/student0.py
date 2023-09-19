#!/usr/bin/env python3
""" This module defines a Student datatype and a main function to demonstrate the instantiation of a Student object"""

class Student:
    """This class represents a Student. This multiline string will act as a doc string since it is declared at the top of the class"""

def main():
    """This main function is for testing purpose only. This Student class will be imported by another module"""
    jeff = Student()
    heather = Student()
    print(jeff, id(jeff), hex(id(jeff)))
    print(heather, id(heather), hex(id(heather)))

if __name__ == "__main__":
    main()


