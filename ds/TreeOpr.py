class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class TreeOpr:
    def __init__(self):
        self.tree = None

    # level order insertion
    def insert(self, x):
        if not self.tree:
            self.tree = TreeNode(x)
            return

        q = []
        q.append(self.tree)

        while q:
            temp = q.pop(0)
            if not temp.left:
                temp.left = TreeNode(x)
                break
            else:
                q.append(temp.left)

            if not temp.right:
                temp.right = TreeNode(x)
                break
            else:
                q.append(temp.right)

    # lowerst common ancestor
    def lca(self,root:'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root == p or root == q:
            return self.tree

        left_lca = self.lca(root.left, p, q)
        right_lca = self.lca(root.right, p, q)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca else right_lca

        left_lca = self.lcs()
        

        
            
    
