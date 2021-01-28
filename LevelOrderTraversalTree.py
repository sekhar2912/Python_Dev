
leftView = []
rtView = []

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    

def print_level_order_traversal(root):
    queue = []

    if root is None:
        return
    if root.data != None:
        queue.append(root)

    while len(queue) > 0:
        root = queue.pop(0)
        print(root.data)
        if(root.left != None):  queue.append(root.left)
        if(root.right != None ): queue.append(root.right)
        
       
def print_level_by_level_traversal(root):
    queue = []
    if root is None:
        return
    if root.data != None:
        queue.append(root)
        queue.append('NULL')
    
    temp = []
    mRet = set(list())
    print("----Level Order Traversal---")
    while len(queue) > 0:
        
        if len(queue) == 1 and root == 'NULL' :
            break
        root = queue.pop(0) 
        if root != None and root != 'NULL':
            temp.append(root.data)
            if(root.left != None):  queue.append(root.left)
            if(root.right != None ): queue.append(root.right)
        elif root == 'NULL' : 
            queue.append('NULL')
            if len(temp) > 0 :
                print(temp)
           
                print("-------------")
                
                leftView.append(temp[0])
                rtView.append(temp[-1])
                temp.clear()
    print(mRet)

# def levelOrder(root):
#     queue = []
#     temp = []
#     mRetList = []
#     if root is None:
#         return
#     if root.data != None:
#         queue.append(root)
#         queue.append('NULL')
    
#     while(len(queue) > 0):
#         if len(queue) == 1 and root == 'NULL' :
#             break
#         root = queue.pop(0)
        
#         if root != None and root != 'NULL':
#             temp.append(root.data)
#             if root.left != None: temp.append(root.left)
#             if root.right != None: temp.append(root.right)
#         elif root == 'NULL':
#             queue.append('NULL')
#             if len(temp) > 0:
#                 print(temp)
#                 mRetList.append(temp)
#                 temp.clear()
    
#     return mRetList 

def print_inorder_traversal(root):

    current = root
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left  # This is trigger for else block of code
        elif (stack):
            current = stack.pop()
            print(current.data,end=" *** ")
            current = current.right

        else:
            break
        
def print_preorder_traversal_rec(root):

    if root:
        print(root.data,end=" *** ")
        print_preorder_traversal_rec(root.left)
        print_preorder_traversal_rec(root.right)

def print_Inorder_traversal_rec(root):

    if root:
        print_Inorder_traversal_rec(root.left)
        print(root.data,end=" *** ")
        print_Inorder_traversal_rec(root.right)

def print_postorder_traversal_rec(root):

    if root:
        print_postorder_traversal_rec(root.left)
        print_postorder_traversal_rec(root.right)
        print(root.data,end=" *** ")
        

root = Node(12) 
root.left = Node(10) 
root.right = Node(20) 
root.right.left = Node(25) 
root.right.right = Node(40) 

#levelOrder(root)
print_level_by_level_traversal(root)

print("Left View " , leftView)
print("Right View " , rtView)

print_inorder_traversal(root)
print("Printing Recurrsion",end="**")
print_Inorder_traversal_rec(root)
print_preorder_traversal_rec(root)
print_postorder_traversal_rec(root)


#    12
# 10  20
#    25   40



