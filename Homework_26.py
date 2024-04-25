# Ex_1
# import math
#
#
# def area(r, alpha):
#     return math.pi * r ** 2 * ((alpha * 57.296 / 180) * math.pi) / 360
# print(f"{round(area(4,45),3)} °C ")
# Ex_2
# a=[
#   ["M",1000],
#   ["D",500],
#   ["C",100],
#   ["L",50],
#   ["X",10],
#   ["V",5],
#   ["I",1],
#   ]
# n=int(input("Enter number :"))
# x=""
# while True:
#     for i in range(len(a)):
#         if n>=a[i][1]:
#             n-=a[i][1]
#             x+=a[i][0]
#             break
#         elif n>=(a[i][1]-a[i+1][1]):
#             n-=(a[i][1]-a[i+1][1])
#             x+=a[i+1][0]+a[i][0]
#             break
#         elif n==0:
#             break
#
# print(x)
# Ex_3
# def filter_longest_words(words):
#     max_length = max(len(word) for word in words)
#     return [word for word in words if len(word) == max_length]
#
#
# input_list = ["aba", "aa", "z", "adv", "vcd", "aba"]
# print(filter_longest_words(input_list))
