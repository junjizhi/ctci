# Implement a merge sort in python

def sort_array(a):
    n = len(a)
    merge_sort(a, 0, n-1)
    return a

def merge_sort_array(a, start, end):
    if start == end:
        return
    else:
        middle = (start + end) / 2
        merge_sort(a, start, middle)
        merge_sort(a, middle+1, end)
        # merge two sub-arrays
        left_index = start
        right_index = middle + 1
        n = end + 1 - start
        temp_arr = []
        while left_index <= middle and right_index <= end:
            if a[left_index] < a[right_index]:
                temp_arr.append(a[left_index])
                left_index += 1
            else:
                temp_arr.append(a[right_index])                
                right_index += 1
        for i in range(left_index, middle+1):
            temp_arr.append(a[i])
        for i in range(right_index, end+1):
            temp_arr.append(a[i])
        for i in range(n):
            a[start+i] = temp_arr[i]

a = [6,5]
b = [9,1,5,2,3]
print "a=", a
print "merge sorted a=", sort_array(a)
print "b=", b
print "merge sorted b=", sort_array(b)
