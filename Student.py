'''

i.  定义了一个学生类：属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。
    行为：学习（要求参数传入学习的时间），玩游戏（要求参数传入游戏名）,编程（要求参数传入写代码的行数）
    数的求和（要求参数用变长参数来做，返回求和结果）
'''
class Student:
    __id=""
    __name=""
    __age=""
    __sex=""
    __hight=""
    __wight=""
    __grade=""
    __address=""
    __phone=""

    def setId(self,id):
        self.__id=id
    def setName(self,name):
        self.__name=name
    def setAge(self,age):
        self.__age=age
    def setHight(self,hight):
        self.__hight=hight
    def setWight(self,wight):
        self.__wight
    def setSex(self,sex):
        self.__sex=sex
    def setGrade(self,grade):
        self.__grade=grade
    def setAddress(self,address):
        self.__address=address
    def setPhone(self,phone):
        self.__phone=phone
    def getId(self,id):
        return self.__id
    def getName(self,name):
        return self.__name
    def getAge(self, age):
        return self.__age
    def getHight(self, hight):
        return self.__hight
    def getWight(self, wight):
        return self.__wight
    def getGrade(self, grade):
        return self.__grade
    def getAddress(self, adddress):
        return self.__address
    def getPhone(self, phone):
        return self.__phone

    def learn(self,hour):
        print("学习的时间为",hour,"小时")
    def playGame(self,gameName):
        print("玩的游戏名字为",gameName)
    def biancheng(self,rows):
        print("写的代码行数为",rows)

#可变长度参数*args:以元组形式接收。**kwargs:以字典形式接收
    def numberSum(self,*args):
        print(sum(args))
        return sum(args)
    def dect(self,**kwargs):
        print(kwargs)
        return kwargs
    def show(self):
        print("我叫",self.__name,"年龄是",self.__age,"身高",self.__hight,"性别",self.__sex,"体重",self.__wight,"成绩",self.__grade)
p=Student()
p.setId("6134400")
p.setName("刘沁雅")
p.setAge("17")
p.setSex("女")
p.setHight("170cm")
p.setWight("69kg")
p.setGrade("85")
p.setAddress("西南大街")
p.setPhone("1234567891011")
p.show()


p.learn(10)
p.playGame("英雄联盟")
p.biancheng(500)


p.numberSum(1,1,1,1,1,95)
p.dect(a=1,b=2,c=3)