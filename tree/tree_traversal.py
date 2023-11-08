class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value


def pre_order(root):
  if(root):
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
  if(root):
    in_order(root.left)
    print(root.value)
    in_order(root.right)


def post_order(root):
  if(root):
    post_order(root.left)
    post_order(root.right)
    print(root.value)


r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)

pre_order(r)
in_order(r)
post_order(r)
