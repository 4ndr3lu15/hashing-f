from curses.ascii import HT
import src.linked_list as linked_list
import time

class HTable:
    # classe que implementa a Hash Table
    def __init__(self, M:int = 42209):
        self.size = M                   # tamanho da tabela
        self.slots = []                 # cada slot é uma posição/hash
        for _ in range(self.size):
            self.slots.append(linked_list.LinkedList())
        self.meantime_get = [0, 0]          # atributo para calcular o tempo médio de busca
        self.meantime_put = 0               # atributo para calcular o tempo médio de cálculo de hash
        self.col_cont = 0                   # atributo para contar colisões

    def print_table(self): #TODO: RUSure = False
        # método responsável por imprimir a tabela completa
        for i in range(self.size):
            print('hash ' + str(i).zfill(len(str(self.size))) + ': ' + self.slots[i].printLL())

    def take_f(self, f):
        # método responsável por atribuir uma função de hash à Hash Table
        self.f_in_table = f

    def put(self, data):
        # método responsável por calcular o hash e inserir na Hash Table
        # esse método também calcula o tempo médio de cálculo do hash
        # boas praticas de uso do programa: usar esse método apenas uma vez para cada instância de uma HTable
        t = 0
        for item in data:
            t0 = time.time()
            hash = self.f_in_table(item[0], self.size)
            t1 = time.time() - t0
            t += t1
            if self.slots[hash].head != None:
                self.col_cont += 1
            self.slots[hash].insert(item)
        self.meantime_put = t / len(data)

    def get(self, item):
        # método responsável por buscar um item na tabela
        # esse método também calcula e atualiza o tempo médio de busca
        hash = self.f_in_table(item, self.size)
        t0 = time.time()
        x = self.slots[hash].strong_get(self.slots[hash].get(item)[1])
        y = self.slots[hash].get(item)
        t1 = time.time() - t0
        if self.meantime_get[1] == 0:
            self.meantime_get = [t1, 1]
        else:
            self.meantime_get[0] = ((self.meantime_get[0] * self.meantime_get[1]) + t1)/(self.meantime_get[1]+1)
            self.meantime_get[1] += 1
        print('y')
        print(y)
        print('x')
        print(x)
        return [item, y, x, hash]           # retorna o item, a posição na LinkedList,
                                            # as diferentes aparições do item
                                            # e o hash do item
