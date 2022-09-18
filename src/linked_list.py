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
    position = 0
    positions = []
    while current:
      if current.data[0] == item:
        # adiciona as posições na lista onde o item é encontrado
        positions.append(position)
      current = current.next
      position += 1
    return [item, positions] # item e posições da tabela onde o item está

  def strong_get(self, pos):
    itens = []
    current = self.head
    count = 0
    for i in pos:
      while count < i:
        count += 1
        current = current.next
      itens.append(current.data)
    return itens