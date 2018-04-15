class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)

class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

sai =  WorkingStudent('Sai', 'MIT', 2000, 'Software Developer')
print(sai.salary)
kiran = WorkingStudent.friend(sai, 'Kiran', 2345, 'Software Developer')

print(kiran.name)
print(kiran.school)
print(kiran.salary)  #prints an error cuz, its not defined in the super class
print(kiran.job_title)                     #but when changed to @classmethod
