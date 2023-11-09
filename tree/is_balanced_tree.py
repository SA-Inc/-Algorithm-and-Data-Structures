class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value


class Height:
  def __init__(self):
    self.height = 0


def is_balanced(root, height):
  left_height = Height()
  right_height = Height()

  if(root is None):
    return True

  left = is_balanced(root.left, left_height)
  right = is_balanced(root.right, right_height)

  height.height = max(left_height.height, right_height.height) + 1

  if(abs(left_height.height - right_height.height) <= 1):
    return left and right

  return False



r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)

r.right.left = Node(6)
r.right.right = Node(7)

print(is_balanced(r, Height()))
