class Role:
    n = 123 #类变量
    n_list = []
    def __init__(self, name, role, weapon, size,life_value=100, money=80 ):
        self.name = name#实例变量（静态属性），作用域就是实例本体
        self.role = role
        self.weapons = weapon
        self.life_value = life_value
        #self.money = money
        self.n = size
 #   def __del__(self):
 #       print('%s died' %self.name)
    def shot(self):#类的方法，功能（动态属性）
        print('shoting me')
    def buy_gun(self):
        print('i have buy gun！'%self.weapons)
    def got_shot(self, new):
        print('i have got gun %s',new)
#print(Role.n)
r1 = Role('luo', 'police','AK47',222)#把一个类变成具体的对象的过程叫实例化
# r1.bullet='bullet'
# #r1.n = '改变量'
# print(r1.n, r1.name,r1.bullet,r1.got_shot('nihao'))
#
# r2 = Role('du', 'fanren', 'AK')
# print(r2.n)
# #Role.n='AD'
#
# print(r1.n, r2.n)
print(r1.n)