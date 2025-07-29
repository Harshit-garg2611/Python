'''
 # Inheritance :
    Inheritance is like a family tree. A child class (or subclass) inherits traits (attributes
    and methods) from its parent class (or superclass). This allows you to create new
    classes that are specialized versions of existing classes, without rewriting all the
    code.
'''

class Animal: # Parent class (superclass)
    
    
    location = "Local"
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("Generic animal sound")
        
    def eat(self):
        print("Food to eat")
        
# a = Animal("Dog")
# a.speak()

# inherit parent class 

class Dog(Animal):
    
    '''
# super() :
    Inside a child class,  super()  lets you call methods from the parent
    class. This is useful when you want to extend the parent’s behavior instead of
    completely replacing it. It’s especially important when initializing the parent
    class’s part of a child object.
'''

    def speak(self):
        super().speak()
        print("Bhaw bhaw !")
        
    def eat(self):
        return super().eat()
        
        
d = Dog("Tomy")
# d.speak()
# print(d.location,d.name)

d.eat()



'''
Polymorphism, as we saw with the  speak()  method in the inheritance example,
means that objects of different classes can respond to the same method call in
their own specific way. This allows you to write code that can work with objects of
different types without needing to know their exact class
'''


class Bird(Animal):
    
    def speak(self):
        print("chirp")
        
        
        
        
b = Bird("Kamo")
b.speak()




