#!/usr/bin/python3
"""MyList class inherits from list"""


class MyList(list):
    """Class which inherits from list"""
    def __init__(self):
        """initializing the object"""
        super().__init__()

    def print_sorted(self):
        """outputs the sorted list"""
        print(sorted(self))
