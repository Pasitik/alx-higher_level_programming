#!/usr/bin/python3

"""
Contains a Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Base with a __init__ method """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializing class or instance attributes

        Args:
            id (int): an integer assignable to self.id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get the value of size """
        return self.width

    @size.setter
    def size(self, value):
        """ set the value for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ return a string representation of this instance """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    def update(self, *args, **kwargs):
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.size = args[1]
            elif i == 2:
                self.x = args[2]
            elif i == 3:
                self.y = args[3]

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "size":
                self.size = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value

        def to_dictionary(self):
            square_dict = {}
            square_dict["id"] = self.id
            square_dict["size"] = self.size
            square_dict["x"] = self.x
            square_dict["y"] = self.y

            return square_dict
