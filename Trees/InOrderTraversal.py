# InOrder: Left Root Right
# Traverse Left subtree --> Visit the root node --> Traverse the right subtree
class InOrderTraversal:
  def inorderFn(self, root):
    if root is None:
      return []
    return self.inorderFn(root.left)+[root.val]+self.inorderFn(root.right)
