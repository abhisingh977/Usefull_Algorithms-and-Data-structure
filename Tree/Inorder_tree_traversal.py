class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
    def insert(self,val):
        if self.val:
            if val<self.val:
                if self.left is None:
                    self.left=Node(val)
                else: 
                    self.left.insert(val)
            elif val>self.val:
                if self.right is None:
                    self.right=Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val=val
list=[]
def inorder(root):                                                  
    
    if root:
        inorder(root.left)                                   #Traverse the left nodes firstS
        list.append(root.val)
        inorder(root.right)
    return(list)



root=Node(7)
root.insert(6)
root.insert(3)
root.insert(13)
root.insert(5)
root.insert(8)
root.insert(4)
root.insert(9)
root.insert(12)


trav=inorder(root)
print(trav)