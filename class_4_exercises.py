""" The Vector Class
Create a Vector() class that simulates a 1D vector array. 
Assume the inputs to the class are valid. The Vector instance should have at least two (relevant) attributes.
a. Override some dunder method(s) so that you're able to add either an integer or a different vector to a vector.
b. Override some dunder method(s) so that you're able to check which of the two vectors is bigger, element-wise. 
The ouput is another vector with the corresponding True and False values. """

class Vector:
    """simulates a 1D vector array."""

    def __init__(self, data):
        self.data=list(data)
        self.length = len(self.data)

    def __len__(self):
        """Allows us to call len() on the vector"""
        return self.length
    
    def __add__(self, other):
        if isinstance(other,int):
            for datum in self.data:
                datum+=other
            return self
        elif isinstance(other,Vector):
            assert len(self) == len(other)
            new_vec=[]
            for i, j in zip(self.data, other.data):
                new_vec.append(i+j)
            return new_vec
    
    def __gt__(self, other):
        assert(type.other==Vector)
        assert len(self) == len(other)
        ans = [i>j for i,j in zip(self.data,other.data)]
        return Vector(ans)

