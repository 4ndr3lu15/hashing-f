# primeira função
def f1(text:str, size:int):
  final = 0
  for i in range(1,len(text)):
    if ord(text[i])%2 == 0:
        final *= ord(text[i]) ** ord(text[i])
    else:
        final += 1
        final *= ord(text[i])
  return final%size

# segunda função
def f2(text:str, size:int):
  p = 31
  final = 0
  for i in range(len(text)):
    final += (ord(text[i])*(p**i))%size

  return final % size

# terceira funcao
def f3(text:str, size:int):
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))

    x = 0
    for i in range(len(ascii_values)):
        x += ascii_values[i]
    return x % (size)

# quarta funcao
def f4(text:str, size:int):
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))

    x = 0
    for i in range(len(ascii_values)):
        x += ascii_values[i] ** 4
    return x % (size)

# quinta funcao
def f5(text:str, size:int):
  final = 0
  for i in range(1,len(text)):
    final += (ord(text[i]) - ord(text[i-1]))**4
  return final%size