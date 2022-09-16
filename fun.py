def funcao_reserva(text:str, size:int):
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))

    x = 0
    for i in range(len(ascii_values)):
        x += ascii_values[i]
    return x % (size)

def funcao_reserva2():
    #onhotencoding
    pass

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

def f5(text:str, size:int):
  final = 0
  for i in range(1,len(text)):
    final += (ord(text[i]) - ord(text[i-1]))**4
  return final%size



def zequinha():
    #uosar os 3 atributos de cada termo um encding no começo do hash
    #mas talvez isso não faça sentido pq a tabela tem um tamanho específico, isso aumentaria o tamanho da tabela, talvez
    pass