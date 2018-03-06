_author__ = "Alex Li"
#import json

import pickle
#import test_pickle_fan

#test_pickle_fan.sayhi()

def sayhi(name):
    print("hello,",name)

info = {
    'name':'alex',
    'age':22,
    'func':sayhi
}


f = open('test.txt',"wb")
#print(pickle.dumps(info))
#print(json.dumps(info))
f.write( pickle.dumps(info))

f.close()