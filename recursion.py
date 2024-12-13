# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
# print(summa(5))

stack = []
stack.append(1)
print("Add element", stack)
stack.append(2)
print("Add element", stack)
stack.append(3)
print("Add element", stack)
print(stack)
stack.pop()
print("Del elem", stack)
stack.pop()
print("Del elem", stack)
stack.pop()
print("Del elem", stack)