class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Double:
    def __init__(self):
        self.head = None

    def new(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None

    def pre_new(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node

    def print(self):
        current = self.head
        list_print = []
        while current:
            list_print.append(current.data)
            current = current.next

        return list_print


names = ['Ashley', 'Connor', 'Teagan']

lists = Double()

for x in names:
    lists.new(x)

print(lists.print())

lists.pre_new('Stephen')

print(lists.print())
