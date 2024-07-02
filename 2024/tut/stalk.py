class Stack():
    
    def __init__(self):
        self.stack = list()
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
    
    def __str__(self):
        return str(self.stack)
    
    
    
mystack = Stack()
mystack.push(1)
mystack.push(3)
print(mystack)
print(mystack.pop())
print(mystack.peek())
print(mystack.pop())
print(mystack.pop())