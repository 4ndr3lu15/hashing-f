from linked_list import Node
from linked_list import SLinkedList

class HTable:
    def __init__(self, size:int = 2000):
        for i in range(size):
            print(i)
        self.every = size

x = HTable()