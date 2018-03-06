__author__ = "Alex Li"
import test_pickle
import pickle
import sys
import os
from conf import setings

new=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

new1=os.path.join(new, 'day3\Atm')
sys.path.append(new1)
print(sys.path)


setings.loggings()
# def sayhi(name):
#     print("hello2,",name)
#
# print(sys.path)
# f = open('test.txt',"rb")
#
# data = pickle.loads(f.read())
# print(test_pickle.sayhi('new'))
# print(data)
# print(data["func"]("luo"))