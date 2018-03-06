china = {
    "华南": {
        "广东": ["广州市", "佛山市", "深圳市", "东莞市"],

        "广西": ["南宁市", "柳州市", "桂林市", "北海市"],

        "海南": ["海口市", "三亚市", "三沙市", "儋州市"]

    },
    "华东": {
        "上海": ["黄浦区", "卢湾区", "徐汇区", "长宁区", "普陀区"],

        "安徽": ["合肥市", "芜湖市", "淮南市", "马鞍山市"],

        "江苏": ["南京市", "无锡市", "徐州市", "常州市", "苏州市"]

    },
    "华北": {
        "北京": ["东城区", "西城区", "朝阳区", "丰台区", "石景山区", "海淀区"],

        "山西": ["太原市", "大同市", "阳泉市", "长治市"],

        "河北": ["石家庄市", "唐山市", "秦皇岛市", "邢台市"]

    },
    "华中": {
        "湖北": ["武汉市", "黄石市", "十堰市", "十堰市"],

        "河南": ["郑州市", "开封市", "洛阳市", "平顶山市"],

        "湖南": ["长沙市", "株洲市", "衡阳市", "邵阳市"]

    },
    "西南": {
        "重庆": ["万州区", "涪陵区", "渝中区", "大渡口区"],
        "四川": ["成都市", "自贡市", "攀枝花市", "德阳市"],
        "贵州": ["贵阳市", "六盘水市", "遵义市", "安顺市"],

    },
    "特别行政区": {
        "香港": ["屯门", "弯仔", "北角", "西贡"],
        "澳门": ["花地玛堂区", "圣安多尼堂区", "大堂区", "望德堂区"],

    },

}


def selectChina(currentGroup, history):#history列表用来装字典
    print("Choice Menu. 'b' for back to upper menu, 'q' for exit.")
    for i1 in currentGroup:
        print(i1)
    choice = input('enter your choice: ')
    if choice == 'b':
        if len(history) <= 0:#返回最顶层菜单
            print("it is top menu.")
            return selectChina(china, [])
        else:
            return selectChina(history.pop(), history)#pop方法导出最后一个值，并返回
    if choice == 'q':
        exit()
    if choice in currentGroup:
        try:
            #currentGroup[choice]
            history.append(currentGroup)
            return selectChina(currentGroup[choice], history)
        except:
            print("it is last menu.")
    return selectChina(currentGroup, history)

selectChina(china, [])