"""
This problem was asked by Google.

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
"""

"""
[X] Create a tree node with a value and an option for left and right nodes
[X] Create a method to check sum of nodes
[ ] Create a container to hold a dictionary of seen node values to compare to any new node value
[ ] Create a method to traverse tree, stopping if sum is found
"""

class TreeNode:
  """
  Define a tree node with a value and optional left and right nodes
  Read values and nodes
  """
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

  def get_value(self):
    return self.value  
  
  def get_left(self):
    return self.left
  
  def get_right(self):
    return self.right  
  

def add_nodes(node_one: TreeNode, node_two: TreeNode):
  return node_one.get_value() + node_two.get_value()


def tree_runner(k: int, tree_root: TreeNode):
  seen_node_values = []

  def check_sum(node):
    for seen_node in seen_node_values:
      if (k - node.get_value() == seen_node.get_value()):
        ans = [node, seen_node]
        return ans
    return []


  def add_value(node):
    ans =  []
    if (len(seen_node_values) > 0):
      ans = check_sum(node)
    seen_node_values.append(node)
    return ans

  def traverse(node):
    ans = add_value(node)
    if ans:
      return ans
    
    if node.left:
      ans = traverse(node.left)
      if ans:
        return ans
      
    if node.right:
      ans = traverse(node.right)
      if ans:
        return ans
    
    return ans

  return traverse(tree_root)
  






# run zone

node = TreeNode(10, TreeNode(5), TreeNode(9, TreeNode(12), TreeNode(15)))

print(tree_runner(20, node))
