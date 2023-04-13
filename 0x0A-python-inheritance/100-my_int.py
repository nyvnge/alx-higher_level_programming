#!/usr/bin/python3
"""
class MyInt
"""


class MyInt(int):
    """integer"""
    def __new__(cls, *args, **kwargs):
        """new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
