# import xlrd
#
# dect={}
#
# # 1.打开
# Sales_Data = xlrd.open_workbook(filename=r"C:\Users\刘帅\PycharmProjects\day07\2020年每个月的销售情况.xlsx")
#
#
# Sales_Statistics = {}
#
# month = 1
# while month <= 12:  # 12月份 12张表
#     Month_Sales = Sales_Data.sheet_by_index(month - 1)  # 每月的表
#     rows = Month_Sales.nrows
#     for i in range(rows):
#         data = Month_Sales.row_values(i)
#         if data[1] == "服装名称":  # 第一行跳过
#             pass
#         else:
#             if data[1] in Sales_Statistics:
#                 continue
#             else:
#                 Sales_Statistics[data[1]] = {
#                                              "单价": data[2]
#                                              }
#     month+=1
#
# print(Sales_Statistics["羽绒服"]["单价"])






