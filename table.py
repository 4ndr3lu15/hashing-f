import linked_list
import time

class HTable:
    # classe que implementa a Hash Table
    def __init__(self, M:int = 42209):
        self.size = M                   # tamanho da tabela
        self.slots = []                 # cada slot é uma posição/hash
        for _ in range(self.size):
            self.slots.append(linked_list.LinkedList())
        self.meantime = [0, 0]          # atributo para calcular o tempo médio de busca

    def print_table(self):
        # método responsável por imprimir a tabela completa
        #todo: deixar bonitinho tipo 00001, 00002, etc
        for i in range(self.size):
            print('hash ' + str(i) + ': ' + self.slots[i].printLL())

    def take_f(self, f):
        # método responsável por atribuir uma função de hash à Hash Table
        self.f_in_table = f

    def put(self, data):
        # método responsável por calcular o hash e inserir na Hash Table
        for item in data:
            hash = self.f_in_table(item, self.size)
            self.slots[hash].insert(item)

    def get(self, item):
        # método responsável por buscar um item na tabela
        # esse método também calcula e atualiza o tempo médio de busca
        t0 = time.time()
        hash = self.f_in_table(item, self.size)
        x = self.slots[hash].get(item)
        t1 = time.time() - t0
        self.meantime[0] = ((self.meantime[0] * self.meantime[1]) + t1)/(self.meantime[0]+1)
        self.meantime[1] += 1
        return [item, x[1], hash]
     
def f1(text:str, size:int):
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))

    x = 0
    for i in ascii_values:
        x += 1
    return x % (size)

x = HTable()
x.take_f(f1)

yay = 'irra pai vamo que vamo que vamo nessa porra caralho 2 3 4 5 6 7'.split()
x.put(yay)

x.print_table()
print(type(x.f_in_table))
print(x.slots[0])