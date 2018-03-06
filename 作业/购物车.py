goods_list = {
             'iphone6': {'price':6000,'num':10,'sum':10,'buy':0},
             'ipad': {'price':3000,'num':20,'sum':20,'buy':0},
             'mi4': {'price':2000,'num':43,'sum':43,'buy':0},
             'huawei6_plus': {'price':1999,'num':8,'sum':8,'buy':0},
}

def loging(admin, pwd):
    with open('身份信息', 'r') as f:
        for i in f:
            admin1 , pwd1 , balance = i.strip().split()
            if admin == admin1 and pwd == pwd1:
                print('成功登录')
                return balance
        else:
            pass

def show_goods(goods_dict):
    print('序号'' 物品'' 价格'' 当前数量'" 产品总数")
    goods_list = {}
    num = 1
    for k in goods_dict:
        print(num, k ,goods_dict[k]['price'],goods_dict[k]['num'], goods_dict[k]['mun'])
        num += 1
        goods_list[num]=([k , goods_dict[k]['price'],goods_dict[k]['num'], goods_dict[k]['mun'],goods_dict[k]['buy']])
    return goods_list
def buy_car(good_list ):
    print('序号'' 物品'' 价格'' 当前数量'" 产品总数"' 购买数量')
    for i in good_list:
        print(i, goods_list[i][0], goods_list[i][1], goods_list[i][2], goods_list[i][3], goods_list[i][4])



admin = input('请输入用户名：')
pwd  = input('请输入密码')
change_money = loging(admin,pwd)
buy_goods_list = {}
first_flag = 1
while first_flag:
    goods_dict = show_goods(goods_list)
    shop_index = input('请输入商品编号|购物车(S)|余额充值(M)|结账(J)')
    if shop_index == 'q':
        exit(0)
    if shop_index == 's':
        buy_car(buy_goods_list)
    if shop_index == 'm':
        pass
    if shop_index == 'j':
        pass
    if int(shop_index) in goods_dict:
        print('序号:%s'' 物品:%s'' 价格；%s'' 当前数量:%s'" 产品总数:%s"% (shop_index, goods_dict[shop_index][0],goods_dict[shop_index][1], goods_dict[shop_index][2],goods_dict[shop_index][3]))
        flag_seconde = 1
        while first_flag:
            buy_num = input('请输入购买的数量>>：')
            if buy_num =='q':
                exit(0)
            if buy_num == 'b':
                break
            if int(buy_num) == 0:
                pass
            if int(buy_num)>0 and int(buy_num)<= goods_dict[shop_index][3]:
                buy_goods_list[shop_index] = [goods_dict[shop_index][0],goods_dict[shop_index][1], goods_dict[shop_index][2],goods_dict[shop_index][3],buy_num]

