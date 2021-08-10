#1号衣服
#sales销售量
#Inventory库存
id1=1
name1="羽绒服"
price1=253.6
Inventory1=500
sales1=10+69+140+10+10
#2号衣服
name2="牛仔裤"
price2=86.3
Inventory2=600
sales2=60+72+35+90+60+60+140
#3号衣服
name3="风衣"
price3=96.8
Inventory3=335
sales3=43+25+43+60+43+78
#4号衣服
name4="皮草"
price4=135.9
Inventory4=855
sales4=63+24+63+57
#5号衣服
name5="T恤"
price5=65.8
Inventory5=632
sales5=63+45+129+63+58+48+63
#6号衣服
name6="衬衫"
price6=49.3
Inventory6=562
sales6=120
#总销售量
number=10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78
#总金额amount
amount=price1*sales1+price2*sales2+price3*sales3+price4*sales4+price5*sales5+price6*sales6
id="日期"
name="服装名称"
price="价格/件"
Inventory="库存数量"
slase="销售量"
print("---------------12月份衣服销售数据--------------------+")
print(id,name,price,Inventory,slase)
print("---------------------------------------------------+")
print(" 1号",name1,price1,Inventory1,"10     | ")
print(" 2号",name2,price2,Inventory2,"60     | ")
print(" 3号",name3,price3,Inventory3,"43     | ")
print(" 4号",name4,price4,Inventory4,"63     | ")
print(" 5号",name5,price5,Inventory5,"63     | ")
print(" 6号",name6,price6,Inventory6,"120    | ")
print(" 7号",name2,price2,Inventory2,"72     | ")
print(" 8号",name1,price1,Inventory1,"69     | ")
print(" 9号",name2,price2,Inventory2,"35     | ")
print("10号",name1,price1,Inventory1,"140    | ")
print("11号",name2,price2,Inventory2,"90     | ")
print("12号",name4,price4,Inventory4,"24     | ")
print("13号",name5,price5,Inventory5,"45     | ")
print("14号",name3,price3,Inventory3,"25     | ")
print("15号",name2,price2,Inventory2,"60     | ")
print("16号",name5,price5,Inventory5,"129    | ")
print("17号",name1,price1,Inventory1,"10     | ")
print("18号",name3,price3,Inventory3,"43     | ")
print("19号",name5,price5,Inventory5,"63     | ")
print("20号",name2,price2,Inventory2,"60     | ")
print("21号",name4,price4,Inventory4,"63     | ")
print("22号",name3,price3,Inventory3,"60     | ")
print("23号",name5,price5,Inventory5,"58     | ")
print("24号",name2,price2,Inventory2,"140    | ")
print("25号",name5,price5,Inventory5,"48     | ")
print("26号",name3,price3,Inventory3,"43     | ")
print("27号",name4,price4,Inventory4,"57     | ")
print("28号",name1,price1,Inventory1,"10     | ")
print("29号",name5,price5,Inventory5,"63     | ")
print("30号",name3,price3,Inventory3,"78     | ")
print("---------------------------------------------------+")
print("12月份销售总金额",amount)
print("羽绒服销售占比",'{:.2f}%'.format((sales1/number)*100))
print("牛仔裤销售占比",'{:.2f}%'.format((sales2/number)*100))
print("风衣销售占比",'{:.2f}%'.format((sales3/number)*100))
print("皮草销售占比",'{:.2f}%'.format((sales4/number)*100))
print("T恤销售占比",'{:.2f}%'.format((sales5/number)*100))
print("衬衫销售占比",'{:.2f}%'.format((sales6/number)*100))
print("羽绒服销售额占比",'{:.2f}%'.format((sales1*price1/amount)*100))
print("牛仔裤销售额占比",'{:.2f}%'.format((sales2*price2/amount)*100))
print("风衣销售额占比",'{:.2f}%'.format((sales3*price3/amount)*100))
print("皮草销售额占比",'{:.2f}%'.format((sales4*price4/amount)*100))
print("T恤销售额占比",'{:.2f}%'.format((sales5*price5/amount)*100))
print("衬衫销售额占比",'{:.2f}%'.format((sales6*price6/amount)*100))

