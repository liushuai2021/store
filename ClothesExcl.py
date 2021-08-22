
import xlrd

# 1.打开
WbAssress = xlrd.open_workbook(filename=r"C:\Users\刘帅\PycharmProjects\day07\2020年每个月的销售情况.xlsx")
strs=r"C:\Users\刘帅\PycharmProjects\day07\2020年每个月的销售情况.xlsx"
strs0="1月"
sales=4
price=2
goods=1
# goods = input("请输入商品所在列数")
# sales = input("请输入数量所在列数")
# price = input("请输入价格所在列数")
# 2.选中用户管理选项卡
st = WbAssress.sheet_by_name(strs0)
# 3.获取所有行  所有列
rows = st.nrows
cols = st.ncols
#存储商品与价格
Sales_Statistics = {}
month = 1
while month <= 12:  # 12月份 12张表
    Month_Sales = WbAssress.sheet_by_index(month - 1)  # 每月的表
    rows = Month_Sales.nrows
    for i in range(rows):
        data = Month_Sales.row_values(i)
        if data[1] == "服装名称":  # 第一行跳过
            pass
        else:
            if data[1] in Sales_Statistics:
                continue
            else:
                Sales_Statistics[data[1]] = {
                                             "单价": data[2]
                                             }
    month+=1


def fileAdress():
    strAdress= xlrd.open_workbook(filename=strs)
    return strAdress
#按行获取数据，返回列表
def getRows(str,add,begin):
    wb = fileAdress()
    str = wb.sheet_by_name(str)
    list = []
    data = str.row_values(add)[begin:]
    for i in range(len(data)):
        list.append(data[i])
    return list
#按列获取一列数据，返回列表
def getCols(str,add,begin):
    wb=fileAdress()
    str=wb.sheet_by_name(str)
    list=[]
    data=str.col_values(add)[begin:]
    for i in range(len(data)):
        list.append(data[i])
    return list
#求月销售额的方法
def salesVolume(strs0,price,sales):
    dataPrice = getCols(strs0,price,1)
    dataNumber = getCols(strs0,sales,1)
    sumlist = []
    for i in range(len(dataPrice)):
            sumlist.append(dataPrice[i] * dataNumber[i])
    return sum(sumlist)
#求单件衣服月销售件数方法
#参数goods:商品名,返回件数
def salesNumbr(goods,counts,ClothesList):
    nzkkey=[]
    sums=[]
    # counts = getCols(strs0, 4, 1)
    # ClothesList = getCols(strs0, 1, 1)
    # for key,value in enumerate(ClothesList):
    for i in range(len(ClothesList)):
        if ClothesList[i] == goods:
            num = i
            nzkkey.append(num)
        else:
            continue
        # for key,value in enumerate(nzkkey):
    for i in range(len(nzkkey)):
        sums.append(counts[nzkkey[i]])

    return sum(sums)
# counts = getCols(strs0, 4, 1)
# ClothesList = getCols(strs0, 1, 1)
# re = salesNumbr("风衣", counts, ClothesList)
# print(re)
#全年总销售额方法

#月总销售件数
def salesNumbrMonthAll(strs0,sales):
    counts = getCols(strs0, sales, 1)
    return  sum(counts)
def salesMoneyYearLoad(sales,price):
    month=getQuarterly(0)
    allsum=[]
    for i in range(len(month)):
        strs0=month[i]
        money=salesMoneyMonth(strs0,price,sales)
        allsum.append(money)
    # print(sum(allsum))
    return sum(allsum)
#获取季度
def getQuarterly(choose):
    month=[]
    if choose==0:
        month=["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
    elif choose==1:
        month = ["1月","2月","3月"]
    elif choose==2:
        month = ["4月","5月","6月"]
    elif choose==3:
        month = ["7月","8月","9月"]
    elif choose==4:
        month = ["10月","11月","12月"]
    return month
#-------------------------------------------------------------------------------------------

#月总销售额
#
def salesMoneyMonth(strs0,price,sales):
    list=salesVolume(strs0,price,sales)
    # print(strs0,"销售额为",list,"￥")
    return list
def salesMoneyMonthLoad(strs0,price,sales):
    list = salesMoneyMonth(strs0, price, sales)
    print(strs0, "销售额为", list, "￥")
#销售占比
def salesNumberMonth(strs0,sales,goods):
    strs0 = input("请输入查询月份")
    re0=[]
    resum=0
    good=input("请输入商品名")
    counts = getCols(strs0, sales, 1)
    ClothesList = getCols(strs0, goods, 1)
    re = salesNumbr(good, counts, ClothesList)
    re=int(re)
    list=getCols(strs0,sales,1)
    print(strs0,good,"销售占比为",re/sum(list))
#月销售件数最多商品
def saleMax(strs0,goods,sales):
    list=[]
    Number=[]
    counts = getCols(strs0, sales, 1)
    ClothesList = getCols(strs0, goods, 1)
    goodslist=getCols(strs0,goods,1)
    for key,value in enumerate(goodslist):
        if value in list:
            continue
        else:
            list.append(value)
    for i in range(len(list)):
        num= salesNumbr(list[i],counts,ClothesList)
        Number.append([num])
        # print(maxNumber)
    maxNumber=[]
    for key,value in enumerate(Number):
        maxNumber.append(value[0])
    for key,value in enumerate(maxNumber):
        if value==max(maxNumber):
            num0=key
            re=goodslist[key]
        else:
            continue
    print(strs0,"最畅销的商品：",re,"本月销售件数为",maxNumber[num0])
    return re,maxNumber[num0]
#销售额最少
def saleMin(strs0,goods,sales):
    list=[]
    Number=[]
    counts = getCols(strs0, sales, 1)
    ClothesList = getCols(strs0, goods, 1)
    goodslist=getCols(strs0,goods,1)
    for key,value in enumerate(goodslist):
        if value in list:
            continue
        else:
            list.append(value)
    for i in range(len(list)):
        num= salesNumbr(list[i],counts,ClothesList)
        Number.append([num])
        # print(maxNumber)
    minNumber=[]
    for key,value in enumerate(Number):
        minNumber.append(value[0])
    for key,value in enumerate(minNumber):
        if value==min(minNumber):
            num0=key
            re=goodslist[key]
        else:
            continue
    print(strs0,"最不畅销的商品：",re,"本月销售件数为",minNumber[num0])
# 每件衣服月销售额占比
def salesMoneyScaleMonth(price,goods,sales):
    good= input("请输入商品名")
    goodprice=Sales_Statistics[good]["单价"]
    counts = getCols(strs0, sales, 1)
    ClothesList = getCols(strs0,goods, 1)
    re = salesNumbr(good, counts, ClothesList)
    re=int(re)
    allSum=salesMoneyMonth(strs0,price,sales)
    print(good,"销售额占比:",(re*goodprice)/allSum)
    # return (reSum*292)/allSum
# 每件衣服年销售额
def salesMoneyScalesYear(good,goodprice,price,goods,sales):
    month=getQuarterly(0)
    year=[]
    for i in range(len(month)):
        strs0=month[i]
        counts = getCols(strs0, sales, 1)
        ClothesList = getCols(strs0, goods, 1)
        re = salesNumbr(good, counts, ClothesList)
        re = int(re)
        year.append(re*goodprice)
    clothesAll=sum(year)
    allSum=salesMoneyYear(sales,price)
    return clothesAll/allSum
def salesMoneyScalesYearLoad(price,goods,sales):
    good=input("请输入商品名")
    goodprice=Sales_Statistics[good]["单价"]
    re=salesMoneyScalesYear(good,goodprice,price,goods,sales)
    print(good,"年销售额",re)
#全年总销售额
def salesMoneyYear(sales,price):
    allsum=salesMoneyYearLoad(sales,price)
    print("全年销售额:",allsum)
    return allsum
#每季度销售总额
def salesMoneyQuarterly(sales,price):
    allsum = []
    print(info0)
    Quarterly=input("")
    Quarterly=int(Quarterly)
    month=getQuarterly(Quarterly)
    for i in range(len(month)):
        strs0 = month[i]
        money = salesMoneyMonth(strs0, price, sales)
        allsum.append(money)
    print(sum(allsum))
    return sum(allsum)
#单件衣服的年销售额
def salesMonryClothesCount(sales,goods):
    count=[]
    month = getQuarterly(0)
    good=input("请输入商品名")
    # price=input("请输入价格")
    price=Sales_Statistics[good]["单价"]
    for i in range(len(month)):
        counts = getCols(month[i], sales, 1)
        ClothesList = getCols(month[i], goods, 1)
        num=salesNumbr(good, counts, ClothesList)
        count.append(num*price)
    return sum(count)
#单件衣服全年销售额占比
def salesMonryClothes(sales,price):
    all=salesMoneyYear(sales, price)
    clothes=salesMonryClothesCount(sales,goods)
    print("全年销售额占比：",clothes/all)
#单件衣服的年销售件数
def salesYearClothesCount(good,sales,goods):
    count = []
    month = getQuarterly(0)
    # good = input("请输入商品名")
    for i in range(len(month)):
        counts = getCols(month[i], sales, 1)
        ClothesList = getCols(month[i], goods, 1)
        num=salesNumbr(good, counts, ClothesList)
        count.append(num)
    return sum(count)
#全年衣服的销售总件数
def salesYearClothesCounts(sales):
    month=getQuarterly(0)
    all=[]
    for i in range(len(month)):
        num=salesNumbrMonthAll(month[i], sales)
        all.append(num)
    return sum(all)
#每件衣服的年销售件数占比
def salesYearClothesCountsLoad(sales,goods):
    good=input("请输入商品名")
    count=salesYearClothesCount(good,sales,goods)
    all=salesYearClothesCounts(sales)
    print(good,"年销售件数占比",count/all)
#年销售件数最多的商品
def salesMaxYear(sales,goods):
    sumAll=[]
    goodsList=getCols(strs0, goods, 1)
    clothes=[]
    for key,value in enumerate(goodsList):
        if value in clothes:
            continue
        else:
            clothes.append(value)

    # for key,value in enumerate(clothes):
    for i in range(len(clothes)):
        monthNumber=salesYearClothesCount(clothes[i], sales, goods)
        sumAll.append(monthNumber)
    for i in range(len(sumAll)):
        if sumAll[i]==max(sumAll):
            num=i
        else:
            continue
    print(clothes[num],"今年最畅销的商品,共销售了",max(sumAll))
    return sumAll
#年销售件数最少的商品
def salesMinYear(sales,goods):
#年销售件数最少的商品
    month=getQuarterly(0)
    sumMin=[]
    goodsList=[]
    goodsList=getCols(strs0, goods, 1)
    clothes=[]
    for key,value in enumerate(goodsList):
        if value in clothes:
            continue
        else:
            clothes.append(value)

    # for key,value in enumerate(clothes):
    for i in range(len(clothes)):
        monthNumber=salesYearClothesCount(clothes[i], sales, goods)
        sumMin.append(monthNumber)
    for i in range(len(sumMin)):
        if sumMin[i]==min(sumMin):
            num=i
        else:
            continue
    print(clothes[num],"今年最不畅销的商品,共销售了",min(sumMin))
    return sumMin
#每个季度最畅销的商品方法
def salesMaxQuarterlyLoad(month,sales):
    monthcount=salesNumbrMonthAll(month, sales)
    return monthcount

#获取季度商品列表
def goodsList(choose,goods):
    monthQuarterly=[]
    month=getQuarterly(1)
    for i in range(len(month)):
         goodsList = getCols(month[i], goods, 1)
         monthQuarterly.append(goodsList[i])
    clothes = []
    for key, value in enumerate(goodsList):
        if value in clothes:
            continue
        else:
            clothes.append(value)
            # '休闲裤', '牛仔裤', '风衣', '皮草', 'T血', '衬衫', '羽绒服'
#     print(num)
    return clothes
#求季度单件数商品销售件数
def goodQuarterlyCount(choose,good):
    month=getQuarterly(choose)
    numMonth=[]
    for i in range(len(month)):
        counts = getCols(month[i], 4, 1)
        ClothesList = getCols(month[i], 1, 1)
        num=salesNumbr(good, counts, ClothesList)
        numMonth.append(num)
    return sum(numMonth)
#每个季度最畅销的商品
def salesMaxQuarterly(goods):
    print(info0)
    all=[]
    choose=input("")
    if choose.isdigit():
        choose=int(choose)
        clotheslist = goodsList(choose,goods)
        for i in range(len(clotheslist)):
            numQuarterly=goodQuarterlyCount(choose, clotheslist[i])
            all.append(numQuarterly)
        for i in range(len(all)):
            if all[i]==max(all):
                num=i
            else:
                continue
        print("第",choose,"季度最畅销的商品是",clotheslist[num],"销量为",max(all))
    else:
        print("输入非法！")
    return 0
info0 = '''
        ------------
        0：全部     
        1：第一季度  
        2：第二季度
        3：第三季度
        4：第四季度
        ------------
'''
info = '''
        -----------------------------
                操作指南
            0：求商品月总销售额
            1：每件衣服的月销售件数占比
            2：每件衣服的月销售额占比
            3：每月最畅销商品
            4：最不畅销商品
            5：全年销售额
            6：季度销售额
            7：衣服全年销售额占比
            8：每件衣服的年销售（件数）占比
            9：每件衣服的年销售额占比
            10:每年最畅销的商品
            11:每年最不畅销的商品
            12：每个季度最畅销的商品
            q：退出
        -------------------------------
        '''
while True:
    print(info)
    choose=input()
    if choose.isdigit():
        choose=int(choose)
        if choose==0:
            strs0 = input("请输入查询月份")
            salesMoneyMonthLoad(strs0,price,sales)
        elif choose==1:
            salesNumberMonth(strs0,sales,goods)
        elif choose==2:
            salesMoneyScaleMonth(price,goods,sales)
        elif choose==3:
            strs0=input("请输入月份")
            saleMax(strs0,goods,sales)
        elif choose==4:
            strs0 = input("请输入月份")
            saleMin(strs0, goods, sales)
        elif choose==5:
            salesMoneyYear(sales,price)
        elif choose==6:
            salesMoneyQuarterly(sales, price)
        elif choose==7:
            salesMonryClothes(sales,price)
        elif choose==8:
            salesYearClothesCountsLoad(sales,goods)
        elif choose==9:
            salesMoneyScalesYearLoad(price, goods, sales)
        elif choose==10:
            salesMaxYear(sales, goods)
        elif choose==11:
            salesMinYear(sales, goods)
        elif choose==12:
            salesMaxQuarterly(goods)
    elif choose=="q":
        print("退出查询成功！")
        break
    else:
        print("输入非法！")














