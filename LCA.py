
class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def lca(root, n1, n2): 
    while root: 
        # If both n1 and n2 are smaller than root, 
        # then LCA lies in left 
        if root.data > n1 and root.data > n2: 
            root = root.left 
          
        # If both n1 and n2 are greater than root,  
        # then LCA lies in right 
        elif root.data < n1 and root.data < n2: 
            root = root.right 
  
        else: 
            break
  
    return root 

root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
  
n1 = 4 ; n2 = 8
t = lca(root, n1, n2) 
print(t.data) 

    #        20
    #     8      22
    # 4       12
    #      10    14