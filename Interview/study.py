

def binary_search(a_list, item):
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
