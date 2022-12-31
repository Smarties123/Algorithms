def quick_sort(arr):
    
    

    s1 = [] # i < pivot
    s2 = [] # i = pivot
    s3 = [] # i > pivot

    if (len(arr) > 1):

        pivot = arr[0]

        for i in arr:
            if (i<pivot):
                s1.append(i)
            elif (i>pivot):
                s3.append(i)
            else: # i == pivot
                s2.append(i)
        # quick_sort(s1)
        # quick_sort(s3)
        
        # arr_2 = []
        # for i in s1:
        #     arr_2.append(i)
        # for i in s2:
        #     arr_2.append(i)
        # for i in s3:
        #     arr_2.append(i)
        return quick_sort(s1) + s2 + quick_sort(s3)

        
    else:
        return arr


array = [7,2,9,4,3,8,6,1]
print(quick_sort(array))