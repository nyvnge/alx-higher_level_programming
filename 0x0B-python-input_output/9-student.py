#!/usr/bin/python3
"""
Student class
"""


class Student:
    """Student representation"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of the student instance"""
        return self.__dict__
