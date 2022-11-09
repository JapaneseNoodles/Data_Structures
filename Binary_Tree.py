class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_child(self, data):
        if data == self.data:
            return

        if self.data is None:
            self.data = BinarySearchTree(data)

        if data < self.data:
            if self.left_child:
                self.left_child.add_child(data)
            else:
                self.left_child = BinarySearchTree(data)
        else:
            if self.right_child:
                self.right_child.add_child(data)
            else:
                self.right_child = BinarySearchTree(data)

    def preorder(self):
        items = []

        if self.left_child:
            items += self.left_child.preorder()

        items.append(self.data)

        if self.right_child:
            items += self.right_child.preorder()

        return items


numbers = [5, 7, 2, 3, 8, 9, 0]
root = BinarySearchTree(numbers[0])

for x in range(1, len(numbers)):
    root.add_child(numbers[x])

print(root.preorder())
