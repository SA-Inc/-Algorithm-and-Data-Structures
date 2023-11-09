class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value


def count_nodes(root):
  if(root is None):
    return 0
  return (1 + count_nodes(root.left) + count_nodes(root.right))


def is_complete(root, index, node_count):
  if(root is None):
    return True
  if(index >= node_count):
    return False
  return (is_complete(root.left, 2 * index + 1, node_count) and is_complete(root.right, 2 * index + 2, node_count))


r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)

r.right.left = Node(6)
r.right.right = Node(7)

print(count_nodes(r))
print(is_complete(r, 0, count_nodes(r)))
