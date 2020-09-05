class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.depth = 0
        self.data = data

# Insert method to create nodes
    def insert(self, data, d=1):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    self.left.depth = d
                else:
                    d += 1
                    self.left.insert(data, d)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                    self.right.depth = d
                else:
                    d += 1
                    self.right.insert(data, d)

        else:
            self.data = data

    def remove(self, data):
        if data < self.data:
            if self.left is None:
                print(f'{data} is not found')
            else:
                self.left.remove(data)
        elif data > self.data:
            if self.right is None:
                print(f'{data} is not found')
            else:
                self.right.remove(data)
        else:
            if self.left is None and self.right is None:
                print(f'{self.data} was found for deleting')
                del self.data




    # findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" is not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" is not Found"
            return self.right.findval(lkpval)
        else:
            return str(self.data) + " is found"

# Print the tree
    def PrintTree(self):
        if self.right:
            self.right.PrintTree()

        for d in range(self.depth):
            print('-', end='')

        print(f"{self.data} ({self.depth})")

        if self.left:
            self.left.PrintTree()



root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)

root.PrintTree()

print('--------------------')
root.remove(10)
print('--------------------')

root.PrintTree()

#
# print('--------------------')
# root.remove(19)
# root.PrintTree()
#
# print('--------------------')
# root.remove(35)
# root.PrintTree()
