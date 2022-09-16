# ignore, file just to play with concepts

text = input("enter a string to convert into ascii values:")
ascii_values = []
for character in text:
    ascii_values.append(ord(character))
print(ascii_values)
print(str([1,1]))

# implementar função onde se passa uma lista de posições para uma lista encadeada e retorna os itens presentes
def strong_get(self, positions):
    itens = []
    for i in positions:
      current = self.head
      while current:
        for _ in range(i):
          current = current.next
      itens.append[current.data]
    return itens


x = HTable(M=3)
x.take_f(f3)

yay1 = 'abelha carro'.split()
yay2 = 'copo cadeira'.split()
yay3 = 'copo violão'.split() 
yay4 = 'copo tarde'.split()
yay5 = 'remédio água'.split()
x.put([yay1, yay2, yay3, yay4, yay5])

x.print_table()
print(type(x.f_in_table))
print(x.meantime_put)
print(x.col_cont)
print(x.get('copo'))