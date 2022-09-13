import linked_list

class HTable:
    def __init__(self, size:int = 15):
        self.size = size
        self.body = []
        for i in range(self.size):
            self.body.append(linked_list.LinkedList())

    def print_table(self):
        #todo: deixar bonitinho tipo 00001, 00002, etc
        for i in range(self.size):
            print('hash ' +str(i)+':'+ self.body[i].printLL())


    def apply_f(self, function, data):
        hash = function(data, self.size)
        self.body[hash].insert(data)

    def search(self, term):
        pass
        
def f1(text:str, size:int):
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))

    x = 0
    for i in ascii_values:
        if i % 2 == 0:
            x = x + i
        else:
            x = x*i
    return x % size

x = HTable()

for i in range(100):
    x.apply_f(f1, str(i))

x.print_table()
print(f1('lagarticha', 100))