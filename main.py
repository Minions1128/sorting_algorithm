from sort.bubble_sort import bubble_sort, bubble_sort1
from sort.quick_sort import quick_sort, q_sort
from sort.merge_sort import merge_sort
from sort.heap_sort import heap_sort
from sort.select_sort import select_sort
from sort.insert_sort import insert_sort
from sort.shell_sort import shell_sort


if __name__ == '__main__':
    test = [5, 1, 3, 4, 2, 5, 7, 3, 6, 10, 5,
        15, 24, 100, 23, 45, 76, 3, 12, 23,
        123, 5432, 12, 2, 0, 234, 0, 122, 3, 7,
        8, 9, 238, 1000, 2345, 5678, 223, 567,
        345, 11245, 3345, 345, 12, 2]
    print test
    # print bubble_sort(test)
    # print bubble_sort1(test)
    # print quick_sort(test, 0, len(test)-1)
    # print q_sort(test)
    # print merge_sort(test)
    # print heap_sort(test)
    # print select_sort(test)
    # print insert_sort(test)
    print shell_sort(test)
