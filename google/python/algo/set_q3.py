
#l = list()
#print l
#t = (l,l) 
#print t
#l.append(1)
#print l
#print t

class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
  def insert(self, data):
    if data < self.data:
      if self.left is None:
        self.left = Node(data)
      else:
        self.left.insert(data)
    else:
      if self.right is None:
        self.right = Node(data)
      else:
        self.right.insert(data)

def main():
  root = Node(8)
  print root.left, root.right, root.data
  root.insert(3)
  root.insert(10)
  root.insert(1)
  print root.left.left, root.right.right
  
if __name__ == '__main__':
  main()
