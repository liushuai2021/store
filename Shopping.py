'''
商城
    1、初始化钱包余额
    2、推个空的购物车
    3、正常购物
        输入商品标号选择数据
        是否有商品
            有
                钱是否足够
                    够
                        添加到购物车里
                        余额减去单价
                    不够
                        提示余额不足
            无
                商城中无此商品
    4、打印小票
    任务：
        1、购物小条的重复打印问题
        2、10张联想电脑0.5折 20张老干妈优惠券0.1 15张华为优惠券0.8，随机抽取一张优惠券，
        在结算的时候进行打折。
'''
import random
money=100000
shop=[
    ["lenovo PC",5000],
    ["Mac PC",12000],
    ["HUAWEI WATCH PRO 20",2000],
    ["机械革命",15000],
    ["老干妈",7.5],
    ["卫龙辣条",3],
    ["西瓜",2],
]
#空的购物车
mycart=[]
#联想优惠券列表
lenovolucky=[]
lenovo="true"
num1=10
#华为优惠券列表
huawelucky=[]
huawei="true"
num2=20
#老干妈优惠券列表
laogamalucky=[]
laogama="true"
num3=20
i=1
j=0
#折扣抽奖
while(j<10):
    chose = input("输入1抽取折扣,一共可以抽取10次")
    if chose.isdigit():
            chose = int(chose)
            num = random.randint(0, 3)
            num = int(num)
            if num == 1:
                if num1 > 0:
                    print("恭喜抽中lenvov优惠券，商品打5折!")
                    lenovolucky.append(lenovo)
                    num1 = num1 - 1
                else:
                    print("lenovo优惠券发完了")
            elif num == 2:
                if num2 > 0:
                    print("恭喜抽中华为优惠券，商品打6折!")
                    huawelucky.append(huawei)
                    num2 = num2 - 1
                else:
                    print("华为优惠券发完了")
            elif num == 3:
                if num3 > 0:
                    print("恭喜抽中老干妈优惠券，商品打1折!")
                    laogamalucky.append(laogama)
                    num3 = num3 - 1
                else:
                    print("老干妈优惠券发放完了")
            else:
                print("很遗憾，您没有抽到优惠券T-T")
    elif chose == "q" or chose == "Q":
        print("折扣诱人，下次一定偶！")
        break
    j=j+1
# print("联想5折券",len(lenovolucky))
# print("华为优惠券",len(huawelucky))
# print("老干妈优惠券",len(laogamalucky))
# print("终止", j, len(lenovolucky))
# for key,value in enumerate(lenovolucky):
# print(key,value)
a=len(lenovolucky)
b=len(huawelucky)
c=len(laogamalucky)
while(i<10):
    print("您的奖券剩余量为-------------------------")
    if a>0:
        print("联想5折券", a)
    else:
        print("",end="")
    if b>0:
        print("华为优惠券", b)
    else:
        print("",end="")
    if c>0:
        print("老干妈优惠券",c)
    else:
        print("",end="")
    print("---------------------------------------")
    for key, value in enumerate(shop):
        print(key, value)
    chose=input("请输入商品编号")
    if chose.isdigit():
        chose = int(chose)
        if chose>=len(shop):
            print("商店无商品，请再次输入")
        else:
             if shop[chose][1]>money:
                print("余额不足")
             else:
                 if chose==0:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]
                    a=a-1
                 elif chose==2:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]
                    b= b- 1
                 elif chose==4:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]
                    c= c - 1
                 else:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]
    elif chose=="q"or chose=="Q":
        print("欢迎下次光临")
        break
    i=i+1

# for key,value in enumerate(shop):
# print(key,value)
#打印小票
count=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
for key,value in enumerate(mycart):
    # print(key,value[0],value[1])
    if "lenovo PC" ==value[0]:
        count=count+1
    elif "Mac PC"==value[0]:
        count1=count1+1
    elif "HUAWEI WATCH PRO 20" == value[0]:
        count2 = count2 + 1
    elif "机械革命"== value[0]:
        count3 = count3 + 1
    elif "老干妈" == value[0]:
        count4 = count4 + 1
    elif "卫龙辣条" == value[0]:
        count5 = count5 + 1
    elif "西瓜"==value[0]:
        count6=count6+1
    else:
        break
#lenovo PC

if count>0:
    if len(lenovolucky)>0:
        print(count, "lenovo PC", "总价", shop[0][1] * len(lenovolucky) * 0.5+shop[0][1]*(count-len(lenovolucky)))
    else:
        print(count, "lenovo PC", "总价", shop[0][1] * count )
else:
    print("",end="")

#Mac PC

if count1>0:
    print(count1,"Mac PC","总价",shop[1][1]*count1)
else:
    print("",end="")

#华为

if count2>0:
    if len(huawelucky)>0:
       print(count2, "HUAWEI WATCH PRO 20", "总价", shop[2][1] * len(huawelucky) * 0.6+shop[2][1]*(count2-len(huawelucky)))
    else:
       print(count2, "HUAWEI WATCH PRO 20", "总价", shop[2][1] * count2)
else:
    print("",end="")

#机械革命

if count3>0:
    print(count3,"机械革命","总价",shop[3][1]*count3)
else:
    print("",end="")

#老干妈

if count4>0:
    if len(laogamalucky)>0:
        print(count4, "老干妈", "总价", shop[4][1] * len(laogamalucky)* 0.1+shop[4][1]*(count-len(laogamalucky)))
    else:
        print(count4, "老干妈", "总价", shop[4][1] * count4)
else:
    print("",end="")

# 卫龙辣条
if count5>0:
    print(count5,"卫龙辣条","总价",shop[5][1]*count5)
else:
    print("",end="")

#西瓜
if count6>0:
    print(count6,"西瓜","总价",shop[6][1]*count6)
else:
    print("",end="")



