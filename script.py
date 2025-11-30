# class Student:
#     count = 0
#     def __init__(self,name="Вася",height=155):
#         #self.height=155
#         #print(self.height)
#         self.name=name
#         self.height=height
#         Student.count+=1
#     def info(self):
#         print(self.name,self.height)
#
# st1=Student()
# # Student.__init__(self=st1)
# st2=Student("Петя",height=158)
# st3=Student("Саша",height=162)
# print("Ім'я та ріст студентів")
# st1.info()
# st2.info()
# st3.info()
# print("Кількість",Student.count)

class Pet:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pet.count+=1
    def info(self):
        print("Тварина: ",self.name, ", Вік:",self.age)

pet1 = Pet('Кіт', 3)
pet2= Pet('Собака', 5)
pet3 = Pet('Черепаха', 1)
pet1.info()
pet2.info()
pet3.info()
#print("Тварина: " + pet1.name, ", Вік:" + str(pet1.age))
#print("Тварина: " + pet2.name, ", Вік:" + str(pet2.age))
#print("Тварина: " + pet3.name, ", Вік:" + str(pet3.age))
print("Всього тварин:",Pet.count)