goods_list = {
             'iphone6': {'price':6000,'num':10,'sum':10},
             'ipad': {'price':3000,'num':20,'sum':20},
             'mi4': {'price':2000,'num':43,'sum':43},
             'huawei6_plus': {'price':1999,'num':8,'sum':8},
}
def show_goods(goods_dict):
    print('序号'' 物品'' 价格'' 当前数量'" 产品总数")
    goods_list = {}
    num = 1
    for k in goods_dict:
        print(num, k ,goods_dict[k]['price'],goods_dict[k]['num'], goods_dict[k]['sum'])
        num += 1
        goods_list[num]=([k , goods_dict[k]['price'],goods_dict[k]['num'], goods_dict[k]['sum']])
    return goods_list
goods_dict = show_goods(goods_list)
print(goods_dict)