class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BinaryTree:
  def __init__(self, arr):
    self.root = None

    self.insert_array(arr)


  def insert_array(self, arr):
    self.root = Node(arr.pop(0))
    queue = []
    queue.append(self.root)

    while(len(queue) > 0 and len(arr) > 0):
      current_node = queue.pop(0)
      left_node_value = arr.pop(0)
      right_node_value = arr.pop(0)

      if(left_node_value != None):
        current_node.left = Node(left_node_value)
        queue.append(current_node.left)

      if(right_node_value != None):
        current_node.right = Node(right_node_value)
        queue.append(current_node.right)


  def max_height(self, root):
    if(root == None):
      return 0

    return 1 + max(self.max_height(root.left), self.max_height(root.right))


  def dfs(self, root, row, left, right, grid):
    if(root == None):
      return

    mid = (left + right) // 2

    grid[row][mid] = str(root.data)

    self.dfs(root.left, row + 1, left, mid - 1, grid)
    self.dfs(root.right, row + 1, mid + 1, right, grid)


  def printTree(self):
    rows = self.max_height(self.root)
    cols = pow(2, rows) - 1
    grid = [[''] * (cols) for _ in range((rows))]

    self.dfs(self.root, 0, 0, len(grid[0]) - 1, grid)

    for row in range(0, rows, 1):
      for col in range(0, cols, 1):
        print(grid[row][col], end = '.')
      print()



def dfs_pre_order(root):
  stack = []
  path = []

  stack.append(root)

  while(len(stack) != 0):
    top = stack.pop()

    path.append(top.data)

    if(top.right is not None):
      stack.append(top.right)

    if(top.left is not None):
      stack.append(top.left)

  return path



def dfs_in_order(root):
  stack = []
  path = []

  # current_node = root

  while(len(stack) != 0 or root is not None):
    if(root is not None):
      stack.append(root)
      root = root.left
    else:
      root = stack.pop()
      path.append(root.data)
      root = root.right

  return path



def dfs_post_order(root):
  stack = []
  visited = None
  path = []

  while(len(stack) != 0 or root is not None):
    if(root is not None):
      stack.append(root)
      root = root.left
    else:
      top = stack[-1]

      if(top.right is not None and visited != top.right):
        root = top.right
      else:
        path.append(top.data)
        visited = stack.pop()

  return path



def bfs(root):
  queue = []

  queue.append(root)

  while(len(queue) != 0):
    front = queue.pop(0)

    print(front.data)

    if(front.left is not None):
      queue.append(front.left)

    if(front.right is not None):
      queue.append(front.right)



bt = BinaryTree([10,5,15,3,7,None,18])

bt.printTree()

print(dfs_pre_order(bt.root))
print(dfs_in_order(bt.root))
print(dfs_post_order(bt.root))
