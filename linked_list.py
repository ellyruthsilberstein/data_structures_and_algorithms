class Node:
  """
  An object for stroing a single node of a linked list. 
  Models two attributes - data and the link to the next node in the list
  """
  
  data = None
  next_node = None
  
  def __init__(self, data):
    self.data = data
    
  def __repr(self):
    return "<Node data: %s>" % self.data
  
class LinkedList:
  """
  Singly linked list
  """
  
  def __init__(self):
    self.head = None
    
  def is_empty(self):
    return self.head == None
  
  def size(self):
    """
    Returns the number of nodes in the list
    Takes 0(n) time
    """
    
    current = self.head 
    count = 0 
    
    while current != None:
      count += 1
      current = current.next_node
      
    return count
    
  def add(self, data)
   """
   Adds new Node containing data at the head of list
   Takes O(1) time
   """
     new_node = Node(data)
     new_node.next_node = self.head
     self.head = new_node
   
  def search(self, key):
    """
    Search for the first node containing data that matches the key
    Returns node or None if not found 
    Takes O(n) times
    """
    current = self.head
    
    while current:
      if current.data == key:
        return current
      else:
        current = current.next_node
    return None
  
  def insert(self, data, index):
    """
    Inserts a new Node containing data at index position 
    Insetion takes O(1) time but finding the node at the insertion point takes O(n) time. 
    
    Takes an overall O(n) time
    """
    
    if index == 0:
      self.add(data)
      
    if index > 0:
      new = Node(data)
      
      position = index
      current = self.head
      
      while position > 1:
        current = node.next_node
        position -= 1
        
      prev_node = current
      next_node = current.next_node
      
      prev_node.next_node = new 
      new.next_node = next_node
  
  def __repr__(self):
  """
  Returns a string representation of the list.
  Takes O(n) time
  """

    nodes = []
    current = self.head

    while current:
      if current is self.head:
        nodes.append("[Head: %s]" % current.data)
      elif current.next_node is None:
        nodes.append("[Tail: %s]" % current.data)
      else:
        nodes.append("[%s]" % current.data)

      current = current.next_node

    return '-> '.join(nodes)
