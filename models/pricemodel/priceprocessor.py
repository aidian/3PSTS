#-*-coding:utf-8-*-
import math

minGoldLine = 0.382
maxGoldLine = 0.618
minGsjLine = 0.125
maxGsjLine = 0.875
sMaxLine = 1.618
isError = 0






























isRisingReturnPrice = 1 # 是否上升回调
minPrice = 12.74 # 最低价格
maxPrice = 15.22 #最高价格


htPrice = 14.23 # 上升一笔后的回调价格
curPrice = 2680 # 当前价格

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
    print("-----------------------------上升回落买入卖出结论-----------------------------------------------------")

    sp1 = pow(maxPrice, maxGoldLine) * pow(minPrice, minGoldLine)
    sp2 = math.sqrt(maxPrice * minPrice)
    sp3 = pow(maxPrice, minGoldLine) * pow(minPrice, maxGoldLine)

    tp1 = (maxPrice / minPrice) * htPrice
    tp2 = pow(maxPrice / minPrice, sMaxLine) * htPrice
    sMaxGsj = pow(minPrice, maxGsjLine) * pow(maxPrice, minGsjLine)

    print("上升回落第一关 %.2f 若支撑住，大概率继续上升，突破压力位第一关（乐观谨慎） %.2f 突破压力位第二关（非常谨慎） %.2f 最大突破关（非常危险）：%.2f" % (sp1, tp1, tp2, sMaxGsj))
    print("上升回落第二关 %.2f 大概率震荡，谨慎操作！！！" % sp2)
    print("上升回落第三关 %.2f 大概率继续下跌，禁止买入！！！" % sp3)
    print("上升回落最大关 %.2f 大概率创新低，禁止买入！！！" % sMaxGsj)

    # if curPrice >= sp1:
    #     print("小心操作，准备买入，还未跌破第一关：%.2f 最大下跌空间：%.2f%%" %(sp1,(curPrice - sp1) / curPrice * 100))
    #
    # if curPrice > sp1 and curPrice <= tp1:
    #     print ("买入后第一关压力位：%.2f 上升空间：%.2f%%" % (tp1, (tp1 - curPrice) / curPrice * 100))
    #
    # if curPrice > tp1 and curPrice <= tp2:
    #     print ("突破第一关压力位：%.2f 第二关压力位：%.2f 上升空间：%.2f%%" %(tp1,tp2,(tp2 - curPrice) / curPrice * 100))

if isError == 0 and isRisingReturnPrice == 0:
    # 下降趋势反弹
    print("-----------------------------下跌反弹买入卖出结论-----------------------------------------------------")

    xp3 = pow(maxPrice, maxGoldLine) * pow(minPrice, minGoldLine)
    xp2 = math.sqrt(maxPrice * minPrice)
    xp1 = pow(maxPrice, minGoldLine) * pow(minPrice, maxGoldLine)
    xMaxGsj = pow(maxPrice, maxGsjLine) * pow(minPrice, minGsjLine)
    print("下跌反弹P1 %.2f 随时平仓！！！" % xp1)
    print("下跌反弹P2 %.2f 大概率震荡" % xp2)
    print("下跌反弹P3 %.2f 大概率继续上升" % xp3)
    print("下跌反弹G %.2f 大概率开始回落" % xMaxGsj)

    # if curPrice < xp1:
    #     print ("禁止买入！！！随时准备平仓！！！，下跌反弹还未突破第一关：%.2f，还需要升高：%.2f%%" %(xp1, (xp1 - curPrice) / curPrice * 100))
    #
    # if curPrice >= xp1 and curPrice < xp2:
    #     print ("大概率震荡！！！非常小心操作，随时准备平仓，下跌反弹距离第二关：%.2f，还需要升高%.2f%%" %(xp2, ((xp2 - curPrice) / curPrice * 100)))
    #
    # if curPrice >= xp2 and curPrice < xp3:
    #     print ("突破第二关，非常小心操作！！！大概率震荡，距离第三关：%0.2f 还需要升高：%.2f%%" %(xp3,((xp3 - curPrice) / curPrice * 100)))
    #
    # if curPrice >= xp3:
    #     print("突破第三关，非常危险，随时平仓！！！距离最大警告点：%0.2f 上升空间：%.2f%%" %(xMaxGsj,((xMaxGsj - curPrice) / curPrice * 100)))





