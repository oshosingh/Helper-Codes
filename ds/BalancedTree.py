class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def insert(self, root, key):
        
        # Step 1 Perform Normal BST
        if not root:
            return TreeNode(key)
        elif key<root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2 Update the height of the ancestor node
        root.height = 1 + max(self.__getHeight(root.left), self.__getHeight(root.right))

        # Step 3 Get the balance factor
        balance = self.__getBalance(root)

        # Step 4 If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        
        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Perform Rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1+max(self.__getHeight(z.left), self.__getHeight(z.right))
        y.height = 1+max(self.__getHeight(y.left), self.__getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # Perfrom Rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1+max(self.__getHeight(z.left), self.__getHeight(z.right))
        y.height = 1+max(self.__getHeight(y.left), self.__getHeight(y.right))

        return y

    def __getHeight(self, root):
        if not root:
            return 0

        return root.height

    def __getBalance(self, root):
        if not root:
            return 0

        return self.__getHeight(root.left)-self.__getHeight(root.right)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

myTree = AVL()
root = None
 
root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)

print("Preorder traversal of the",
      "constructed AVL tree is")
myTree.preOrder(root)
print()
        
