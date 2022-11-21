def selection_sort(arr):
    a = arr

    for i in range(len(a)):
        mini = i

        for j in range(i, len(a)):
            if a[j] < a[i]:
                mini = j
            tmp = a[i]
            a[i] = a[mini]
            a[mini] = tmp

    return a
    



test = [89, 45, 68, 90, 34, 17]
print(selection_sort(test))
