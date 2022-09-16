import linked_list
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

    def print_table(self):
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
            hash = self.f_in_table(item, self.size)
            t1 = time.time() - t0
            t += t1
            if self.slots[hash].head != None:
                self.col_cont += 1
            self.slots[hash].insert(item)
        self.meantime_put = t / len(data)


    def get(self, item):
        # método responsável por buscar um item na tabela
        # esse método também calcula e atualiza o tempo médio de busca
        t0 = time.time()
        hash = self.f_in_table(item, self.size)
        x = self.slots[hash].get(item)
        t1 = time.time() - t0
        self.meantime_get[0] = ((self.meantime_get[0] * self.meantime_get[1]) + t1)/(self.meantime_get[0]+1)
        self.meantime_get[1] += 1
        return [item, x[1], hash]           # retorna o item, a posição na LinkedList e o hash do item
     
def f1(text:str, size:int):
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))

    x = 0
    for i in range(len(ascii_values)):
        x += ascii_values[i]
    return x % (size)

def f2(text:str, size:int):
  p = 31
  final = 0
  for i in range(len(text)):
    final += (ord(text[i])*(p**i))%size

  return final % size

def f3(text:str,size:int):
  #Criar dicionário com frequencias
  freq = dict()
  for character in text:
    freq[character] = freq.get(character,0) + 1

  #Calcular resultado final
  final = 0
  for k,v in freq.items():
    final += ord(k)*v

  return final%size

x = HTable(M=100)
x.take_f(f2)




yay = 'abelha carro ventuinha mochila copo cadeira computador celular guarda-roupa violão fim de tarde copo caixa desodorante remédio água nuvem árvore carro'.split()
x.put(yay)

x.print_table()
print(type(x.f_in_table))
print(x.meantime_put)
print(x.col_cont)

## buscando um termo na tabela
#print('o termo procurado tem hash ' + str(a[2]).zfill(len(str(x.size))) + ' e está na posição {} de tal hash'.format(a[1]))