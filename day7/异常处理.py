class LuoError(Exception):#继承异常
    def __init__(self, message):
        self.name = message
    def __str__(self):
        return 'sffdd'
try:
    raise LuoError('数据库连接错误')
except LuoError as e :
    print(e)