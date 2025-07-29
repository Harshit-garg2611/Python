class Employee:
    
    company = "MPL"
    def __init__(self,name,salary,department):  # this is constructor
        self.name=name  # create instance attribute of name and assign it the value name.
        self.salary=salary
        self.department=department
    
    def get_name(self):
        return self.name
    
    
    def get_salary(self):
        return self.salary
    
    
    def get_department(self):
        return self.department
    
    
    def get_info(self):
        return f"My name is {self.name} and my salary is {self.salary}. I am {self.department} in {self.company}"
    
    
e = Employee("Harshit",8000000,"Data Engineer")
print(e.department) # this is the property of class employee
print(e.get_department()) # this is method or function of class employee
print(e.get_info())

