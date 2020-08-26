"""面试算法"""


def binary_search(a_list, item):
    """
    二分法有序查找
    :param a_list:
    :param item:
    :return:
    """
    left = 0
    right = len(a_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if a_list[mid] == item:
            return mid
        elif a_list[mid] > item:
            right = mid - 1
        elif a_list[mid] < item:
            left = mid + 1
    return -1


def bubble_sort(a_list):
    """
    冒牌排序(每一次对比相邻两个数, 每一次找出最大数放在最后)
    :param a_list:
    :return:
    """
    for index in range(len(a_list)-1, 0, -1):
        for i in range(index):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
    return a_list


def insert_sort(a_list):
    """
    插入排序(例如, [3, 2, 1, 4])
    :param a_list:
    :return:
    """
    for i in range(1, len(a_list)):
        current_value = a_list[i]
        position = i
        while position > 0:
            if a_list[position-1] > current_value:
                a_list[position] = a_list[position-1]
            position -= 1
        # 变量赋值给合适的位置
        a_list[position] = current_value
    return a_list


def string_sort(string_list):
    """
    将'+'和'-'两种字符组成的列表排序, 将+放在前面, 将-放在后面
    :param string_list:
    :return:
    """
    length = len(string_list)
    start_position = 0
    end_position = 0
    while start_position + end_position < length:
        if string_list[start_position] == '-':
            string_list[start_position], string_list[length-1-end_position] =\
                string_list[length-1-end_position], string_list[start_position]
            end_position += 1
        else:
            start_position += 1
    return string_list


def fib(n):
    """
    斐波那契(用来解决爬楼梯问题, 楼梯一次可以爬1步或者2步)
    :param n:
    :return:
    """
    a, b = 1, 1
    for i in range(n - 1):
        a, b = a + b, a
    return a


