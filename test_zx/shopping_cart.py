#-*- coding: utf8 -*-

commodity_list = [
    ('book',60),
    ('MacBook Pro',9000),
    ('cigarette',10),
    ('toys',600),
]
#raw_input() 将所有输入作为字符串看待，返回字符串类型。而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）
money = raw_input("请输入你的账户余额[退出：q]：")
goods_purchased = []




#判断输入的是否为数字
if money.isdigit():
    money = int(money)
    #循环显示商品列表
    while True:
        #根据列表的索引获取对应的值
        for i,v in enumerate(commodity_list,1):
            print (i,v)

        commodity_id = raw_input("请输入你要选择的商品编号[退出：q]")
        if commodity_id.isdigit():
            commodity_id = int(commodity_id)
            #判断获得的索引是否在列表的索引内
            if commodity_id>0 and commodity_id<=len(commodity_list):
                p_itrm = commodity_list[commodity_id-1]
                if p_itrm[1] < money:
                    money = money - p_itrm[1]
                    goods_purchased.append(p_itrm[0])
                    print "您购买的商品为%s，您的余额为%s" % (goods_purchased, money)
                else:
                    print "您的余额不足,现在余额为%s，所买商品价格为%s"%(money,p_itrm[1])
            else:
                print "您输入的编码不存在"

        elif commodity_id == 'q':
            a = {}
            for z in goods_purchased:
                if goods_purchased.count(z)>1:
                    a[z] = goods_purchased.count(z)
                    print a
            print "您购买的商品为%s，您的余额为%s"%(goods_purchased,money)
            break
        # 不在索引范围的抛出异常
        else:
            print "您输入的编号不正确，请重新输入！"

#判断输入的是否为quit退出
elif money== 'q':
    print '欢迎下次光临'
    #提示购物车内的已购买商品和剩余的金额

    #提示欢迎下次再来
#判断非数字，抛出异常
else:
    print '您输入的金额包含非法字符'