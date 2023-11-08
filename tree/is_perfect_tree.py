class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value


def max_depth(node):
  if(node is None):
    return 0
  else:
    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)
    if(left_depth > right_depth):
      return left_depth + 1
    else:
      return right_depth + 1


def is_perfect_tree(root, depth, level = 0):
  if(root is None):
    return True
  if(root.left is None and root.right is None):
    return (depth == level + 1)
  if(root.left is None or root.right is None):
    return False
  return is_perfect_tree(root.left, depth, level + 1) and is_perfect_tree(root.right, depth, level + 1)


r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)

# r.right.left = Node(6)
# r.right.right = Node(7)

print(max_depth(r))
print(is_perfect_tree(r, max_depth(r)))
