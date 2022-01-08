"""
NODE CLASS IMPLEMENTATION

- INSERT method
compares the value of the node to the parent node
and decides whether to add it as a left node or right node.

NB: if the node is greater than the parent node,
it is inserted as a right node; otherwise,​ it’s inserted left.

- FIND method
while searching for a value in the tree,
we need to traverse the node from left to right and with a parent.

"""

"""
Let's try to implement code that creates the below tree

        27
     /       \
    14       35
   /  \     /  \
  9   16   31   42 

"""

'''APPROACH I'''

class Node():
    def __init__(self, data):
        # left child (pointer)
        self.left = None
        # right child (pointer)
        self.right = None
        # node's value
        self.data = data

    def __repr__(self):
        return f'{self.data}'

node_1, node_2, node_3  = Node(27), Node(14), Node(35)
node_4, node_5, node_6, node_7 = Node(9), Node(16), Node(31), Node(42)

node_1.left, node_1.right = Node(14), Node(35)
node_2.left, node_2.right = Node(9), Node(16)
node_3.left, node_3.right = Node(31), Node(42)

print(node_3.right)

'''APPROACH II'''

# class Node():
#     def __init__(self, data):
#         # left child
#         self.left = None
#         # right child
#         self.right = None
#         # node's value
#         self.data = data

#     def insert(self, data):
#         # Compare the new value with the parent node
#         if self.data:                       # check if there is data in the root
#             # left child is smaller than the parent 
#             if data < self.data:
#                 if self.left is None:       # if node does not have a value
#                     self.left = Node(data)
#                 else:                       # if there is some value in that node
#                     self.left.insert(data)  # recursively check the left of the tree
            
#             # right child is greater than the parent 
#             #   all operations are mirrored from the above 
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:                              # if you don't have a root, set data to root
#             self.data = data

#         # findval method to compare the value with nodes

#     def find_value(self, val):
#         if val < self.data:
#             if self.left is None:
#                 return str(val) + " is not Found"
#             return self.left.find_value(val)
#         elif val > self.data:
#             if self.right is None:
#                 return str(val) + " is not Found"
#             return self.right.find_value(val)
#         else:
#             return str(self.data) + " is found"

#     # Print the tree
#     def print_tree(self):
#         if self.left:
#             self.left.print_tree()
#         print(self.data),
#         if self.right:
#             self.right.print_tree()

# # Use the insert method to add nodes
# root = Node(27)
# root.insert(42)
# root.insert(14)
# root.insert(35)
# root.insert(31)
# root.insert(9)
# root.insert(16)

# # The above code will create root node as 27, left child as 14, and right child as 35.
# root.print_tree()

# """
# We created tree with 9 14 16 27 31 35 nodes. 
# In this tree value 7 is not there so it gives the output as 7 not found. 
# 14 is the left child root, hence found. 

# """

# print(root.find_value(7))
# print(root.find_value(14))

'''APPROACH III - optional'''
# Approach to implement binary search tree with a slightly nicer visualisation
# class bst:
#     def __init__(self, value):
#         self.value = value
#         self.right = None
#         self.left = None
        
# def insert(root, key):
#     if not root:
#         return bst(key)
#     if key >= root.value:
#         root.right = insert(root.right, key)
#     elif key < root.value:
#         root.left = insert(root.left, key)
#     return root

# def insert_values(root, values):
#     for value in values:
#         root = insert(root, value)
#     return root

# def print2DTree(root, space=0, LEVEL_SPACE = 5):
#     if (root == None): return
#     space += LEVEL_SPACE
#     print2DTree(root.right, space)
#     # print() # neighbor space
#     for i in range(LEVEL_SPACE, space): print(end = " ")  
#     print("|" + str(root.value) + "|<")
#     print2DTree(root.left, space)

# root = insert_values(None, [27, 14, 35, 31, 9, 16, 42])
# print2DTree(root)  