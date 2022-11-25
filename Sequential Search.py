def sequential_search(arr, k):

    i = 0
    while(i <= len(arr) and arr[i] != k):
        i += 1
    if i<len(arr):
        return i
    else:
        return -1


a = [11, 12, 13, 16, 19, 20, 25, 27, 30, 35, 39, 41, 66]
key_value = 19
print(sequential_search(a, key_value))