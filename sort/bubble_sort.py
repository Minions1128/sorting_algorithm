import time

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            # time.sleep(0.001)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def bubble_sort1(array):
    for i in range(len(array)):
        flag = True
        for j in range(len(array)-i-1):
            # time.sleep(0.001)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = False
        if flag:
            return array