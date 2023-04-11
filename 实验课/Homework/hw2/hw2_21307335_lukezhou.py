import os
class Stu:
    def __init__(self,str):
        str.strip();
        data=str.split(' ')
        self.name=data[0]
        self.stu_num=data[1]
        self.gender=data[2]
        self.age=int(data[3])
def by_name(stu):
    return stu.name;
def by_schoolnum(stu):
    return stu.stu_num;
def by_gender(stu):
    return stu.gender;
def by_age(stu):
    return stu.age;
class StuData(Stu):
    def __init__(self,textname):
        self.data = []
        with open(textname,'r') as f:
            for line in f:
                self.data.append(Stu(line))
    def SortData(self,str):
        if str=="name":
            self.data.sort(key=by_name)
        elif str=="stu_num":
            self.data.sort(key=by_schoolnum)
        elif str=="gender":    
            self.data.sort(key=by_gender)
        elif str=="age":        
            self.data.sort(key=by_age)
    def AddData(self,name, stu_num, gender, age):
        self.data.append(Stu(name+" "+stu_num+" "+gender+" "+str(age)))
    def ExportFile(self,newfilename):
        with open(newfilename, 'a+') as f:
            for stu in self.data:
                print(stu.name,stu.stu_num,stu.gender,stu.age,file=f)

        
if __name__ == '__main__':
    # 测试程序
    os.chdir('E:\desktop\Stu\\2023AI\Experiments\Homework\hw2')
    s1 = StuData('student_data.txt')
    s1.AddData(name="Bob", stu_num="003", gender="M", age=20)
    s1.SortData('age')
    s1.ExportFile('new_stu_data.txt')