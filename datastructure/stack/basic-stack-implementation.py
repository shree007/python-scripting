

class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return len(self.items) == 0
    
	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.is_empty():
			return self.items.pop()
		else:
			return "stack is empty"

	def peek(self):
		if not self.is_empty():
			return self.items[-1]
		else:
			return "stack is empty"

	def size(self):
		return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.pop())