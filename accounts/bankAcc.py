class Account:  ################################# Class

    def __init__(self, filepath):         ######## Constructor
        self.filepath = filepath          ######## Instance Variable
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):           ######## Class Methods
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

#account=Account(r"C:\Users\sai kiran pothula\PycharmProjects\Exercises\venv\mypythonexercises\accounts\balance.txt")

class CheckingAcc(Account):
    """ This is a sub class to Acoount which is base class an example for inheritance in python"""
    type = "checking"    ########### Class Variable

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
#Object Instance
jacks_checking = CheckingAcc(r"C:\Users\sai kiran pothula\PycharmProjects\Exercises\venv\mypythonexercises\accounts\jacks.txt", 2)
print(jacks_checking.balance)
jacks_checking.deposit(10)
print(jacks_checking.balance)
jacks_checking.transfer(100)
print(jacks_checking.balance)
jacks_checking.commit()
#Instantiation creating an object of a class
johns_checking = CheckingAcc(r"C:\Users\sai kiran pothula\PycharmProjects\Exercises\venv\mypythonexercises\accounts\johns.txt", 2)
print(johns_checking.balance)
johns_checking.deposit(10)
print(johns_checking.balance)
johns_checking.transfer(100)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.__doc__) ##### Prints the class description between doc string quotes using __doc__
