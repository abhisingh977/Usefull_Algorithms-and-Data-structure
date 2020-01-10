class Node:
    def __init__(self, data):                       #Create a tree Node
        self.left=None
        self.rigth=None
        self.data=data
    
    def insert(self, data):                         # Insert new Node in the tree
        if self.data:                               
            if data < self.data:                    # If new Node data is less the go to left branch 
                if self.left is None:               # If there is not Node in left then create a node with the data
                    self.left = Node(data)
                else:
                    self.left.insert(data)          # If a Node exist then compare the node with data recursively
            elif data> self.data:                    # If new Node data is greater the go to left branch 
                if self.rigth is None:                # If there is not Node in right then create a node with the data  
                    self.rigth=Node(data)
                else: self.rigth.insert(data)           # If a Node exist then compare the node with data recursively
        else:
            self.data=data
            
    def PrintTree(self):                                # Print the Tree inorder way...
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.rigth:
            self.rigth.PrintTree()
root=Node(7)                                    # Create the Tree root
root.insert(2)                                  # Add the nodes....
root.insert(6)
root.insert(5)
root.insert(12)
root.insert(24)
root.insert(6)

root.PrintTree()