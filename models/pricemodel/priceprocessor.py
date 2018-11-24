#-*-coding:utf-8-*-
import  math

minGoldLine = 0.382
maxGoldLine = 0.618
minGsjLine = 0.125
maxGsjLine = 0.875
sMaxLine = 1.618
isError = 0






















isRisingReturnPrice = 0 # 是否上升回调
minPrice = 30 # 最低价格
maxPrice = 33.89 #最高价格


htPrice = 92.58 # 上升一笔后的回调价格
curPrice = 93 # 当前价格

print("-----------------------------原始数据-----------------------------------------------------")

print("最高价格 %.2f" %maxPrice)
print("最低价格 %.2f" %minPrice)
print("回落价格 %.2f" %htPrice)
print("当前价格 %.2f" %curPrice)

# 校验错误
if maxPrice < minPrice:
    isError = 1
    print ("警告：最大价格小于最小价格")
if htPrice < minPrice:
    isError = 1
    print ("警告：回调价格小于最小价格")
if isRisingReturnPrice == 1 and htPrice > maxPrice:
    isError = 1
    print ("警告：回调价格大于最高价格")

if curPrice <= 0 or curPrice < minPrice:
    isError = 1
    print ("警告：当前价格异常")

print("-----------------------------买入卖出结论-----------------------------------------------------")

if  isError == 0 and isRisingReturnPrice == 1:
    # 上升趋势回调
    sp1 = pow(maxPrice, maxGoldLine) * pow(minPrice, minGoldLine)
    sp2 = math.sqrt(maxPrice * minPrice)
    sp3 = pow(maxPrice, minGoldLine) * pow(minPrice, maxGoldLine)
    sMaxGsj = pow(minPrice, maxGsjLine) * pow(maxPrice, minGsjLine)

    tp1 = (maxPrice / minPrice) * htPrice
    tp2 = pow(maxPrice / minPrice, sMaxLine) * htPrice
    # print("上升回落P1 %.2f 突破TP1 %.2f 突破TP2 %.2f" % (sp1, tp1, tp2))
    # print("上升回落P2 %.2f" % sp2)
    # print("上升回落P3 %.2f" % sp3)
    # print("上升反弹G %.2f" % sMaxGsj)

    if htPrice >= sp1:
        print("可以买入，上升回落第一关：%.2f 高于第一关：%.2f%%" %(sp1,(htPrice - sp1) / sp1 * 100))

    if curPrice <= tp1:
        print ("买入后第一关压力位：%.2f 上升空间：%.2f%%" % (tp1, (tp1 - curPrice) / curPrice * 100))

    if curPrice > tp1 and curPrice <= tp2:
        print ("突破第一关压力位：%.2f 第二关压力位：%.2f 上升空间：%.2f%%" %(tp1,tp2,(tp2 - curPrice) / curPrice * 100))

if isError == 0 and isRisingReturnPrice == 0:
    # 下降趋势反弹
    xp3 = pow(maxPrice, maxGoldLine) * pow(minPrice, minGoldLine)
    xp2 = math.sqrt(maxPrice * minPrice)
    xp1 = pow(maxPrice, minGoldLine) * pow(minPrice, maxGoldLine)
    xMaxGsj = pow(maxPrice, maxGsjLine) * pow(minPrice, minGsjLine)
    print("下跌反弹P1 %.2f" % xp1)
    print("下跌反弹P2 %.2f" % xp2)
    print("下跌反弹P3 %.2f" % xp3)
    print("下跌反弹G %.2f" % xMaxGsj)





