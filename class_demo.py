# class Student:
#     def __init__(self,name,hindi,english,maths):
#         self.name= name
#         self.hindi= hindi
#         self.english= english
#         self.maths= maths
#
#     def average(self):
#         avg= (self.hindi+self.maths+self.english)/3
#         print(avg)
#
#
# s1= Student("Deepak", 98,97,87)
# s1.average()

class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks= marks


    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hello my name is",self.name,"My average is",sum/3)


s1= Student("Deepak", [98,98,99])
s1.average()
