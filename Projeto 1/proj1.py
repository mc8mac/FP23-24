def eh_territorio(t):
    if not isinstance(t,tuple):
        return False
    if not 1<=len(t)<=26:
        return False 
    for i in t:
        if not isinstance(i, tuple):
            return False
        for j in i:
            if type(j) != int:
                return False
            if not j in {0,1}:
                return False
    lenght = len(t[0])
    if not 1<=lenght<=99:
        return False
    for i in t:
        if not len(i) == lenght:
            return False
    return True

def obtem_ultima_intersecao(field):
    h = len(field[0])
    v = len(field) - 1
    return (chr(ord('A') + v), h)

def eh_intersecao(inter):
    if not isinstance(inter,tuple):
        return False
    if not len(inter) == 2:
        return False
    if type(inter[0]) != str:
        return False
    if type(inter[1]) != int:
        return False
    if not 1<=inter[1]<=99:
        return False
    if not 'A'<=inter[0]<='Z':
        return False
    if not len(inter[0]) == 1:
        return False
    return True

def eh_intersecao_valida(field,inter):
    inter1 = obtem_ultima_intersecao(field)
    if not eh_territorio(field):
        return False
    if inter[0] > inter1[0] or inter[1] > inter1[1]:
        return False
    return True

def eh_intersecao_livre(field,inter):
    return field[ord(inter[0])-ord('A')][inter[1]-1] == 0

def obtem_intersecoes_adjacentes(field, inter):
    if not eh_intersecao_valida(field,inter):
        return ()
    if not eh_territorio(field):
        return ()
    
    h = len(field[0])
    v = len(field)
    i = ord(inter[0])-ord('A')
    j = inter[1]-1
    tup = ()

    if j-1 >= 0:
        tup = tup + ((chr(ord('A') + i), j),)
    if i-1 >= 0:
        tup = tup + ((chr(ord('A') + i - 1), j+1),)
    if i+1 < v:
        tup = tup + ((chr(ord('A') + i + 1), j+1),)
    if j+1 < h:
        tup = tup + ((chr(ord('A') + i), j+2),)
    return tup

def ordena_intersecoes(tup):
    return tuple(sorted(tup, key= lambda x: (x[1], x[0])))


def territorio_para_str(field):
    if not eh_territorio(field):
        raise ValueError("territorio_para_str: argumento invalido")
    rows, cols = len(field), len(field[0])
    s = '  '
    s += ''.join(f' {chr(ord("A") + i)}' for i in range(rows)) + '\n'
    for j in range(cols-1, -1, -1):

        if j+1 > 9:
            s += f'{j+1} '
        else: s +=  f' {j+1} '

        s += ' '.join('.X'[field[i][j]] for i in range(rows))
        s += f' {j+1}\n' if j+1 > 9 else f'  {j+1}\n'
    s += '  '
    s += ''.join(f' {chr(ord("A") + i)}' for i in range(rows))
    return s

def obtem_cadeia(field, inter):
    if not eh_territorio(field):
        raise ValueError("obtem_cadeia: argumentos invalidos")
    if not eh_intersecao(inter):
        raise ValueError("obtem_cadeia: argumentos invalidos")
    if not eh_intersecao_valida(field, inter):
        raise ValueError("obtem_cadeia: argumentos invalidos")
    state = eh_intersecao_livre(field, inter)
    connected = []
    queue = [inter]

    while queue:
        current = queue.pop(0)
        if current not in connected:
            connected.append(current)
            adjacent = obtem_intersecoes_adjacentes(field, current)
            for adj in adjacent:
                if eh_intersecao_valida(field, adj) and eh_intersecao_livre(field, adj) == state and adj not in queue:
                    queue.append(adj)
    connected = tuple(connected)
    return ordena_intersecoes(connected)


def obtem_vale(field, inter):
    if not eh_territorio(field):
        raise ValueError("obtem_vale: argumentos invalidos")
    if not eh_intersecao(inter):
        raise ValueError("obtem_vale: argumentos invalidos")
    if not eh_intersecao_valida(field, inter):
        raise ValueError("obtem_vale: argumentos invalidos")
    if eh_intersecao_livre(field, inter):
        raise ValueError("obtem_vale: argumentos invalidos")
    
    chain = obtem_cadeia(field, inter)
    connected = []

    for i in chain:
        tup = obtem_intersecoes_adjacentes(field, i)
        for j in tup:
            if eh_intersecao_livre(field, j) & (j not in connected):
                connected.append(j)
    connected = tuple(connected)

    return ordena_intersecoes(connected)
 

def verifica_conexao(field, inter1, inter2):

    if not eh_territorio(field):
        raise ValueError("verifica_conexao: argumentos invalidos")
    if not eh_intersecao(inter1):
        raise ValueError("verifica_conexao: argumentos invalidos")
    if not eh_intersecao(inter2):
        raise ValueError("verifica_conexao: argumentos invalidos")
    if not eh_intersecao_valida(field, inter1):
        raise ValueError("verifica_conexao: argumentos invalidos")
    if not eh_intersecao_valida(field, inter2):
        raise ValueError("verifica_conexao: argumentos invalidos")

    chain = obtem_cadeia(field, inter1)
    if inter2 in chain:
        return True
    return False

def calcula_numero_montanhas(field):
    if not eh_territorio(field):
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    count = 0
    for i in field:
        for j in i:
            if j == 1:
                count += 1
    return count

def calcula_numero_cadeias_montanhas(field):
    if not eh_territorio(field):
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")
    count = 0
    chain = []
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 1 & ((chr(ord('A') + i), j+1) not in chain):
                temp = obtem_cadeia(field, (chr(ord('A') + i), j+1))
                if temp not in chain:
                    chain.append(temp)
                    count += 1
                    
    return count

def calcula_tamanho_vales(field):
    if not eh_territorio(field):
        raise ValueError("calcula_tamanho_vales: argumento invalido")
    chain = []
    
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 1:
                temp = obtem_vale(field, (chr(ord('A') + i), j+1))
                for k in temp:
                    if k not in chain:
                        chain.append(k)
    
    return len(chain)    