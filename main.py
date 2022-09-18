from base64 import b16decode
import src.table as table
import src.fun as fun

def assembly(x:int):
    if x == 1:
        return fun.f1
    elif x == 2:
        return fun.f2
    elif x == 3:
        return fun.f3
    elif x == 4:
        return fun.f4
    elif x == 5:
        return fun.f5
    

lexico = []
with open('data/lexico_v3.0.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    a = lines[i].split(',')
    a[3] = a[3][0]
    lexico.append(a)

H = table.HTable()

print('OLÁ, SELECIONE UM NUMERO DE 1 A 5 PARA A FUNÇÃO QUE SERÁ USADA')
x = int(input('Digite qual função será usada: '))
if x in [1,2,3,4,5]:
    b = True
    H.take_f(assembly(x))
    H.put(lexico)
else:
    print('POR FAVOR, DA PRÓXIMA VEZ SIGA AS INSTRUÇÕES!')
    b = False

while b:
    print('Escolha uma das opções:')
    print('[1] REALIZAR BUSCA')
    print('[2] EXIBIR TEMPO MÉDIO DE BUSCA')
    print('[3] EXIBIR QUANTAS BUSCAS JÁ FORAM FEITAS')
    print('[4] EXIBIR QUANTIDADE DE COLISÕES')
    print('[5] EXIBIR TEMPO MÉDIO DE CÁLCULO DE HASH')
    print('[6] IMPRIMIR TABELA COMPLEA (NÃO RECOMENDADO!)')
    print('[0] ENCERRAR PROGRAMA')
    kk = int(input('DIGITE UM NÚMERO DE 0 A 6: '))
    
    if kk == 1:
        hmm = input('DIGITE A PALAVRA A SER BUSCADA: ')
        y = H.get(hmm)
        print('o item {} tem hash {} e é encontrado nas posições {} de sua lista encadeada'.format(y[0], y[3], y[1][1]))
        print('o item em questão aparece como:')
        for i in y[2]:
            print(i)

    elif kk == 2:
        print('tempo médio de busca até agora: {time:.7f} segundos'.format(time = H.meantime_get[0]))

    elif kk == 3:
        print('número de buscas já realizadas: ' + str(H.meantime_get[1]))

    elif kk == 4:
        print('quantidade de colisões: ' + str(H.col_cont))

    elif kk == 5:
        print('tempo médio de cálculo de hash: {time:.7f} segundos'.format(time =H.meantime_put))
    
    elif kk == 6:
        H.print_table()
    else:
        print('FALOU, MANO!')
        b = not b