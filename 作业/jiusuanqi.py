import re
def settle(equation_str):
    flag1 = True
    while flag1:
        try:
            equation_str1 = re.search(' ', equation_str).group()
            equation_str = equation_str.replace(equation_str1, '')
        except AttributeError:
                flag1 =False
    flag2 = True
    while flag2:
        try:
            equation_str1 = re.search('\+-',equation_str).group()
            equation_str = equation_str.replace(equation_str1, '-')
        except AttributeError:
            flag2 = False
    return equation_str
def choose(equation_):
    equation_1=re.search('\([^()]+\)',equation_).group()
    return equation_1
def count(equation):


if __name__ == '__main__'
    equation = input('请输入你想计算的算式>>:').strip()##(12+41*())
    try:
        new_equation=choose(equation)#选出括号

    except AttributeError:
        count(equation)
    new_equation=settle(equation)
    choose(new_equation)
    except AttributeError:
        count(equation)



