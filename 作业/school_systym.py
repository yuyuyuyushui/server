import uuid,os, pickle
path = '/etc/down'

class School(object):#学校类
    date_path = path
    def __init__(self, name , school_addr):
        self.name  =  name
        self.course = []
        self.addr = school_addr
        self.classes = []
        self.uid = uuid.uuid1()
    def save(self):#存学校对象
        pickle.dump(self, open(os.path.join(School.date_path,self.uid), 'w'))
    def __str__(self):
        print('学校名字%s'%self.name)
    @staticmethod
    def get_all():
        obj_list = []
        for item in os.listdir(path):
            obj = pickle.load(item)
            obj_list = obj_list.append(obj)
        return obj_list
school_all_obj = School.get_all()
for school_obj in school_all_obj:
    print(school_obj)


class Course(object):#课程类
    def __init__(self, name, cycle, price):
        self.name = name
        self.cycle = cycle
        self.price = price


class Classes(object):#班级类
    date_path = path
    def __init__(self,semester, name):
        self.semester = semester
        self.name = name
        self.course = []
        self.teacher = []
        self.nid = uuid.uuid1()
    def save(self):#存班级对象
        pickle.dump(self, open(os.path.join(Classes.date_path,self.nid), 'w'))
    @staticmethod
    def get_all():
        obj_list = []
        for item in os.listdir(Classes.date_path):
            obj = pickle.load(item)
            obj_list = obj_list.append(obj)




class Teacher(object):
    def __init__(self, name):
        self.name = name
        self.classes = []
    def choice_class(self, obj_classes):
        print('you can choice class:%s'%obj_classes.name)
        self.classes.append(obj_classes)

class Students(object):
    date_path = path
    def __init__(self, name, class_obj_nid):
        """
        :param name: 学生名字
        :param class_obj_nid: 班级对象的序列号（）
        """
        self.name = name
        self.class_obj_nid = class_obj_nid
        self.uid = uuid.uuid1()
    def save(self):
        pickle.dump(self, open(os.path.join(Students.date_path, self.uid), 'w'))

    @staticmethod
    def get_all():
        obj_list = []
        for item in os.listdir(Students.date_path):
            obj = pickle.load(item)
            obj_list = obj_list.append(obj)
        return obj_list

class_obj_list= Classes.get_all()
sel = input('请输入班级对象的索引号：')
class_obj  = class_obj_list[sel]#在班级列表中选择出班级对象
print(class_obj_list[sel])
Students('李浩', class_obj.name)

student_obj = Students.get_all()
student_obj_single = student_obj[3]
num = student_obj_single.class_obj_nid
pickle.load(num)


