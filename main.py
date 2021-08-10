#让系统随机产生一个随机数
import random
i=10000
count=0
num3=0
num5=0
print("********QAQ切记不要输入非数字，会崩的欧QAQ*********")
num=random.randint(0,1000)
while(i>0):
    count=count+1
    i=i-500
    print("您的可用余额为",i)
    chose=input("请输入数字")
    chose=int(chose)
    if chose>num:
        print("输入数字过大")
        num3=input("是否花费￥获得提示信息：输入1代表是，输入2代表不是")
        num3=int(num3)
        if num3==1:
            print("金额一共3挡：1000，1500，5000")
            num4=input("请输入花费金额")
            num4=int(num4)
            if num4==1000:
                i=i-1000
                if i>0:
                    print("答案的个位数是",num%10,"偶!")
                else:
                    break
            elif num4==1500:
                i=i-1500
                if i>0:
                    print("答案在后两位数是",num%100,"偶")
                else:
                    break
            elif num4==5000:
                i=i-5000
                if i > 0:
                    print("答案在", num % 1000 + num % 10, "左10位偶")
                else:
                    break
            else:
                print("输入非法！！")
        else:
            print("祝您好运！")
    elif chose<num:
        print("输入数字过小")
        num5 = input("是否花费￥获得提示信息：输入1代表是，输入2代表不是")
        num5 = int(num5)
        if num5 == 1:
            print("金额一共5挡：1000，1500，5000")
            num6 = input("请输入花费金额")
            num6 = int(num6)
            if num6== 1000:
                i=i-1000
                if i>0:
                    print("答案的个位数是",num%10,"偶!")
                else:
                    break
            elif num6 == 1500:
                i=i-1500
                if i>0:
                    print("答案的后两位数是",num%100,"偶!")
                else:
                    break
            elif num6 == 5000:
                i = i - 5000
                if i>0:
                    print("答案在",num%1000+num%10,"左10位偶")
                else:
                    break
            else:
                print("输入非法！！")
        else:
            print("祝您好运！")
    else:
        print("恭喜，本次猜中，本次幸运数字")
        i=i+10000
        num1=input("键盘输入数字1，开始下一轮游戏。输入其他数字结束游戏！")
        num1=int(num1)
        if num1==1:
            print("第",count-1,"轮游戏即将开始")
            num = random.randint(0, 1000)
        else:
            break
if i>0:
    print("***********************")
    print("游戏结束，欢迎您下次再来玩!")
    print("***********************")
else:
    print("T_T")
    print("余额不足，请继续充值")








