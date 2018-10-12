# stack data structure could be lifo or filo
# https://www.geeksforgeeks.org/stack-data-structure/
# https://www.youtube.com/watch?v=0Zsabo7ires
# https://www.youtube.com/watch?v=QVcsSaGeSH0
# https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/
# BEST RESOURCE:  https://www.youtube.com/watch?v=6oL-0TdVy28

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # check if the current node is empty or null
    # display the value of the root or current node
    # traverse the left subtree by recursively calling the dfs function
    # traverse the right subtree by recursively calling the dfs function
    
     



  def breadth_first_for_each(self, cb):
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
