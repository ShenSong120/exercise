def binary_search(a_list, item):
    """二分查找"""
    first = 0
    last = len(a_list) - 1

    while first <= last:
        mid = (first + last) // 2
        print(mid)
        if a_list[mid] > item:
            last = mid - 1
        elif a_list[mid] < item:
            first = mid + 1
        else:
            return mid + 1
    return -1


def bubble_sort(a_list):
    """
    冒泡排序
    :param a_list:
    :return:
    """
    for pass_num in range(len(a_list)-1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
    return a_list


def insert_sort(a_list):
    """
    插入排序
    :param a_list:
    :return:
    """
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position-1] > current_value:
            a_list[position] = a_list[position-1]
            position -= 1
        a_list[position] = current_value


def select_sort(a_list):
    """
    选择排序
    :param a_list:
    :return:
    """
    for i in range(len(a_list)-1):
        min_index = i
        for j in range(i+1, len(a_list)):
            if a_list[j] < a_list[min_index]:
                min_index = j
        a_list[i], a_list[min] = a_list[min], a_list[i]
    return a_list


def quick_sort(a_list):
    """
    快速排序
    :param a_list:
    :return:
    """
    if len(a_list) < 2:
        return a_list
    mid = a_list[len(a_list)//2]
    left, right = [], []
    a_list.remove(mid)
    for item in a_list:
        if item >= mid:
            right.append(item)
        else:
            left.append(item)
    return quick_sort(left) + [mid] + quick_sort(right)


def judge_str(a_list):
    if len(a_list) < 2 or len(a_list)%2 != 0:
        if a_list == '':
            return True
        else:
            return False
    cycle_flag = True
    while cycle_flag is True:
        a_list = a_list.replace('{}', '').replace('[]', '').replace('()', '')
        if '[]' in a_list:
            pass
        elif '()' in a_list:
            pass
        elif '{}' in a_list:
            pass
        else:
            cycle_flag = False
    if len(a_list) > 0:
        return False
    else:
        return True


def list_sort(a_list, b_list):
    """
    将两个有序链表合并为一个
    :param a_list:
    :param b_list:
    :return:
    """
    result = []
    while a_list and b_list:
        if a_list[0] < b_list[0]:
            result.append(a_list[0])
            a_list.pop(0)
        else:
            result.append(b_list[0])
            b_list.pop(0)
    if a_list:
        result.extend(a_list)
    if b_list:
        result.extend(b_list)
    return result


a = [1, 2, 1, 3, 5]
b = set(a)
b.add(6)
print(b)









































































