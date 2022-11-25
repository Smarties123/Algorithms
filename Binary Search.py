from math import floor

def binary_search(arr, k):

    l = 0
    r = len(arr)-1
    
    while (l <= r):
        mid = floor((l+r)/2)
        if k == arr[mid]:
            return mid
        else:
            if k < arr[mid]:
                r = mid-1
            else:
                l = mid+1
    return -1 # key_value not in array

a = [11, 12, 13, 16, 19, 20, 25, 27, 30, 35, 39, 41, 66]
key_value = 19
print(binary_search(a, key_value))