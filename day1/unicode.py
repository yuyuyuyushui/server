import sys
print(sys.getdefaultencoding())
s = '你好'
print(s.encode("gbk").decode("gbk"))