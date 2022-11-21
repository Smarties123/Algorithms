def bubble_sort(arr):
    a = arr

    for i in range(len(a)-1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
    return a



test = [89, 45, 68, 90, 34, 17]
print(bubble_sort(test))
# Output [17, 34, 45, 68, 89, 90]
