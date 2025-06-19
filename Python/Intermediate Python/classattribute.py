class Employee():
    company = "Google"
    salary = 100
    
    # @staticmethod
    # def showDetails():
    #     print("This is a static method salary is {salary}".format(salary = self.salary))

    @classmethod
    def showDetails(cls):
        print("This is a class method salary is {salary}".format(salary = cls.salary))

e = Employee()
e.salary = 300
e.showDetails()

# note: the decorator @classmethod is used to define a class method. A class method is a method that is bound to the class and not the object of the class. It takes cls as the first parameter and can access class variables and methods.