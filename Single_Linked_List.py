# Q2.1
import array as arr  #

first_set = arr.array('i', [])  # creating an array
second_set = arr.array('i', [])  # creating an array

for x in range(0, 6):
    inp1 = int(input('PLease enter an even number from 1 to 12:'))  # accepting an input
    first_set.append(inp1)  # adding the data into the array

for x in range(0, 4):
    inp2 = int(input('PLease enter an odd number from 20 to 40:'))  # accepting an input
    second_set.append(inp2)  # adding the data into the array

# Q2.2


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

# Q2.3


class Node:
    def __init__(self, data=None):  # creates a new node
        self.data = data  # this is the variable for the data of the node
        self.next = None  # this is the pointer to the next node in the linked list


class LinkedLists:
    def __init__(self):
        self.head = Node()  # creating a head node

    def new_item(self, data):
        new_node = Node(data)  # creates a new node with the accepted data
        current = self.head  # sets an iterator equal to the original node
        while current.next != None:  # a while loop that will iterate through the linked list until
            current = current.next   # the last node is found
        current.next = new_node  # setting the node with no data equal to the accepted data

    def printer(self):
        current = self.head  # sets an iterator equal to the original node
        while current.next !=None:  # a while loop that will iterate through the linked list
            current = current.next  # iterates through each position in the linked list
            print(current.data, " --> ", end='')  # prints out that position in the list
        print('')  # printing out a string so that each print out of the linked list is on its own respective line

    def clear(self):
        current = self.head  # sets an iterator equal to the original node
        while current.next != None:  # a while loop that will iterate through the linked list
            pos = current.next  # iterates through each position in the linked lists
            del current.data  # deletes the data within that position
            current = pos  # assign the position to  the current variable so that the while loop can keep running


Linked_List = LinkedLists()  # creates the linked list

for x in final_set:  # iterates through the array created
    Linked_List.new_item(x)  # inserts each item from the array into the linked list

print('Linked list in same order as merge sorted arrays:')
Linked_List.printer()  # prints out the contents of the linked list
Linked_List.clear()  # clears the linked list so that the reversed array can be inserted

Linked_List = LinkedLists()  # creates a new linked list

final_set.reverse()  # reverses the array
for x in final_set:
    Linked_List.new_item(x)  # inserts the items from the reversed array into the linked lists

print('Linked list in reverse order as merge sorted arrays:')
Linked_List.printer()  # prints out the contents of the linked list

print('Linked list in reverse order as merge sorted arrays after the value 45 is added:')
Linked_List.new_item(45)  # inserts the value 45 into the last position in the linked list
Linked_List.printer()  # prints out the contents of the linked list
