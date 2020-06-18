

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


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 8))


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
