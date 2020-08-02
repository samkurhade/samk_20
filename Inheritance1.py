# inheritance
class Employee:
    no_of_leaves = 10

    def __init__(self , aname , asalary , arole):  # This is a constructor "__init__"
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):  # This is not a constructor its another function
        return f"The name is {self.name}. salary is {self.salary} and role is {self.role}"

    @classmethod            # This is a classmethod
    def change_leaves(cls , newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        # params = string.split("_")
        # print(params)
        # return cls(params[0],params[1], params[2])
        return cls(*string.split("_"))

    @staticmethod      # This is a static method
    def printgood(string):
        print("This is good" +   string)

class Programmer(Employee):   #  This is a single inheritance . using creating another class .here we can access all the methods and attributes by using programmer class of employee class.s
    def __init__(self,aname , asalary , arole ,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
         return f"The name is {self.name}. salary is {self.salary} and role is {self.role} and languages are {self.languages}"

sam = Employee("Sam" , 500 , "Student")
rohan = Employee("Rohan" , 657, "Instructor")


karan = Employee.from_dash("Karan_345_Student")

sandy = Programmer("sandy",456,"programmer" ,["Python","cpp"])

print(sandy.printprog())
print(sandy.no_of_leaves) # we can access the employee class variable also

# Here employee class is parent class


