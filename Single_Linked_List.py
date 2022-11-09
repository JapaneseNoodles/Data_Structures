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
