class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width  # use an underscore to indicate a private attribute
        self.height = height  # use an underscore to indicate a private attribute

    # define the getter method for width
    @property
    def width(self):
        return self._width

    # define the setter method for width
    @width.setter
    def width(self, value):
        if type(value) is not int:  # use isinstance for type checking
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    # define the getter method for height
    @property
    def height(self):
        return self._height

    # define the setter method for height
    @height.setter
    def height(self, value):
        if type(value) is not int:  # use isinstance for type checking
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
