def binary_search(list, item):
    low = 0
    high = len(list) - 1
    mid = int((low + high) / 2)
    while low <= high:
        if item == list[mid]:
            return mid + 1
        elif item < list[mid]:
            high = mid - 1
            mid = int((low + high) / 2)

        elif item > list[mid]:
            low = mid + 1
            mid = int((low + high) / 2)
    return None
