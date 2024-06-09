def find_division_point(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == 0 and arr[mid + 1] == 1:
            return mid
        elif arr[mid] == 0:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
result = find_division_point(arr)
print("Место разделения: Индекс", result)
