# author:jason
import random

# 银行类型
bank_type = {
    1:"工商银行",
    2:"农业银行"
}

#工商银行
icbc_bank = {}

# 农业银行
abc_bank={}
# 农业银行卡类型

bank = {
    1:{},
    2:{}
}
abc_card = {
    1:"金卡",
    2:"普通会员卡"
}


# 开户行名称
bank_name = {1:"中国工商银行昌平支行",2:"中国农业银行昌平支行"}
bank_choice = {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"Bye"}  # 银行业务选项
# 工商银行的信息模板
icbc_myinfo='''
    \033[0;32;40m
    ------------账户信息------------
    账号：{account}
    姓名：{username}
    密码：{password}
    地址：
        国家：{country}
        省份：{province}
        街道：{street}
        门牌号：{door}
    账户余额：{money}
    注册银行名：{bank_name}
    -------------------------------
    \033[0m
'''
# 农业银行打印模板信息
abc_myinfo='''
    \033[0;32;40m
    ------------账户信息------------
    账号：{account}
    姓名：{username}
    密码：{password}
    卡类型：{cardtype}
    地址：
        国家：{country}
        省份：{province}
        街道：{street}
        门牌号：{door}
    账户余额：{money}
    注册银行名：{bank_name}
    -------------------------------
    \033[0m
'''

# 首页消息模板
msg_info = '''\033[1;31;5m
******************************************************************************************************
                            今日银行消息：
                        【今日银行转账手续费通知：】
                        1.转账2000元以下。    异地同行或跨行转账手续费是ATM转账是1.6元/笔.
                        2.转账2000-5000元。   异地同行或跨行转账手续费是ATM转账是4元/笔.
                        3.转账5000-10000元。  异地同行或跨行转账手续费是ATM转账是8元/笔
                        4.转账10000-50000元。 异地同行或跨行转账手续费是ATM转账是12元/笔。
                        5.转账50000元以上。   异地同行或跨行转账手续费是ATM转账金额的0.03%，最高50元。
******************************************************************************************************
\033[0m
'''


# 欢迎模板
welcome = '''
                                **********************************
                                *      中国{0}银行账户管理系统   *
                                ***********************************
                                *               选项              *
'''

welcome_item = '''                                *              {0}.{1}             *                '''
# 打印欢迎页面信息
def print_welcome(bktype):
    print(msg_info)
    print(welcome.format(bank_type[bktype]),end="")
    keys = bank_choice.keys()
    for i in keys:
        print(welcome_item.format(i,bank_choice[i]))

    print('''                                **********************************''')

# 输入帮助方法：chose是打印选项
def inputHelp(chose,datatype="str"):
    while True:
        print("请输入",chose,end="")
        i = input(">>>:")
        if len(i) == 0:
            print("该项不能为空！请重新输入！")
            continue
        if datatype != "str":
            return int(i)
        else:
            return i

# 判断是否存在该银行选项
def  isExists(chose,data):
    if chose in data:
        return True
    return False

# 专门打印个人信息
def printMyInfo(bktype,username):
    user = bank[bktype][username]
    if bktype == 2:
        print("恭喜开户成功！以下是您的开户信息：")
        print(abc_myinfo.format(account=user["account"],
                                username=username,
                                password=user["password"],
                                country=user["country"],
                                province=user["province"],
                                street=user["street"],
                                door=user["door"],
                                money=user["money"],
                                bank_name=user["bank_name"],
                                cardtype=user["cardtype"]
                                ))
    else:
        print("恭喜开户成功！以下是您的开户信息：")
        print(icbc_myinfo.format(account=user["account"],
                                 username=username,
                                 password=user["password"],
                                 country=user["country"],
                                 province=user["province"],
                                 street=user["street"],
                                 door=user["door"],
                                 money=user["money"],
                                 bank_name=user["bank_name"],
                                 ))

# 获取随机码
def  getRandom():
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    string = ""
    for i in range(8):
        string = string + li[int(random.random()* len(li))]
    return string

# 通过账号获取账户信息,返回用户名
def findByAccount(account,bktype):
    for i in bank[bktype].keys():
        if bank[bktype][i]["account"] == account:
            return i
    return None
def findByAccountBank(bank_name,bktype):
    for i in bank[bktype].keys():
        if bank[bktype][i]["bank_name"] == bank_name:
            return i
    return None
# 银行的开户方法
def bank_addUser(username,password,country,province,street,door,money,cardtype,bk_type):
    if len(bank[bk_type]) >= 100:
        return 3
    elif username in bank[bk_type].keys():
        return 2
    else:
        abc_data = {
            "account":getRandom(),
            "password":password,
            "cardtype":cardtype,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":money,
            "bank_name":bank_name[bk_type]
        }
        icbc_data = {
            "account":getRandom(),
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":money,
            "bank_name":bank_name[bk_type]
        }
        bank[bk_type][username] = abc_data if bk_type == 2 else icbc_data
    return 1

# 银行的存钱方法
def bank_saveMoney(ac,money,bktype):
    for i in bank[bktype].keys():
        if bank[bktype][i]["account"] == ac:
            print("历史余额为：",bank[bktype][i]["money"])
            bank[bktype][i]["money"] += money
            return True
    return False

# 银行的查询功能
def bank_selectUser(account,password,bktype):

    uname = findByAccount(account,bktype)

    if uname != None and len(uname) != 0:
        if password == bank[bktype][uname]["password"]:
            printMyInfo(bktype,uname)
        else:
            print("用户密码错误！")
    else:
        print("该用户不存在！")

# 银行的取钱功能
def bank_takeMoney(account,password,money,bktype):
    uname = findByAccount(account,bktype)
    if uname != None:
        if bank[bktype][uname]["password"] == password:
            if bank[bktype][uname]["money"] < money:
                return 3
            else:
                bank[bktype][uname]["money"] -= money
                return 0
        else:
            return 2
    else:
        return 0

# 银行的转账功能
def bank_transformMoney(outputaccount,inputaccount,outputpassword,outputmoney,bktype):
    status = bank_takeMoney(outputaccount,outputpassword,outputmoney,bktype)
    if status == 1:
        return status
    elif status == 2:
        return status
    elif status == 3:
        return status

    if inputaccount != None and findByAccount(inputaccount,bktype) != None:
        bank_saveMoney(inputaccount,outputmoney,bktype)
        return 0
    else:
        return 1

# 开户方法
def addUser(bktype):
    username = inputHelp("用户名")
    password = inputHelp("密码")
    cardtype = 2
    if bktype == 2:
        cardtype = inputHelp("开卡类型[1:金卡，2：普通会员卡]")
        if cardtype == "1":
            cardtype = 1
        elif cardtype == "2":
            cardtype = 2
        else:
            print("对不起，输入错误！系统默认分配您的卡类别为：普通会员卡！")
    country = inputHelp("居住地址：1.国家：")
    province = inputHelp("省份")
    street = inputHelp("街道")
    door = inputHelp("门牌号")
    money = inputHelp("银行卡余额","int")

    # 调用银行的开户方法完成开户操作  返回 1 2 3
    status = bank_addUser(username,password,country,province,street,door,money,cardtype,bktype)
    # 判断1   2   3
    if status == 1:
        printMyInfo(bktype,username)
    elif status == 2:
        print("改用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
    elif status == 3:
        print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")

# 存钱
def saveMoney(bktype):
    account = inputHelp("账号")
    m = inputHelp("存入的金额","int")

    flag = bank_saveMoney(account,m,bktype)

    if flag:
        print("存储成功!您的个人信息为：")
        printMyInfo(bktype,findByAccount(account,bktype))
    else:
        print("对不起，您的个人信息不存在！请先开户后再次操作！")

# 取钱
def takeMoney(bktype):
    account = inputHelp("账户")
    password = inputHelp("密码")
    tmoney = inputHelp("取出金额","int")

    f = bank_takeMoney(account,password,tmoney,bktype)

    if f == 1:
        print("改用户不存在！")
    elif f == 2:
        print("密码错误！")
    elif f == 3:
        print("取款金额不足！")
    elif f == 0:
        print("取款成功！")
        bank_selectUser(account,password,bktype)

# 转账功能
def transformMoney(bktype):

    output = inputHelp("转出的账号")
    input = inputHelp("转入的账号")
    outputpass = inputHelp("转出的密码")
    outputmoney = inputHelp("要转出的金额","int")
    #调用方法
    f = bank_transformMoney(output, input, outputpass, outputmoney, bktype)
    bank_output=findByAccountBank(output,bktype)
    bank_input=findByAccountBank(input,bktype)
    if bank_output==bank_input:
        print("ok")
        if f == 1:
            print("转出或转入的账号不存在！")
        elif f == 2:
            print("输入密码错误！")
        elif f == 3:
            print("转账金额不足！")
        else:
            print("转账成功！")
            print("您的个人信息：")
            bank_selectUser(output, outputpass,bktype)

    elif bank_input!=bank_output:
        print("收取1.6元手续费")
        if f == 1:
            print("转出或转入的账号不存在！")
        elif f == 2:
            print("输入密码错误！")
        elif f == 3:
            print("转账金额不足！")
        else:
            print("转账成功！")
            print("您的个人信息：")
            bank_selectUser(output, outputpass, bktype)

# 查询账户方法
def selectUser(bktype):
    account = inputHelp("账号")
    password = inputHelp("密码")

    bank_selectUser(account,password,bktype)




# 预处理输入
def prepare(bktype):
    while True:
        print_welcome(bktype)
        chose = inputHelp("选项")
        if isExists(chose,bank_choice):
            if chose == "1":
                addUser(bktype)
            elif chose == "2":
                saveMoney(bktype)
            elif chose == "3":
                takeMoney(bktype)
            elif chose == "4":
                transformMoney(bktype)
            elif chose == "5":
                selectUser(bktype)
            elif chose == "6":
                print("Bye,Bye您嘞！！！！")
                return
        else:
            print("不存在改选项，别瞎弄！")


# 核心程序
while True:
    bk_type = inputHelp("您要操作的银行（1：工商银行，2：农业银行）：")

    if bk_type == "1":
        prepare(1)
    elif bk_type == "2":
        prepare(2)
    elif bk_type == "q" or bk_type == "Q":
        print("欢迎下次光临！Bye！")
        break
    else:
        print("操作错误！")


