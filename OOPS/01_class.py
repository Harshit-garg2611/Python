class Employee:
    company = "HP"
    def get_salary(self): # self is important here as it refers to instance of class that is being created 
        return 34000



print(Employee().get_salary())

# Here Employee() : is a call of constructor to create object of this class
# It automatically creates an instance of class employee i.e. : object 


# NOW SELF : 
"""
Inside a class,  self  is like saying “this particular object.” It’s
a way for the object to refer to itself. It’s always the first parameter in a
method definition, but Python handles it automatically when you call the
method. You don’t type  self  when calling the method; Python inserts it for
you
"""

e2 = Employee()
print(e2.get_salary())
print(e2.company)
