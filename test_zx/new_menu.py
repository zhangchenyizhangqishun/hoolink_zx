# -*- coding:utf-8 -*-

menu = {
    "陕西":{
        "西安":{
            "高薪区":{
                "高新一中":"",
                "高新一小":""
            },
            "莲湖区":{
                "远东一小":"",
                "庆安小学":""
            }
        },
        "渭南":{
            "韩城":{
                "桑树坪小学":""
            }
              },
        "咸阳":{
            "旬邑":{
                "土桥小学":""
            }
        }
    },
    "上海":{
        "浦东区":"",
        "徐家汇":""
    },
    "浙江":{
        "杭州市":{
            "滨江区":{
                "英飞特":"",
                "大华":""
            }
        }
    }
}

current_layer = menu
# parent_layer = menu
perent_layers = []   # 保存所有的父级
while True:
    for key4 in current_layer:
        print key4
    chioe3 = raw_input(">>>").strip()
    if len(chioe3) == 0:continue
    if chioe3 in current_layer:
        # parent_layer = current_layer    # 将父层赋值给了变量parent_layer
        perent_layers.append(current_layer)  # 将每次的key值村入到perent_layer列表中
        current_layer = current_layer[chioe3]  # 将输入的子层赋值给了变量current_layer
    elif chioe3 == 'q':
        if perent_layers:    # 对最底层的列表做非空判断，不为空才进行删除和赋值
            current_layer = perent_layers.pop()  # 每次返回的时候将列表最后一个的值删除掉 并取出，因为是当前循环的key值
            # current_layer = parent_layer    # 将父层再次赋值给current_layer
    else:
        print "无此项"
        break

#
# 作业：（19-20day）
# 1 实现加减乘除及括号优先级解析
# 1 - 2 * ( (60-30 + (-40/5) + (9-2*5/3 + 7 /3*99/4*2988 + 10 * 568/14)) - (-4*3) / (16- 3*2))