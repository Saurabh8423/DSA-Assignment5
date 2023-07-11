def distance_value(arr1, arr2, d):
    distance = 0
    for num in arr1:
        found = False
        for comp in arr2:
            if abs(num - comp) <= d:
                found = True
                break
        if not found:
            distance += 1
    return distance
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
print(distance_value(arr1, arr2, d))
