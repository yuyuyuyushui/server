#python3中类的类的重构
class MyType(type):
    def __init__(self,what, bases=None, dict=None):
        super(MyType, self).__init__(what, bases, dict)
        # self=Foo
        print(123)
        pass

    def __call__(self, *args, **kwargs):
        # self=Foo
        obj = self.__new__(self, *args, **kwargs)

        self.__init__(obj)



class Foo(object,metaclass=MyType):
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

    def func(self):
        print('hello wupeiqi')

Foo('luo')