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

    
    # Recursive function to delete a node with
    # given key from subtree with given root.
    # It returns root of the modified subtree.
    def delete(self, root, key):
  
        # Step 1 - Perform standard BST delete
        if not root:
            return root
  
        elif key < root.val:
            root.left = self.delete(root.left, key)
  
        elif key > root.val:
            root.right = self.delete(root.right, key)
  
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
  
            elif root.right is None:
                temp = root.left
                root = None
                return temp
  
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,
                                      temp.val)
  
        # If the tree has only one node,
        # simply return it
        if root is None:
            return root
  
        # Step 2 - Update the height of the 
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
  
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
  
        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
  
        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
  
        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
  
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
  
        return root
    
        
