import random
from DBUTilsBank import update, select

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
#跨行转账收费打印模板信息
bank='''
******************************************************************************************************
                            今日银行消息：
                        【今日银行转账手续费通知：】
                        1.转账2000元以下。    异地同行或跨行转账手续费是ATM转账是1.6元/笔.
                        2.转账2000-5000元。   异地同行或跨行转账手续费是ATM转账是4元/笔.
                        3.转账5000-10000元。  异地同行或跨行转账手续费是ATM转账是8元/笔
                        4.转账10000-50000元。 异地同行或跨行转账手续费是ATM转账是12元/笔。
                        5.转账50000元以上。   异地同行或跨行转账手续费是ATM转账金额的0.03%，最高50元。
******************************************************************************************************
    

'''
# 专门打印个人信息
def printMyInfoAbc(bktype,account,username,password,country,province,street,door,money,cardtype,bank_name):
    if bktype == 2:
        print("恭喜开户成功！以下是您的开户信息：")
        print(abc_myinfo.format(account=account,
                                username=username,
                                password=password,
                                country=country,
                                province=province,
                                street=street,
                                door=door,
                                money=money,
                                bank_name=bank_name,
                                cardtype=cardtype
                                ))
def printMyInfoIcbc(bktype, username, account, password, country, province, street, door, money, bank_name):
    if bktype == 1:
        print("恭喜开户成功！以下是您的开户信息：")
        print(icbc_myinfo.format(account=account,
                                 username=username,
                                 password=password,
                                 country=country,
                                 province=province,
                                 street=street,
                                 door=door,
                                 money=money,
                                 bank_name=bank_name,
                                 ))
# 开户的方法
def addUser(bktype):
    username = inputHelp("用户名")
    password = inputHelp("密码")
    if bktype==1:
        account=random.randint(1000000,9999999)
        # account=2475456
        bank_name="中国工商银行"
        country = inputHelp("居住地址：1.国家：")
        province = inputHelp("省份")
        street = inputHelp("街道")
        door = inputHelp("门牌号")
        money = inputHelp("银行卡余额", "int")
        static= icbc_bank_addUser(account,username,password,country,province,street,door,money,bank_name)
        if static==1:
            print("银行库已经满了，请携带相关证件到其他行办理开户业务！")
        elif static==2:
            print("您已经开过户了，不能重复开户")
        else:

            printMyInfoIcbc(bktype,username,account,password,country,province,street,door,money,bank_name)
    elif bktype==2:
        account = random.randint(1000000, 9999999)
        bank_name = "中国农业银行"
        country = inputHelp("居住地址：1.国家：")
        province = inputHelp("省份")
        street = inputHelp("街道")
        door = inputHelp("门牌号")
        money = inputHelp("银行卡余额", "int")
        cardtype=inputHelp("开卡类型[1:金卡，2：普通会员卡]")
        if cardtype == "1":
            cardtype = 1
        elif cardtype == "2":
            cardtype = 2
        else:
            print("对不起，输入错误！系统默认分配您的卡类别为：普通会员卡！")
        static=abc_bank_addUser(account,username,password,country,province,street,door,money,cardtype,bank_name)
        if static == 1:
            print("银行库已经满了，请携带相关证件到其他行办理开户业务！")
        elif static == 2:
            print("您已经开过户了，不能重复开户")
        else:
            printMyInfoAbc(bktype,username,account,password,country,province,street,door,money,bank_name, cardtype)
def icbc_bank_addUser(account,username,password,country,province,street,door,money,bank_name):
    sql="select * from icbc_bank_adduser where bank_name=%s"
    param=["中国工商银行"]
    database="icbc_bank"
    list=select(sql,param,database)
    sql0="SELECT COUNT(*) FROM icbc_bank_adduser WHERE account =%s"
    param0=[account]
    list1=select(sql0,param0,database)
    if 100<len(list):
        return 1
    elif 0!=list1[0][0]:
        print(list1[0][0])
        return 2
    else:
        database="icbc_bank"
        sql = "INSERT INTO icbc_bank_addUser VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param=[account,username,password,country,province,street,door,money,bank_name]
        update(sql,param,database)
        return 3
def abc_bank_addUser(account,username,password,country,province,street,door,money,cardtype,bank_name):
    sql = "select * from abc_bank_adduser where bank_name=%s"
    param = ["中国农业银行"]
    database="abc_bank"
    list = select(sql,param,database)
    sql0 = "select COUNT(*) FROM abc_bank_adduser WHERE account =%s"
    print(sql0)
    param0 = [account]
    list1 = select(sql0, param0,database)
    if 100 < len(list):
        return 1
    elif  0!=list1[0][0]:
        return 2
    else:
        database = "abc_bank"
        sql = "INSERT INTO abc_bank_addUser VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param = [account, username, password, country, province, street, door, money,cardtype, bank_name]
        update(sql, param, database)
        return 3
''
#存钱
def bank_saveMoney(bktype):
    if bktype==1:
        database="icbc_bank"
        bank="icbc_bank_adduser "
    elif bktype==2:
        database = "abc_bank"
        bank="abc_bank_adduser "
    sql="select count(*) from"+" "+bank+" "+"where account=%s"
    account=inputHelp("请输入账户")
    param=[account]
    userlist=select(sql,param,database)
    if 0!=userlist[0][0]:
        password=inputHelp("请输入密码")
        sql0="select ipassword from"+" "+bank+" "+"where account=%s"
        ipassword=select(sql0,param,database)
        if password==ipassword[0][0]:
            savmoney=inputHelp("请输入存款金额")
            sql1="UPDATE "+bank+" "+"SET money = money+"+savmoney+" "+"WHERE account =%s"
            update(sql1,param,database)
            print("存款成功")
            sql2="select money from " +bank+" "+" where account=%s"
            selectmoney=select(sql2,param,database)
            print("您已经成功存款",savmoney,"￥","当前余额为",selectmoney[0][0],"￥")

        else:
            i=0
            while True:
                print("密码错误！输入3次密码错误后，将锁定账号")
                if i>=3:
                    break
                i+=1
    else:
        print("输入的账号不存在，请重新输入！")

#取钱
def bank_getMoney(bktype):
    if bktype==1:
        database="icbc_bank"
        bank="icbc_bank_adduser "
    elif bktype==2:
        database = "abc_bank"
        bank="abc_bank_adduser "
    sql="select count(*) from"+" "+bank+" "+"where account=%s"
    account=inputHelp("请输入账户")
    param=[account]
    userlist=select(sql,param,database)
    if 0!=userlist[0][0]:
        password=inputHelp("请输入密码")
        sql0="select ipassword from"+" "+bank+" "+"where account=%s"
        ipassword=select(sql0,param,database)
        if password==ipassword[0][0]:
            getmoney=inputHelp("请输入取款金额")
            sql1="UPDATE "+bank+" "+"SET money = money-"+getmoney+" "+"WHERE account =%s"
            update(sql1,param,database)
            print("取款成功")
            sql2="select money from " +bank+" "+" where account=%s"
            selectmoney=select(sql2,param,database)
            print("您已经成功取款",getmoney,"￥","当前余额为",selectmoney[0][0],"￥")

        else:
            i=0
            while True:
                print("密码错误！输入3次密码错误后，将锁定账号")
                if i>=3:
                    break
                i+=1
    else:
        print("输入的账号不存在，请重新输入！")

#转账
def transformMoney(bktype):
    if bktype==1:
        database="icbc_bank"
        table="icbc_bank_adduser"
    elif bktype==2:
        database = "abc_bank"
        table = "abc_bank_adduser"
    output = inputHelp("转出的账号")
    input = inputHelp("转入的账号")
    outputmoney = inputHelp("要转出的金额")
    outputpass = inputHelp("转出的密码")
    print("out",outputpass)
    sql0="select ipassword from"+" "+table+" "+"where account=%s"
    param0=[output]
    ipassword=select(sql0,param0,database)
    if outputpass==ipassword[0][0]:
        sql = "select count(*) from" + " " + table + " " + "where account=%s"
        param = [input]
        list = select(sql, param, database)
        if 0 != list[0][0]:
            sql1 = "select money from" + " " +table + " " + "where accpunt=%s"
            list = select(sql1, output,database)
            if outputmoney > list[0][0]:
                sqlout = "UPDATE " + table + " " + "SET money = money-" + " " + outputmoney + " " + "WHERE account =%s"
                param = [output]
                update(sqlout, param, database)
                sqlin = "UPDATE " + table + " " + "SET money = money+" + " " + outputmoney + " " + "WHERE account =%s"
                param1 = [input]
                update(sqlin, param1, database)
                print("转账成功")
                sql2 = "select * from" + " " + table + " " + "where account=%s"
                param2 = [output]
                out = select(sql2, param2, database)
                print("账户", output, "您的余额为", out[0][7], "￥")

            else:
                print("转账失败，银行卡余额不足！")


        else:
            print("跨行转账！")
            print(bank)
            if bktype == 1:
                outdatabase = "icbc_bank"
                outtable = "icbc_bank_adduser"
                indatabase="abc_bank"
                intable="abc_bank_adduser"
            elif bktype == 2:
                outdatabase = "abc_bank"
                outtable = "abc_bank_adduser"
                indatabase = "icbc_bank"
                intable = "icbc_bank_adduser"
            koutput =output
            kinput = input
            koutputmoney = outputmoney
            koutputpass = outputpass
            sql0 = "select ipassword from" + " " + outtable + " " + "where account=%s"
            param0 = [output]
            ipassword = select(sql0, param0, outdatabase)
            if koutputpass==ipassword[0][0]:
                sql = "select count(*) from" + " " + intable + " " + "where account=%s"
                param = [input]
                list = select(sql, param, indatabase)
                if 0 != list[0][0]:
                    koutputmoney=int(koutputmoney)
                    if koutputmoney>0 and koutputmoney<2000:
                        k="1.6"
                    elif koutputmoney>=2000 and koutputmoney<5000:
                        k="4"
                    elif koutputmoney >= 5000 and koutputmoney < 10000:
                        k ="8"
                    elif koutputmoney >=10000 and koutputmoney < 50000:
                        k ="12"
                    elif koutputmoney>=50000:
                        k=outputmoney*0.0003
                        k=k+""
                    else:
                        print("输入非法！")
                    sql1="select money from"+" "+outtable+" "+"where accpunt=%s"
                    list=select(sql1,koutput,outdatabase)
                    if koutputmoney>list[0][0]:
                        koutputmoney = str(koutputmoney)
                        sqlout = "UPDATE " + outtable + " " + "SET money = money-" + " " + koutputmoney + "-" + k + " " + "WHERE account =%s"
                        param = [koutput]
                        update(sqlout, param, outdatabase)
                        sqlin = "UPDATE " + intable + " " + "SET money = money+" + " " + koutputmoney + " " + "WHERE account =%s"
                        param1 = [kinput]
                        update(sqlin, param1, indatabase)
                        print("转账成功", "成功为", kinput, "转账", koutputmoney, "￥")
                        sql2 = "select * from" + " " + table + " " + "where account=%s"
                        param2 = [koutput]
                        out = select(sql2, param2, outdatabase)
                        print("账户", koutput, "您的余额为", out[0][7], "￥")
                    else:
                        print("转账失败，银行卡余额不足！")
                else:
                    print("您输入的账户不存在！")


    else:
        print("密码错误！")

#查询
def selectUser(bktype):
    if bktype == 1:
        database = "icbc_bank"
        bank = "icbc_bank_adduser "
    elif bktype == 2:
        database = "abc_bank"
        bank = "abc_bank_adduser "
    account=inputHelp("请输入账号")
    sql="select* from"+" "+bank+""+"where account=%s"
    param=[account]
    userlsit=select(sql,param,database)
    print(userlsit)
    if bktype == 1:
       printMyInfoIcbc(bktype,userlsit[0][1],userlsit[0][0],userlsit[0][2],userlsit[0][3],userlsit[0][4],userlsit[0][5],userlsit[0][6],userlsit[0][7],userlsit[0][8])
    elif bktype == 2:
       if userlsit[0][8]=="1":
           cardtype="金卡"
       elif userlsit[0][8]=="2":
           cardtype = "普通卡"

       printMyInfoAbc(bktype,userlsit[0][1],userlsit[0][0],userlsit[0][2],userlsit[0][3],userlsit[0][4],userlsit[0][5],userlsit[0][6],userlsit[0][7],cardtype ,userlsit[0][9])



icbc_info='''
                ------------------------------------
                          中国工商银行业务
                ------------------------------------
                    1—***********开户************
                    2—***********存款************
                    3—***********取款************
                    4-***********转账************
                    5-***********查询************
                    6-***********退出************
                ------------------------------------
'''
abc_info='''
                ------------------------------------
                          中国农业银行业务
                ------------------------------------
                    1—***********开户************
                    2—***********存款************
                    3—***********取款************
                    4-***********转账************
                    5-***********查询************
                    6-***********退出************
                ------------------------------------
'''
# 判断是否存在该银行选项
# def  isExists(chose,data):
#     sql="create database if not exists company character set utf8;"
#     if chose in data:
#         return True
#     return False

def prepare(bktype):
    if bktype==1:
        print(icbc_info)
    else:
        print(abc_info)
    while True:
        chose = inputHelp("选项")
        # if isExists(chose,bank_choice):
        if chose == "1":
            addUser(bktype)
        elif chose == "2":
            bank_saveMoney(bktype)
        elif chose == "3":
            bank_getMoney(bktype)
        elif chose == "4":
            transformMoney(bktype)
        elif chose == "5":
            selectUser(bktype)
        elif chose == "6":
            print("Bye,Bye您嘞！！！！")
            return
        # else:
        #     print("不存在改选项，别瞎弄！")



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
