class Tree(object):                                               #Define a Tree Node property
    def __init__(self):                                             
        self.left=None
        self.right=None
        self.data=None

root=Tree()                                                       # Create a empty Tree Node
root.data="root"                                                 # Assign the root value =root
root.left=Tree()                                                 ## Create a empty Tree Node left to parent node root
root.left.data="left"                                               # Assign the value node left to root node =left
root.right=Tree()
root.right.data="right"

# Print th values
print("Print  :"+root.data)                                               
print("Print  :"+root.left.data)
print("Print :" + root.right.data)



        

            
            