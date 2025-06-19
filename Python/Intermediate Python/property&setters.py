# abastraction and encapsulation in python 
# using property and setter

class Employee():
    company = "Google"
    salary = 100
    
    @property
    def name(self):
        return self.firstname + " " + self.lastname

    @name.setter
    def name(self, val):
        self.firstname = val.split(" ")[0]
        self.lastname = val.split(" ")[1]



e = Employee()
e.name = input("Enter your full name:")
print(e.firstname, e.lastname)