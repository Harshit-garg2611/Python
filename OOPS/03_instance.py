# Instance and class attribute :
class Employee:
    
    company = "MPL" # This is class attribute
    
    
    def __init__(self,name,salary,department,company):  # this is constructor
        self.name=name  # create instance attribute of name and assign it the value name.
        self.salary=salary
        self.department=department
        self.company=company  # this is instance of class 
    
    def get_name(self):
        return self.name
    
    
    def get_salary(self):
        return self.salary
    
    
    def get_department(self):
        return self.department
    
    
    def get_company(self):
        return self.company
    
    
    def get_info(self):
        return f"My name is {self.name} and my salary is {self.salary}. I am {self.department} in {self.company}"
    
    
    
e1 = Employee("Alok",354323,"Civil Engineer","Afcons")


# This will always print istance of class if it is present
print(e1.company)


