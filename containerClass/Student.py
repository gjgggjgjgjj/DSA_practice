
class Student:
    def __init__(self, fName="", lName="",  email="", age=0, ssn=""):
        self.fName = fName 
        self.lName = lName
        self.email = email
        self.age = int(age)
        self.ssn = ssn

    def __eq__(self, rhs):
        return self.ssn == rhs.ssn

    def getSsn(self):
        return self.ssn
    #insert
    #traverse and print ars age
    #delete
    #retrive
