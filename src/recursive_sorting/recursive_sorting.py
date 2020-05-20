# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    def sort(a_index=0, b_index=0, index=0):
        if index >= len(merged_arr):
            return merged_arr
        else:
            if a_index > len(arrA) - 1:
                merged_arr[index] = arrB[b_index]
                index += 1
                b_index += 1
                sort(a_index, b_index, index)
            elif b_index > len(arrB) - 1:
                merged_arr[index] = arrA[a_index]
                index += 1
                a_index += 1
                sort(a_index, b_index, index)
            elif arrA[a_index] <= arrB[b_index]:
                merged_arr[index] = arrA[a_index]
                index += 1
                a_index += 1
                sort(a_index, b_index, index)
            else:
                merged_arr[index] = arrB[b_index]
                index += 1
                b_index += 1
                sort(a_index, b_index, index)
    sort()
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    elif len(arr) > 2:
        #split the array
        dividing_index = (len(arr) - 1) // 2
        arr1 = arr[0:dividing_index]
        arr2 = arr[dividing_index:len(arr)]
        sorted_pairs1 = merge_sort(arr1)
        sorted_pairs2 = merge_sort(arr2)
        return merge(sorted_pairs1, sorted_pairs2)
    else:
        if arr[0] < arr[1]:
            return arr
        else:
            arr[0], arr[1] = arr[1], arr[0]
            return arr
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end, right_start=None):
    # Your code here
    if right_start is None:
        right_start = mid + 1 
    # Two pointers to maintain start 
    # of both arrays to merge 
    if start <= mid and right_start <= end: 
        # If element 1 is in right place 
        if (arr[start] <= arr[right_start]): 
            start += 1
            merge_in_place(arr, start, mid, end, right_start)
        else: 
            value = arr[right_start]
            index = right_start
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): 
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            # Update all the pointers 
            start += 1
            mid += 1
            right_start += 1
            merge_in_place(arr, start, mid, end, right_start)



def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        mid = (l + r - 1) // 2
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)
        merge_in_place(arr, l, mid, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

def partition(data):
    pivot = data[0]
    left = []
    right = []
    for x in data[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return left, pivot, right

def quicksort(arr): # O(nlogn) - best time complexity for general purpose sorting
    #find pivot - midpoint, first or last
    if len(arr) <= 1:
        return arr

    left, pivot, right = partition(arr)

    return quicksort(left) + [pivot] + quicksort(right)

def partition_in_place(data, start, end):
    pivot = data[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if data[j] <= pivot:
            data[j], data[i] = data[i], data[j]
            i += 1
        j += 1
    data[start], data[i - 1] = data[i - 1], data[start]
    return i - 1

def quicksort_in_place(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return
    #find pivot - midpoint, first or last

    index = partition_in_place(arr, start, end)

    quicksort_in_place(arr, start, index - 1) # left of pivot
    quicksort_in_place(arr, index + 1, end) # right of pivot

# arr1 = [1,3,5,7,9]
# arr2 = [2,4,6,8]

# merged_array = merge(arr1, arr2)
# print(merged_array)

# arr3 = [5, 7, 3, 9, 1]
# arr4 = [6, 4, 8, 2, 16, 10, 14, 12]
# # quicksort_in_place(arr4)
# # print(arr4)

# arr5 = [1,3,5,7,9,2,4,6,8]
# print(merge_in_place(arr5, 0, 4, 8))
# print(arr5)

# merge_sort_in_place(arr4, 0, len(arr4) - 1)
# print(arr4)