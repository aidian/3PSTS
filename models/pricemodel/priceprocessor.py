#-*-coding:utf-8-*-
import math

minGoldLine = 0.382
maxGoldLine = 0.618
minGsjLine = 0.125
maxGsjLine = 0.875
sMaxLine = 1.618
isError = 0






























isRisingReturnPrice = 0 # 是否上升回调

minPrice = 1506.6 # 最低价格
maxPrice = 1876.2 #最高价格


htPrice = 0 # 上升一笔后的回调价格

curPrice = 1510 # 当前价格

print("-----------------------------原始数据-----------------------------------------------------")

print("最高价格 %.2f" %maxPrice)
print("最低价格 %.2f" %minPrice)
print("回落价格 %.2f" %htPrice)
print("当前价格 %.2f" %curPrice)





















# 校验错误
if maxPrice < minPrice:
    isError = 1
    print ("警告：最大价格小于最小价格")
if htPrice > maxPrice:
    isError = 1
    print ("警告：回调价格大于最大价格")
if isRisingReturnPrice == 1 and htPrice > maxPrice:
    isError = 1
    print ("警告：回调价格大于最高价格")

if curPrice <= 0 or curPrice < minPrice:
    isError = 1
    print ("警告：当前价格异常")

if  isError == 0 and isRisingReturnPrice == 1:
    # 上升趋势回调
    print("-----------------------------上升回调买入卖出结论-----------------------------------------------------")

    sp1 = pow(maxPrice, maxGoldLine) * pow(minPrice, minGoldLine)
    sp2 = math.sqrt(maxPrice * minPrice)
    sp3 = pow(maxPrice, minGoldLine) * pow(minPrice, maxGoldLine)

    sp1yaliwei = pow(maxPrice, maxGsjLine) * pow(sp1, minGsjLine)
    sp2yaliwei = pow(maxPrice, maxGsjLine) * pow(sp2, minGsjLine)
    sp3yaliwei = pow(maxPrice, maxGoldLine) * pow(sp3, minGoldLine)

    tp1 = (maxPrice / minPrice) * htPrice
    tp2 = pow(maxPrice / minPrice, sMaxLine) * htPrice

    if htPrice >0 and curPrice <= sp3:
        print("上升回调第三关【%.2f】，大概率继续下跌，创新低，该回调价格对应的压力位，【下跌反弹第三关】【%.2f】，禁止买入！！！平仓！平仓！平仓！" % (sp3, sp3yaliwei))

    if  htPrice >0 and curPrice > sp3 and curPrice < sp2:
        print("上升回调第二关【%.2f】，大概率震荡，该回调价格对应的压力位，【下跌反弹最大甘氏角】【%.2f】，谨慎操作！！！" % (sp2, sp2yaliwei))

    if  curPrice > sp2 and htPrice > 0:
        if curPrice >= htPrice and curPrice < sp1yaliwei:
            print(
                    "上升回调第一关，当前价格【%.2f】，将会面对第一压力位（当前回调价格对应的下跌反弹最大甘氏角）【%.2f】，大概率震荡，谨慎操作！！！" % (curPrice, sp1yaliwei))
        if curPrice >= sp1yaliwei and curPrice < maxPrice:
            print("回调突破第一压力位【%.2f】，将会面对第二压力位（当前最高价格）【%.2f】，大概率继续创新高，谨慎操作！！！" % (sp1yaliwei, maxPrice))
        if curPrice > maxPrice and curPrice < tp1:
            print("已创新高【%.2f】，将面对压力位【%.2f】，有可能再次下跌，非常谨慎操作，逃顶！！！" % (curPrice, tp1))
        if curPrice >= tp1 and curPrice < tp2:
            print("再次创新高【%.2f】，将面对压力位【%.2f】，大概率再次下跌，非常危险，逃顶！！！" % (curPrice, tp2))
        if curPrice >= tp2:
            print("平仓！平仓！平仓！别人贪婪时，我恐惧！！！")

    if htPrice <= 0:
        print("上升回调第一关【%.2f】，没有确认回调价格，禁止买入！！！" % sp1)
        print("上升回调第二关【%.2f】，没有确认回调价格，禁止买入！！！" % sp2)
        print("上升回调第三关【%.2f】，没有确认回调价格，禁止买入！！！" % sp3)


if isError == 0 and isRisingReturnPrice == 0:
    # 下降趋势反弹
    print("-----------------------------下跌反弹买入卖出结论-----------------------------------------------------")

    xp3 = pow(maxPrice, maxGoldLine) * pow(minPrice, minGoldLine)
    xp2 = math.sqrt(maxPrice * minPrice)
    xp1 = pow(maxPrice, minGoldLine) * pow(minPrice, maxGoldLine)
    xMaxGsj = pow(maxPrice, maxGsjLine) * pow(minPrice, minGsjLine)
    print("下跌反弹第一关【%.2f】，大概率创新低，禁止买入！！！平仓！平仓！平仓！" % xp1)
    print("下跌反弹第二关【%.2f】，大概率震荡，谨慎操作！！！" % xp2)
    print("下跌反弹第三关【%.2f】，大概率继续上升或回落，非常谨慎操作！！！" % xp3)
    print("下跌反弹最大甘氏角【%.2f】，大概率创新高或快速回落，非常谨慎操作！！！" % xMaxGsj)




