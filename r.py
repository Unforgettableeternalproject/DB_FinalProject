# import random
#
# # 建立一個列表
# numbers = ["color","engine","transmission"]
#
# # 迴圈跑30次
# for _ in range(57):
#     # 隨機選取列表中的一個元素並印出
#     print(random.choice(numbers))

# a=[]
# for i in range(57):
#     a.append([input(),"color","engine","transmission"])
# for i in range(57):
#     temp=list(input().split(","))
#     for k in range(len(a)):
#         if a[k][0]==temp[0]:
#             a[k].remove(temp[1])
#             break
# for i in a:
#     if len(i)==1:
#         print(*i,sep=",")
#     else:
#         for j in range(1,len(i)):
#             print(i[0]+","+i[j])


# import random
# from datetime import datetime, timedelta
#
# # 設定時間範圍
# start_date = datetime(2018, 1, 1)
# end_date = datetime(2024, 6, 9)
#
# for i in range(160):
#     # 生成隨機的時間戳記
#     random_date = start_date + (end_date - start_date) * random.random()
#     print(random_date)


# import random
#
# # 建立一個列表
# a = []
# for i in range(20):
#     a.append([input().split(",")])
# # 使用 random.shuffle 函數來隨機排序列表
# random.shuffle(a)
#
# # 印出隨機排序後的列表
# for n in a:
#     print(n[0],n[1])

# a=[]
# D1,D2,D3,D4,D5=0,0,0,0,0
# for i in range(130):
#     a.append(input())
# for i in range(130):
#     temp=int(input())
#     if a[i]=="D001":
#         D1+=temp
#     elif a[i]=="D002":
#         D2+=temp
#     elif a[i]=="D003":
#         D3+=temp
#     elif a[i]=="D004":
#         D4+=temp
#     elif a[i]=="D005":
#         D5+=temp
# print("D001",D1)
# print("D002",D2)
# print("D003",D3)
# print("D004",D4)
# print("D005",D5)

# a=[6,7,5,3,3,1,5,6,5,10,12,8,3,7,2,1,2,12,9,10,8,8,7,10,3,9,8,1,11,12,5,6,2,7,10]
# print(len(a))
# for i in range(1,13):
#     print(i,a.count(i))