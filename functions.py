import table

lexico = {0: 'aaa', 1: 'aab', 2:'aac', 3:'aad', 4:'dasda'}

print(len(lexico))

def f0(text:str, size:int):
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


def f1(lexico):
    x = table.HTable(size=len(lexico))

def f2():
    #usar os 3 atributos de cada termo um encoding no começo do hash
    #mas talvez isso não faça sentido pq a tabela tem um tamanho específico, isso aumentaria o tamanho da tabela, talvez
    pass


x = table.HTable()

for i in range(100):
    x.apply_f(functions.f0, str(i))

x.print_table()