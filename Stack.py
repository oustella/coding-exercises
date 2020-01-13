# Implementing a stack using a list

# class StackNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return self.data
#
#
# class MyStack:
#     def __init__(self, item):
#         self.top = StackNode(item)
#
#     def display(self):
#
#
#     def pop(self):
#         if not self.top:
#             return 'The stack is empty.'
#         else:
#             item = self.top.data
#             self.top = self.top.next
#             return item
#
#     def push(self, item):
#         new_node = StackNode(item)
#         new_node.next = self.top
#         self.top = new_node
#
#
# MyStack('A')
# MyStack.push('B')
# MyStack.pop()