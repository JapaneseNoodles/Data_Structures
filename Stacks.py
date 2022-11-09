class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, category):
        self.stack.append(category)

    def pop(self):
        self.stack.pop()


ask = 'yes'
array = ArrayStack()

while ask != 'no':
    ask = input('Would you like to enter or delete a category?: ')
    if ask == 'enter':
        food_category = input('Enter the category here: ')
        array.push(food_category)
    elif ask == 'delete':
        array.pop()
    elif ask == 'no':
        ask = 'no'

print(array.stack)

