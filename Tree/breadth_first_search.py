class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
  
def BFS(root):
    if root:
        q=[]
        q.append(root)
        while(len(q)>0):
            print(q[0].data)
            node=q.pop(0)
            
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
BFS(root)


        