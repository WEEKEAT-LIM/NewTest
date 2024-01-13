# 创建一个“学生”类，储存姓名、班级、学号、分数。把以下需求封装成不同的函数：

# 1. 可以在创建实例对象时自动初始化信息，并且自动加入列表
# 2. 一个用来储存所有“学生”的列表
# 3.  一个可以根据学生的分数由高到低输出资料学生的函数
# 4. 搜索学生姓名来输出该学生的资料
# 5. 一个用来计算平均分数的函数

STUDENTS = []

class Student:
    
    def __init__(self, name:str, Class:str, id:int, marks:int):
        self.Name = name
        self.Class = Class
        self.ID = id
        self.Marks = marks
        STUDENTS.append(self)
    
    def AvgMarks(self):
        total_marks = 0
        for j in STUDENTS:
            if type(j) != Student:
                return None
            total_marks += j.Marks
        return total_marks/len(STUDENTS)

def SearchByName(name:str):
        for i in STUDENTS:
            if type(i) != Student:
                return None
            if i.Name == name:
                print(f"Name: {i.Name}\t Class: {i.Class} \t ID: {i.ID} \t Marks: {i.Marks}")
                return True
        print("Student Not Found")
        return None

def Sort():
    isSwap = True
    for i in range(len(STUDENTS)):
        for j in range(len(STUDENTS)-i-1):
            if STUDENTS[j].Marks < STUDENTS[j+1].Marks:
                temp = STUDENTS[j]
                STUDENTS[j] = STUDENTS[j+1]
                STUDENTS[j+1] = temp
                isSwap = True
            else:
                isSwap = False
        if isSwap == False:
            return STUDENTS
    return STUDENTS


A = Student("A", "S3C1", 19021, 50)
B = Student("B", "S3C1", 19022, 90)
C = Student("C", "S3C1", 19023, 60)
D = Student("D", "S3C1", 19024, 100)
new = Sort()
for i in new:
    print(f"Name: {i.Name}\t Class: {i.Class} \t ID: {i.ID} \t Marks: {i.Marks}")

print("for test branch")