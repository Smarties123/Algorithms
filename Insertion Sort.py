def insertion_sort(arr):
    a = arr

    for i in range(len(arr)):
        tmp = a[i]
        j = i - 1
        while (j >= 0 and tmp < a[j]):
            a[j+1] = a[j]
            j = j-1
        a[j+1] = tmp
    return a


test = [89, 45, 68, 90, 34, 17]
print(insertion_sort(test))
# Output [17, 34, 45, 68, 89, 90]