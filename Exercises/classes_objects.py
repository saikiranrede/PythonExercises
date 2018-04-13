lottery_player_dict = {
    'name': 'Sai',
    'numbers': (1, 2, 3, 4, 5)
}

class LotteryPlayers:
    def __init__(self, name):
        self.name = 'Sai'
        self.name = name
        self.numbers = (1, 2, 3, 4, 5)

    def total(self):
        return sum(self.numbers)

player1 = LotteryPlayers("Sai")
player2 = LotteryPlayers("Reddy")
player1.numbers = (4, 5, 6, 4, 7)

#print(player1.name)
#print(player1.numbers)
#print(player1.total())

#print(player1 == player2)
#print(player1.name == player2.name)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod                 #classmethod is used if the method does only one action
    def going_to_school(cls):    #in classmethod cls is passed instead of self which passes Student itself not the object(self)
        print("I am going to school")
        print("I'm a {}".format(cls))  #I'm a <class '__main__.Student'>

    @staticmethod
    def going_to_work():
        print("I am going to school")


student = Student("Kiran", "CSU")
student.marks.append(56)
student.marks.append(86)

#print(student.marks)
#print(student.average())
Student.going_to_school()    # Doesn't matter who is calling it, cuz, it does the same thing
Student.going_to_work()      #Why not call it with the class itself
