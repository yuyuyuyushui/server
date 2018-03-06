def talk(self):
    print('%s is talking '%self.name)
class Dog(object):
    def __init__(self, name):
        self.name = name
    def eat(self):
        print('%s is eating'%self.name)

p = Dog('du')
#print(p)
#print(p.eat)
choice = input('pleae input a func:').strip()

if hasattr(p, choice):#判断输入字符串是否是类下的函数
    getattr(p,choice)()#获取输入字符串的方法
    print(getattr(p,choice))
    # setattr(p, choice, '陈')#修改属性的值
    # print(p.name)
else:
    setattr(p,choice,talk)#创建函数并根据输入的方法名字命名方法
    v = getattr(p, choice)(p) #获取命名函数的方法与外部函数的传入


     # setattr(p, choice, 23)#创建属性的值
     # print(getattr(p,choice))