class Point:
    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
    def sum(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    
    def __add__(self, other): # Overloading the + operator
#  'other' refers to the object on the *right* side of the +
        return Point(self.x + other.x, self.y + other.y)
    
    
    def __str__(self): # String representation (for print() and str())
        return f"({self.x}, {self.y})"
    
    
    def __eq__(self, other): # Overloading == operator
        return self.x == other.x and self.y == other.y
    
    
    
p1 = Point(1, 2)
p2 = Point(3, 4)


# print(p1.sum(p2))

p3 = p1 + p2  # This now works!  It calls p1.__add__(p2)


print(p3) # Output: (4, 6)  (This uses the __str__ method)

print(p1 == p2) # Output: False (This uses the __eq__ method)


'''Other useful magic methods: (You don’t need to memorize them all, but be aware
they exist!)
__sub__  ( - ),  __mul__  ( * ),  __truediv__  ( / ),  __eq__  ( == ),  __ne__
( != ),  __lt__  ( < ),  __gt__  ( > ),  __len__  ( len() ),  __getitem__ , 
__setitem__ ,  __delitem__'''