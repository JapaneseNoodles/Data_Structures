def merge_sort(array):
    if len(array) <= 1:   # making sure the array has more the 1 data value
        return array

    midp = len(array)//2  # finding half of the length of the data
    left_half = array[:midp]  # creating an array with all the data up to the midpoint
    right_half = array[midp:]  # creating an array with all the data after the midpoint

    left_half = merge_sort(left_half)  # using recursion, this divides the array into its individual components
    right_half = merge_sort(right_half)  # using recursion, this divides the array into its individual components

    return merge_two(left_half, right_half)  # this merges the two arrays


def merge_two(array1, array2):
    i = 0
    y = 0

    len_first = len(array1)  # finding the length of the array
    len_second = len(array2)  # finding the length of the array

    sorted_set = arr.array('i', [])  # creating a new array for the organised set

    while i < len_first and y < len_second:
        if array1[i] <= array2[y]:  # if the data value of the one array is less than the other array
            sorted_set.append(array1[i])  # then that data is stored in the array
            i += 1  # increase the iterator
        else:
            sorted_set.append(array2[y])  # if the previous condition is not met then the other data value is stored
            y += 1  # increases the iterator
    while i < len_first:  # if the one set is longer than the other then the previous loop does not complete the sort
        sorted_set.append(array1[i])  # therefore this loop inserts the rest of the data
        i += 1  # increases the iterator
    while y < len_second:
        sorted_set.append(array2[y])
        y += 1

    return sorted_set


final_set = merge_two(merge_sort(first_set), merge_sort(second_set))  # this merges the two sorted arrays by merge
                                                                      # sorting the two arrays respectively and then
print(final_set)  # prints the merged array                             merges them together