class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value


def in_order(root):
  if(root):
    in_order(root.left)
    print(root.value)
    in_order(root.right)


def insert(node, value):
  # if tree is empty, create new node
  if(node is None):
    return Node(value)

  # go through tree and insert new node to right place
  if(value < node.value):
    node.left = insert(node.left, value)
  else:
    node.right = insert(node.right, value)
  return node


def min_value(node):
  current = node
  while(current.left is not None):
    current = current.left
  return current


def delete(node, value):
  # if tree empty
  if(node is None):
    return node

  # find value to delete
  if(value < node.value):
    node.left = delete(node.left, value)
  elif(value > node.value):
    node.right = delete(node.right, value)
  else:
    # found and if node has only one or none child, return other side node
    if(node.left is None):
      tmp = node.right
      node = None
      return tmp
    if(node.right is None):
      tmp = node.left
      node = None
      return tmp

    # if node has two children, get min of sub tree and delete
    tmp = min_value(node.right)
    node.value = tmp.value
    node.right = delete(node.left, tmp.value)

  return node



r = None
r = insert(r, 8)
r = insert(r, 3)
r = insert(r, 1)
r = insert(r, 6)
r = insert(r, 7)
r = insert(r, 10)
r = insert(r, 14)
r = insert(r, 4)

in_order(r)

# print(min_value(r).value)

delete(r, 10)

print()

in_order(r)
