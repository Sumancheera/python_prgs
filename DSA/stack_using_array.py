#python prg to implement stack implementation using list
stack=[]
#append() fun to push
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print("initial stack")
print(stack)

#pop() fun to pop element from stack in LIFO order
print("\n elements popped from stack:")
print(stack.pop()) # pop will remove last val in list like stack pop
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop()) #[] will come for stack under flow
print(stack)

