""" Write a function distance_between_points(p1, p2) that takes two points 
and returns the Cartesian distance between them.
 """

import math

class Point:
    """Represents a point in a 2D space"""

def distance(point_a,point_b):
    dis=math.sqrt((point_a.x-point_b.x)**2+(point_a.y-point_b.y)**2)
    return dis

point_a=Point()
point_b=Point()
point_a.x=0
point_a.y=1
point_b.x=4
point_b.y=2

""" Create a Fraction() class with only the basic attributes. Assume that the inputs are numbers.
a. Override some operators so that you can add a Fraction to an integer (Fraction() + int only,
 not int + Fraction()).
b. Override the operator that allows you to check which fraction is larger between the two.
 """

class Fraction:
    """ 
    Models a fraction with a numerator and a denominator, assuming the inputs are numbers
    Attributes:
    num - int, float - numerator
    denom - int, float - denomerator
    value - num/denom
    Methods:
    Can be added and compared to other fractions
    """
    def __init__(self, num=int, denom=int):
        self.num=num
        self.denom=denom
        if self.denom == 0:
            self.value = None
        else:
            self.value = num / denom
    
    def __str__(self):
        return f"{self.num}/{self.denom} (= {self.value})"
    
    def __add__(self, other):
        if isinstance(other, int):
            num_int=self.denom*other
            return Fraction(self.num+num_int,self.denom)

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.value > other.value
        elif isinstance(other, int):
            return self.value > other

""" Create a Path() class, symboling a directory in a mock filesystem. 
The class should at least one attribute, named files, containing the list of files in the folder, 
and three methods, not including the mandatory __init__ method:

Path.get_parent() - returns the name of the parent folder of our Path (not the entire path). 
The Path.get_size() - returns a number corresponding to the size in KB of the folder, 
which should depend on the number of files in the folder.
Path.set_path(Path()) - Change the current directory to the one given (as a Path() instance).
After you've created it, overload the division operator / (__truediv__) to concatenate a Path class instance with a string pointing to a folder."""

import os, os.path

class Path:
    """ 
    File system path to folders, allows the use of "/" to move between folders
    Attributes:
    path - str
    files - list of str
    
    Methods:
    get_parent - returns parent folder as Path
    get_size - returns size of current folder in KB
    set_path(new_path) - changes current path to the .path attribute of new_path
    """
    def __init__(self, path, files=['a.txt', 'b.py', 'c.c']):
        self.path=path
        self.files=files

    def get_parent(self):
        return os.path.abspath(os.path.join(self.path, os.pardir))
    
    def get_size(self):
        folder_size = 0
        for (path, dirs, files) in os.walk(self.path):
            for file in files:
                filename = os.path.join(path, file)
                folder_size += os.path.getsize(filename)
            return folder_size/1024
    
    def set_path(self, new_path):
        self.path = new_path.path
        self.files = new_path.files
    
    def __truediv__(self, other):
        """ 
        Traverse the filesystem using the / sign, assuming that 
        other isn't an absolute path.
        Returns a new instance
        """
        assert type(other) in (str, int)
        new_path = self.path + os.sep + str(other)
        new_files = []
        return Path(path=new_path, files=new_files)

p=Path(r"C:\Users\happy\Videos\Legion (2017) Season 3 S03 (1080p AMZN WEB-DL x265 HEVC 10bit AAC 5.1 Vyndros)", files=["Legion.S03E01.Chapter.20.1080p.10bit.AMZN.WEB-DL.AAC5.1.HEVC-Vyndros.mkv","Legion.S03E02.Chapter.21.1080p.10bit.AMZN.WEB-DL.AAC5.1.HEVC-Vyndros.mkv"])
print(p.path, p.files)

size = p.get_size()
parent = p.get_parent()
print(f"Size: {size}")
print(f"parent: {parent}")
