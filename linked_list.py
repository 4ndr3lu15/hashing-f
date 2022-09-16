# ignore, file just to play with concepts

# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    foo = ''
    current = self.head
    while(current):
      foo = foo + str(current.data) + ' -> '
      current = current.next
    return foo[0:-4] #estamos retornando uma string

  def get(self, item):
    current = self.head
    x = 0
    while(current):
      if current.data == item:
        return [item, 'posição '+ str(x) +' da lista']
      current = current.next
      x += 1
    return [item, 'item não encontrado']

# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
print(LL.printLL())
print(LL.get(5))