# FileName: ps9.py
# Author: Chaitra Kothari
# Date: Nov 12th, 2015
# Description: In this problem set, you will be creating and using classes and methods. Along the way, you should become familiar with concepts
#such as inheritance and overriding methods. 

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Triangle(Shape):
    def __init__(self, b, h):
        """
        h: height of triangle
        b: base of triangle
        """
        self.height = h
        self.base = b
    def area(self):
        """
        Returns area of triangle
        """
        return 0.5 * self.base * self.height
    def __str__(self):
        return 'Triangle with base ' + str(self.base) + ' and height ' + str(self.height)
    def __eq__(self, other):
        """
        Two triangles are equal if they have same base and height
        """
        return type(other) == Triangle and self.height == other.height and self.base == other.base


class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.shapeSet = []

    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        if sh in self.shapeSet: raise ValueError('Shape already exists')
        self.shapeSet.append(sh)
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        self.place = 0
        return self

    def next(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        if self.place >= len(self.shapeSet):
            raise StopIteration
        self.place += 1
        return self.shapeSet[self.place - 1]

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        for sh in self.shapeSet:
            if type(sh) == Circle:
                print sh
        for sh in self.shapeSet:
            if type(sh) == Square:
                print sh
        for sh in self.shapeSet:
            if type(sh) == Triangle:
                print sh
        return ''
 

#test
ss = ShapeSet()
ss.addShape(Circle(4.0)) 
ss.addShape(Square(4.0))
ss.addShape(Square(1.0))
ss.addShape(Triangle(1.0, 1.0))
print(ss)      
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    area = {}
    for sh in shapes:
        area[sh] = sh.area()
    largest = max(area, key = area.get)
    print (largest)


#test
ss = ShapeSet()
ss.addShape(Circle(4.0)) 
ss.addShape(Square(4.0))
ss.addShape(Square(1.0))
ss.addShape(Triangle(1.0, 1.0))
print(ss)
findLargest(ss)

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    shapeFile = open(filename)
    ss = ShapeSet()
    for line in shapeFile:
        fields = line.strip().split(',')
        shape = fields[0]
        if shape == 'circle':
            radius = float(fields[1])
            c = Circle(radius)
            ss.addShape(c)
        elif shape == 'square':
            side = float(fields[1])
            s = Square(side)
            ss.addShape(s)
        else:
            height = float(fields[1])
            base = float(fields[2])
            t = Triangle(height, base)
            ss.addShape(t)
    print (ss)

#test
os.getcwd()
os.chdir('/Users/admin/Documents/GitHubCode/Python-MIT OCW/ProblemSet9')
os.listdir(os.getcwd())
path = 'shapes.txt'
readShapesFromFile(path)



