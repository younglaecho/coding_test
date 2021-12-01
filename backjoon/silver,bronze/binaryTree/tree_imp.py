class Node:
  def __init__(self, data, left_node, right_node):
    self.data = data
    self.left_node = left_node
    self.right_node = right_node


n = int(input())
tree = {}
for i in range(n):
  data, left_node, right_node = input().split()
  tree[data] = Node(data, left_node, right_node)

print(tree['A'].data,tree['A'].left_node,tree['A'].right_node)