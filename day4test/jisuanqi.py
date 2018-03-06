import re
def chengchu(cheng):
    for i in cheng:
        if i == '*':
             


def diu_add(str1):   #去加减
    diu_add=[]
    lst_diu = re.findall('[^+-]+', str1)
    for i in range(len(lst_diu))

        if lst_diu[i].isdigit():
            diu_add.insert(i,lst_diu[i])
        else:
            chengchu(lst_diu[i])





    #return str2

def cal(lst):#去括号
#     kuang = []
#     # for i in range(len(lst)):
#         shuzi = re.search('[^(].+[^)]',lst(i))
#         num = diu_add(shuzi)
#         kuang.append(num)
#     return kuang
    shuzi = re.search('[^(].+[^)]',lst).group()
    str=diu_add(shuzi)
    return str

num = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
r = re.findall('\([^()]+\)', num)
kuang = []
for i in range(len(r)):
    num = cal(r[i])
    kuang.append(num)

print(r)