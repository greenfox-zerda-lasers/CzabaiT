# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack(object):
    elements = []
    last = 0
    length = 0

    def __init__(self):
        pass

    def push(self,element):
        self.elements.append(element)

    def pop(self):
        self.last = self.elements[-1]
        del self.elements[-1]
        return self.last

    def size(self):
        for i in self.elements:
            self.length += 1
        return self.length

stack1 = Stack()
stack1.push(4)
stack1.push(5)
print(stack1.pop())
print(stack1.size())