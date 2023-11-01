GO = {9,13,19}
# Intersecao
def cria_intersecao(arg1,arg2):
    if type(arg1) != str or type(arg2) != int:
        raise ValueError('cria_intersecao: argumentos invalidos')
    if len(arg1) != 1:
        raise ValueError('cria_intersecao: argumentos invalidos')
    if not 'A' <= arg1 <= 'Z' or not 1 <= arg2:
        raise ValueError('cria_intersecao: argumentos invalidos')
    return [arg1,arg2]

def obtem_col(intersecao)->str:
    return intersecao[0]

def obtem_lin(intersecao)->int:
    return intersecao[1]

def eh_intersecao(arg)->bool:
    if type(arg) != list or len(arg) != 2:
        return False
    if type(arg[0]) != str or type(arg[1]) != int:
        return False
    if len(arg[0]) != 1:
        return False
    if not 'A' <= arg[0] <= 'Z' or not 1 <= arg[1]:
        return False
    return True
    
def intersecoes_iguais(intersecao1,intersecao2)->bool:
    return intersecao1 == intersecao2 and eh_intersecao(intersecao1) and eh_intersecao(intersecao2)

def intersecao_para_str(intersecao)->str:
    return obtem_col(intersecao) + str(obtem_lin(intersecao))

def str_para_intersecao(string):
    return cria_intersecao(string[0],int(string[1:]))

def obtem_intersecoes_adjacentes(intersecao,ultima)->tuple:
    maxLin, maxCol = obtem_lin(ultima), obtem_col(ultima)
    lin, col = obtem_lin(intersecao), obtem_col(intersecao)
    tup = ()
    if lin > 1: # Up
        tup += cria_intersecao(col, lin-1),
    if ord(col) > ord('A'): # Left
        tup += cria_intersecao(chr(ord(col)-1), lin),
    if ord(col) < ord(maxCol): # Right
        tup += cria_intersecao(chr(ord(col)+1), lin),
    if lin < maxLin: # Down
        tup += cria_intersecao(col, lin+1),
    return tup

def ordena_intersecoes(intersecoes):
    return tuple(sorted(intersecoes,key=lambda i: (obtem_lin(i),obtem_col(i))))
# Pedras

def cria_pedra_branca():
    return "O"

def cria_pedra_preta():
    return "X"

def cria_pedra_neutra():
    return "."

def eh_pedra(arg)->bool:
    return arg == cria_pedra_branca() or arg == cria_pedra_preta() or arg == cria_pedra_neutra()

def eh_pedra_branca(arg)->bool:
    return arg == cria_pedra_branca()

def eh_pedra_preta(arg)->bool:
    return arg == cria_pedra_preta()

def pedras_iguais(pedra1,pedra2)->bool:
    return pedra1 == pedra2

def pedra_para_str(pedra)->str:
    switch = {
        cria_pedra_branca(): "O",
        cria_pedra_preta(): "X",
        cria_pedra_neutra(): "."
    }
    return switch.get(pedra,"?")

def eh_pedra_jogador(pedra):
    return eh_pedra_branca(pedra) or eh_pedra_preta(pedra)

# Goban
def cria_goban_vazio(n)->list:
    if type(n) != int or n not in GO:
        raise ValueError('cria_goban_vazio: argumento invalido')
    return [[cria_pedra_neutra() for _ in range(n)] for _ in range(n)]

def cria_goban(n,ib,ip):
    if type(n) != int or n not in GO or type(ib) != tuple or type(ip) != tuple:
        raise ValueError('cria_goban: argumentos invalidos')
    goban = cria_goban_vazio(n)
    for i in ib:
        if not eh_intersecao_valida(goban,i) or i in ip or ib.count(i) != 1:
            raise ValueError('cria_goban: argumentos invalidos')
    for i in ip:
        if not eh_intersecao_valida(goban,i) or ip.count(i) != 1:
            raise ValueError('cria_goban: argumentos invalidos')
    for i in ib:
        coloca_pedra(goban,i,cria_pedra_branca())
    for i in ip:
        coloca_pedra(goban,i,cria_pedra_preta())
    return goban

def cria_copia_goban(goban):
    return [[l for l in c]for c in goban]

def obtem_ultima_intersecao(goban)->tuple:
    n = len(goban)
    return cria_intersecao(chr(ord('A')+n-1),n)

def obtem_pedra(goban,intersecao):
    return goban[ord(obtem_col(intersecao))-ord('A')][obtem_lin(intersecao)-1]

def obtem_cadeia(goban,intersecao):
    ultima = obtem_ultima_intersecao(goban)
    state = obtem_pedra(goban,intersecao)
    queue = [intersecao]
    cadeia = []
    while queue:
        intersecao = queue.pop()
        cadeia.append(intersecao)
        for i in obtem_intersecoes_adjacentes(intersecao,ultima):
            if obtem_pedra(goban,i) == state and i not in cadeia and i not in queue:
                queue.append(i)
    return ordena_intersecoes(cadeia)

def coloca_pedra(goban, intersecao, pedra):
    goban[ord(obtem_col(intersecao))-ord('A')][obtem_lin(intersecao)-1] = pedra
    return goban

def remove_pedra(goban, intersecao):
    return coloca_pedra(goban,intersecao,cria_pedra_neutra())
    

def remove_cadeia(goban, intersecoes):
    for i in intersecoes:
        remove_pedra(goban,i)
    return goban

def eh_goban(goban):
    n = len(goban)
    testeCase = cria_goban_vazio(n)
    if type(goban) != type(testeCase) or len(goban) not in GO:
        return False
    for i in goban:
        if type(i) != type(testeCase[0]) or len(i) != len(goban):
            return False
        for j in i:
            if not eh_pedra(j):
                return False
    return True

def eh_intersecao_valida(goban,intersecao):
    if not eh_intersecao(intersecao):
        return False
    ultima = obtem_ultima_intersecao(goban)
    return obtem_col(intersecao) <= obtem_col(ultima) and obtem_lin(intersecao) <= obtem_lin(ultima)

def gobans_iguais(goban1,goban2):
    return goban1 == goban2

def goban_para_str(goban):
    size = len(goban)
    s = '  '
    s += ''.join(f' {chr(ord("A") + i)}' for i in range(size)) + '\n'
    for j in reversed(range(size)):
        s += f'{str(j+1) if j+1 > 9 else " "+str(j+1)} '
        s += ' '.join((obtem_pedra(goban, cria_intersecao(chr(ord('A') + i),j+1))) for i in range(size))
        s += f' {j+1}\n' if j+1 > 9 else f'  {j+1}\n'
    s += '  '
    s += ''.join(f' {chr(ord("A") + i)}' for i in range(size))
    return s

def obtem_territorios(goban)->tuple:
    territorio = []
    side = len(goban)
    for i in range(side):
        for j in range(side):
            intersecao = cria_intersecao(chr(ord('A')+i),j+1)
            state = 1
            for k in territorio:
                if intersecao in k:
                    state = 0
                    break
            if state:
                if not eh_pedra_jogador(obtem_pedra(goban,intersecao)):
                    territorio.append(obtem_cadeia(goban,intersecao))
    return ordena_territorios(tuple(territorio))

def ordena_territorios(territorios):
    return tuple(sorted(territorios,key=lambda x: (obtem_lin(x[0]),obtem_col(x[0]))))

def obtem_adjacentes_diferentes(goban,intersecoes):
    ultima = obtem_ultima_intersecao(goban)
    state = eh_pedra_jogador(obtem_pedra(goban,intersecoes[0]))
    adjacentes = []
    for i in intersecoes:
        for j in obtem_intersecoes_adjacentes(i,ultima):
            if obtem_pedra(goban,j) != state and eh_pedra_jogador(obtem_pedra(goban,j)) != state and j not in adjacentes:
                adjacentes.append(j)
    return ordena_intersecoes(adjacentes)

def jogada(goban,intersecao,pedra):
    coloca_pedra(goban,intersecao,pedra)
    player = eh_pedra_branca(pedra)
    ultima = obtem_ultima_intersecao(goban)

    for i in obtem_intersecoes_adjacentes(intersecao,ultima):
        p = obtem_pedra(goban,i)
        if eh_pedra_branca(p) != player and eh_pedra_jogador(p):
            if not tem_liberdade(goban,i):
                remove_cadeia(goban,obtem_cadeia(goban,i))
    return goban
 
def obtem_pedras_jogadores(goban):
    ultima = obtem_ultima_intersecao(goban)
    b = 0
    p = 0
    for i in range(ord('A'),ord(obtem_col(ultima))+1):
        for j in range(1,obtem_lin(ultima)+1):
            intersecao = cria_intersecao(chr(i),j)
            if eh_pedra_branca(obtem_pedra(goban,intersecao)):
                b += 1
            if eh_pedra_preta(obtem_pedra(goban,intersecao)):
                p += 1
    return (b,p)

def calcula_pontos(goban):
    pedras = obtem_pedras_jogadores(goban)
    if pedras[0] == 0 and pedras[1] == 0:
        return (0,0)
    b = pedras[0]
    p = pedras[1]
    for i in obtem_territorios(goban):
        if all(eh_pedra_branca(obtem_pedra(goban,j)) for j in obtem_adjacentes_diferentes(goban,i)):
            b += len(i)
        elif all(eh_pedra_preta(obtem_pedra(goban,j)) for j in obtem_adjacentes_diferentes(goban,i)):
            p += len(i)
    return (b,p)

def tem_liberdade(goban,intersecao):
    c = obtem_cadeia(goban,intersecao)
    if any(not eh_pedra_jogador(obtem_pedra(goban,j)) for j in obtem_adjacentes_diferentes(goban,c)):
        return True
    return False

def eh_jogada_legal(goban, intersecao, pedra, l):
    copy = cria_copia_goban(goban)
    if not eh_intersecao_valida(goban,intersecao):
        return False
    if eh_pedra_jogador(obtem_pedra(goban,intersecao)):
        return False
    jogada(copy,intersecao,pedra)
    if not tem_liberdade(copy,intersecao):
        return False
    if gobans_iguais(copy,l):
        return False
    return True

def turno_jogador(goban,pedra,l):
    while 1:
        try:
            userInput = input(f"Escreva uma intersecao ou 'P' para passar [{pedra_para_str(pedra)}]:")
            if userInput == 'P':
                return False
            intersecao = str_para_intersecao(userInput)
            if eh_jogada_legal(goban,intersecao,pedra,l):
                jogada(goban,intersecao,pedra)
                return True
            else:
                continue
        except:
            continue

def go(n,tb,tn):
    b = True
    p = True
    if not tb and not tn:
        goban = cria_goban_vazio(n)
    else:
        goban = cria_goban(n,tb,tn)
    
    while 1:
        prev = cria_copia_goban(goban)
        score = calcula_pontos(goban)
        print(f'Branco (O) tem {score[0]} pontos')
        print(f'Preto (X) tem {score[1]} pontos')
        print(goban_para_str(goban))
        p = turno_jogador(goban,cria_pedra_preta(),prev)
        if not p and not b:
            break
        prev = cria_copia_goban(goban)
        score = calcula_pontos(goban)
        print(f'Branco (O) tem {score[0]} pontos')
        print(f'Preto (X) tem {score[1]} pontos')
        print(goban_para_str(goban))
        b = turno_jogador(goban,cria_pedra_branca(),prev)
        if not p and not b:
            break
        continue
    print(f'Branco (O) tem {score[0]} pontos')
    print(f'Preto (X) tem {score[1]} pontos')
    print(goban_para_str(goban))
    score = calcula_pontos(goban)
    return score[0] > score[1]

ip = ("B1","A2","B2","A4","B4","C4","D4","D3","D2","D1","F1")
ib = ("F2","F3","F4","F5","F6","E6","D6","C6","B6","A6","A8","B8","C8","D8","E8","F8","G8","H8","H7","H6","H5","H4","H3","H2","H1","I9","G7","E5","C3")
ip = tuple(str_para_intersecao(x) for x in ip)
ib = tuple(str_para_intersecao(x) for x in ib)
g = cria_goban(9,ib,ip)
answer = obtem_territorios(g)
answer = tuple(tuple(intersecao_para_str(j) for j in i) for i in answer)
print(answer)