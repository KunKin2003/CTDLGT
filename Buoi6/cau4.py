class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def prepend(self,value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    
  def append(self,value):
      new_node = Node(value)
      if self.head is None:
        self.head = new_node
        self.tail = new_node
      else:
        self.tail.next = new_node
        self.tail = new_node
      self.length += 1

  def __str__(self):
    temp_node = self.head
    result = ''
    while temp_node is not None:
      result += str(temp_node.value)
      if temp_node.next is not None:
        result += ' -> '
      temp_node = temp_node.next
    return result

  def getIndex(self,index):
    current = self.head
    for _ in range(index):
      current = current.next
    return current

  def deletedNode(self,index):
    if index > self.length or index <= 0:
      return None
    elif self.length == 1:
      temp = self.head
      self.head = None
      self.tail = None
      self.length = 0
      return temp
    else:
      pre_node = self.getIndex(index - 1)
      popped_node = pre_node.next
      pre_node.next = popped_node.next
      popped_node.next = None
      self.length -= 1
      return popped_node
    
new_linked_list = LinkedList()
new_linked_list.append(5)
new_linked_list.append(10)
new_linked_list.append(15)
new_linked_list.append(18)
print(new_linked_list.__str__())
new_linked_list.deletedNode(2)
print(new_linked_list.__str__())
      

