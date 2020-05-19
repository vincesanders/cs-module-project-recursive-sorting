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
def merge_in_place(arr, start, mid, end):
    # Your code here
    if start > mid:
        return arr
    elif end >= len(arr):
        return arr
    if arr[start] <= arr[end]:
        start += 1
        return merge_in_place(arr, start, mid, end)
    else:
        arr[start], arr[end] = arr[end], arr[start]
        end += 1
        return merge_in_place(arr, start, mid, end)
    # if index >= len(arr):
    #     return arr
    # else:
    #     if start > len(arrA) - 1:
    #         arr[index] = arrB[end]
    #         index += 1
    #         end += 1
    #         merge_in_place(start, end, index)
    #     elif end > len(arrB) - 1:
    #         arr[index] = arrA[start]
    #         index += 1
    #         start += 1
    #         merge_in_place(start, end, index)
    #     elif arrA[start] <= arrB[end]:
    #         arr[index] = arrA[start]
    #         index += 1
    #         start += 1
    #         merge_in_place(start, end, index)
    #     else:
    #         arr[index] = arrB[end]
    #         index += 1
    #         end += 1
    #         merge_in_place(start, end, index)
    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


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
# quicksort_in_place(arr4)
# print(arr4)

arr5 = [1,3,5,7,9,2,4,6,8]
merge_in_place(arr5, 0, 4, 5)
print(arr5)