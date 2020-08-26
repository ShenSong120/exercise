# 1.手写一个python类




# 2.直接手写一个构造函数





# 3.紧接着上面的代码, 直接手写, 补充完整代码, 要求(对列表中的人进行排序, 并筛选出分数大于80的人名单, 组成新的列表并显示)


class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Student(Person):
    def __init__(self, name, gender, age,score):
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


'''二分法查找'''
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


# '''插入排序'''
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






















































































