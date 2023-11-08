class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value


def is_full_tree(root):
  # if tree empty
  if(root is None):
    return True
  # if both child does not exist
  if(root.left is None and root.right is None):
    return True
  # else check
  if(root.left is not None and root.right is not None):
    return is_full_tree(root.left) and is_full_tree(root.right)
  return False


r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)

r.right.left = Node(6)
r.right.right = Node(7)

print(is_full_tree(r))
