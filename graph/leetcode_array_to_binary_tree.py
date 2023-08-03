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


  def print(self):
    rows = self.max_height(self.root)
    cols = pow(2, rows) - 1
    grid = [[''] * (cols) for _ in range((rows))]

    self.dfs(self.root, 0, 0, len(grid[0]) - 1, grid)

    for i in range(0, len(grid), 1):
      print(grid[i])


  def max_height(self, root):
    if(root == None):
      return 0

    return 1 + max(self.max_height(root.left), self.max_height(root.right))



bt1 = BinaryTree([7,4,3,None,None,6,19])

bt1.print()
