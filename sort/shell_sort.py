def shell_sort(array):
    length = len(array)
    gap = int(round(length/2))
    while gap > 0:
        print gap
        for i in range(gap, length):
            if array[i] < array[i-gap]:
                array[i], array[i-gap] = array[i-gap], array[i]
        gap = int(round(gap/2))
    return array
