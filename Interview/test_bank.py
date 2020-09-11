# 1.手写一个python类




# 2.直接手写一个构造函数





# 3.紧接着上面的代码, 直接手写, 补充完整代码, 要求(对列表中的人进行排序, 并筛选出分数大于80的人名单, 组成新的列表并显示)


class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Student(Person):
    def __init__(self, name, gender, age, score):
        super(Student, self).__init__(name, gender, age)
        self.score = score

# People = [kathy, Jim, John, Alice, Leo]




# 4.python高阶函数有哪些, 分别起什么作用?



# 5.简单说说生成器, 迭代器, 装饰器是什么, 都有什么作用?



# 6.python中, 如何将字符串转化为整形?




# 7.TCP三次握手和四次握手, 请分别写出来




# 8.HTTP常见的状态码有哪些? 有什么含义?




# 9.webdriver的核心原理是什么?




# 10.Appium是什么? 主要用来做什么? 他的核心原理是什么?




# 11.selenium1 和 selenium2 的区别是什么，为何要抛弃 selenium1? 它有什么缺陷？





# 12.常见的元素定位方法有哪些？





# 13.直接手写一个冒泡排序和快速排序，时间复杂度是多少？空间复杂度是多少？是否稳定？





# 14.如何查询 Linux 后台日志，直接写出命令





# 15.如何查看当前进程？





# 16.Dockerfile 是什么？如何去创建一个 Dockerfile？





# 17.Python 有没有垃圾回收机制？它又是通过什么来的？





# 18.熟悉 TestNG？那请说一下用法？





# 19.请直接手写一个python单例模式？





# 20.数据库增删改查，手写 SQL





# 21.Redis 是做什么用的？ElasticSearch是什么？做什么用的？





# 22.接口测试怎么做的？如果存在接口依赖关系，怎么做？





# 23.元组和列表的区别是什么？





# 24.Python中，*arg 和 *kwarg 分别代表什么含义，都有哪些作用？





# 25.写过爬虫吗？那请说一下常见的反爬机制有哪些？如果是动态加载的页面，看不到数据，如何去进行爬取？





# 百度三面内容
# 1. 自我介绍
# 2. 为什么base选上海？
# 3. 平时怎么学习一个新东西？
# 4. 怎么看待测开？
# 5. 职业规划
# 6. 判断IP地址是否合法的测试用例
# 7. 还投了哪些？有什么offer？
# -----------------
# 自我介绍
# 项目相关
# 有什么offer,怎么选择？
# 你遇到的一个难点，怎么解决的？
# 简历上有提到自己喜欢学习新技术，问学了哪些技术，怎么学习的？
# 你在校期间最有成就感的一件事？
# 你学的最好的一门课？我说了数据结构、算法等。问了算法中你学到的一些算法，我讲了冒泡和快排
# 你的职业规划？
# 你在校遇到的最有挫折的一件事？
# 有没有男朋友，你的家人怎么看待你的第一份工作的地域问题？
# 有没有什么想问我的？
# 为什么做测开
# -------------------
# Linux按端口号查看进程，查找文件
# -------------------
# 讲一下项目，背景、所用方法、效果
# 对于测开的理解，干嘛的，需要具备什么能力，我为啥能做测开
# 你的优点和缺点
# 有没有榜样，身边的人有么
# 遗憾的事情
# 日常生活中有没有感觉到困难的事情（求职期间还要做科研项目）
# 如果给你一个不熟悉的项目，三天之内完成，你会怎么做
# 技术深度和技术广度的工作你会选择哪个
# 想做测开的原因
# 意向城市
# 反问




# linux三剑客
"""
1.grep擅长查找功能
2.sed擅长取行和替换
3.awk擅长取列
"""


# 测试流程
"""
1. 测试需求(文档, 说明书)
2. 界面测试(外观等等)
3. 功能度(基本功能实现)
4. 安全性
5. 抗破坏性
6. 可移植性
7. 兼容性
8. 易用性
9. 压力测试
10.等等
"""


'''判断字符串'''
# def judge_str(string):
#     flag = True
#     cycle_num = int(len(string)/2)+1
#     for i in range(cycle_num):
#         if '()' in string:
#             string = string.replace('()', '')
#         elif '[]' in string:
#             string = string.replace('[]', '')
#         elif '{}' in string:
#             string = string.replace('{}', '')
#         else:
#             if len(string) == 0:
#                 flag = True
#             else:
#                 flag = False
#             break
#     print(string)
#     return flag
#
#
# a = '{[()]}'
# print(judge_str(a))


'''两个有序列表合并'''
# a = [1, 2, 4, 5, 7]
# b = [3, 4, 5, 6]
# new = []
#
# cycle_num = len(a+b)
# for i in range(cycle_num):
#     if len(a) > 0 and len(b) > 0:
#         if a[0] <= b[0]:
#             new.append(a[0])
#             a.pop(0)
#         else:
#             new.append(b[0])
#             b.pop(0)
#     else:
#         break
# if len(a) > 0:
#     new.extend(a)
# elif len(b) > 0:
#     new.extend(b)
# print(new, a, b)


'''冒泡'''
# def bubble_sort(a_list):
#     for pass_num in range(0, len(a_list)-1):
#         for i in range(len(a_list) - pass_num - 1):
#             if a_list[i] > a_list[i+1]:
#                 a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
#     return a_list
#
#
# print(bubble_sort([1, 5, 4, 6, 2, 8]))


'''插入排序'''
# def insert_sort(a_list):
#     for index in range(1, len(a_list)):
#         current_value = a_list[index]
#         position = index
#         while position > 0 and a_list[position-1] > current_value:
#             a_list[position] = a_list[position-1]
#             position -= 1
#         a_list[position] = current_value


'''选择排序'''
# def selection_sort(a_list):
#     for i in range(len(a_list)-1):
#         min = i
#         for j in range(i+1, len(a_list)):
#             if a_list[j] < a_list[min]:
#                 min = j
#         a_list[i], a_list[min] = a_list[min], a_list[i]
#     return a_list


'''词典排序'''
# from collections import Counter
#
#
# a = [1, 2, 4, 1, 4, 5, 6, 1, 7]
#
# b = dict(Counter(a))
#
# b = sorted(b.items(), key=lambda i: i[1], reverse=True)
#
# print(b[0][1])


'''两个有序链表组成有序链表'''
# a = [1, 3, 5, 7, 9, 14, 15]
# b = [0, 2, 4, 6, 8]
#
# new_list = []
# while a and b:
#     if a[0] >= b[0]:
#         new_list.append(b[0])
#         b.pop(0)
#     else:
#         new_list.append(a[0])
#         a.pop(0)
# if a:
#     new_list.extend(a)
# if b:
#     new_list.extend(b)
# print(new_list)


'''判断字符串是否成对出现'''
# a = '({[()]}'
# for i in range(len(a)//2 + 1):
#     if '()' in a:
#         a = a.replace('()', '')
#     elif '[]' in a:
#         a = a.replace('[]', '')
#     elif '{}' in a:
#         a = a.replace('{}', '')
#     else:
#         break
# if len(a) > 0:
#     flag = 0
# else:
#     flag = 1
# print(flag)


'''两个字符串类型数字相加'''
# a = '123456779'
# b = '7824876'
# e_num = abs(len(a) - len(b))
# if len(a) > len(b):
#     b = e_num * '0' + b
# elif len(a) < len(b):
#     a = e_num * '0' + a
# else:
#     pass
# a_list = list(a)
# b_list = list(b)
# new_list = []
# add_position = 0
# for i in range(max(len(a), len(b))):
#     a_num = int(a_list[-1])
#     b_num = int(b_list[-1])
#     position = (a_num + b_num + add_position) % 10
#     add_position = (a_num + b_num + add_position) // 10
#     new_list.insert(0, position)
#     a_list.pop(-1)
#     b_list.pop(-1)
# if add_position != 0:
#     new_list.insert(0, add_position)
# print(''.join(map(str, new_list)))


'''二分法查找'''
# def search(a_list, num):
#     start = 0
#     end = len(a_list)-1
#     while end >= start:
#         mid = len(a_list) // 2
#         if num > a_list[mid]:
#             start = mid + 1
#         elif num < a_list[mid]:
#             end = mid - 1
#         else:
#             return mid
#     return -1
#
#
# print(search([1, 2, 3, 4, 5], 3))






















































































































