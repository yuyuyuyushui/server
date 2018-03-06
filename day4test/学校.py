class School(object):
    def __init__(self,name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.stuff = []
    def register(self, stu_obj):
        print('%s is registed'%stu_obj.name)
        self.students.append(stu_obj)
    def hire(self,teach_obj):
        print('%s is hired'%teach_obj.name)
        self.stuff.append(teach_obj)
class Schoolnumber(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
class Teacher(Schoolnumber):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print('''
        name:%s
        age:%s
        sex:%s
        salary:%s
        course system:%s
        '''%(self.name,self.age,self.sex,self.salary,self.course))
    def teach(self,):
        print('%s is teaching %s'%(self.name,self.course))
class Stutent(Schoolnumber):
    def __init__(self,name, age, sex, stu_id, grade):
        super(Stutent,self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade
        self.money  = 5000
    def tell(self):
        print('''
        name:%s
        age:%s
        sex:%s
        stu_id:%s
        grade:%s
        '''%(self.name,self.age,self.sex,self.stu_id,self.grade))
    def pay(self):
        print('%s has paied $%s'%(self.name, self.money))
school = School('老男孩','成都')
s1 = Stutent('fan', 23, 'M', 20161314, 5000)
s1.tell()

t1 = Teacher('luo', 25, 'M', 1000, 'Python')
t2 = Teacher('du',24, "MF", 2000, 'JAVA')
t2.tell()
school.register(s1)
print(school.students[0].name)
for stu in school.students:
    stu.pay()