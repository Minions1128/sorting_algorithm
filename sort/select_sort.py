def select_sort(array):
    for i in range(len(array)):
        _min = i
        for j in range(i, len(array)):
            if array[j] < array[_min]:
                _min = j
        array[_min], array[i] = array[i], array[_min]
    return array