import pytest
from proj2 import * # <--- Change the name projectoFP to the file name with your project

# Github: @mc8mac
# 2023/2024
# ist1106082 - Marcos Machado

# Intersecao

class TestMarcosCriaIntersecao:

# A verificar: ==========================================
# Primeiro elemento tem de ser uma string               |
# Segundo elemento tem de ser um inteiro                |
# Primeiro elemento tem de ter len() == 1               |
# Primeiro elemento tem de ser uma letra entre A e S    |
# Segundo elemento tem de ser um inteiro maior que 1    |
# =======================================================
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao(1,1)
        assert str(excinfo.value) == "cria_intersecao: argumentos invalidos"
        
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao("AA",1)
        assert str(excinfo.value) == "cria_intersecao: argumentos invalidos"

    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao("a",1)
        assert str(excinfo.value) == "cria_intersecao: argumentos invalidos"

    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao("A","a")
        assert str(excinfo.value) == "cria_intersecao: argumentos invalidos"

    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao((),())
        assert str(excinfo.value) == "cria_intersecao: argumentos invalidos"

    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao(None,None)
        assert str(excinfo.value) == "cria_intersecao: argumentos invalidos"
    
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao("A",True)
        assert str(excinfo.value) == "cria_intersecao: argumentos invalidos"
    
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            cria_intersecao("A",float(1))
        assert str(excinfo.value) == "cria_intersecao: argumentos invalidos"

class TestMarcosObtemCL:
    def test_1(self):
        i1 = cria_intersecao("A",1)
        assert obtem_col(i1) == "A"

    def test_2(self):
        i1 = cria_intersecao("A",1)
        assert obtem_lin(i1) == 1

    def test_3(self):
        i1 = cria_intersecao("Z",99)
        assert obtem_col(i1) == "Z"

    def test_4(self):
        i1 = cria_intersecao("Z",99)
        assert obtem_lin(i1) == 99

class TestMarcosEhIntersecao:
    
    def test_1(self):
        i1 = 1
        assert not eh_intersecao(1)
    
    def test_2(self):
        i1 = "A1"
        assert not eh_intersecao(1)
    
    def test_3(self):
        i1 = ["A",2,3]
        assert not eh_intersecao(1)
        
    def test_4(self):
        i1 = [1,1]
        assert not eh_intersecao(1)
    
    def test_5(self):
        i1 = ["A","A"]
        assert not eh_intersecao(1)
    
    def test_6(self):
        i1 = ["AA",1]
        assert not eh_intersecao(1)

    def test_7(self):
        i1 = ["a",1]
        assert not eh_intersecao(1)

    def test_8(self):
        i1 = ["A",0]
        assert not eh_intersecao(1)
    
    def test_9(self):
        i1 = cria_intersecao("A",1)
        assert eh_intersecao(i1)

class TestMarcosIntersecoesIguais:
    def test_1(self):
        i1 = cria_intersecao("A",1)
        i2 = cria_intersecao("A",1)
        assert intersecoes_iguais(i1,i2)
    
    def test_2(self):
        i1 = cria_intersecao("A",1)
        i2 = cria_intersecao("B",1)
        assert not intersecoes_iguais(i1,i2)

    def test_3(self):
        i1 = cria_intersecao("A",1)
        i2 = cria_intersecao("A",2)
        assert not intersecoes_iguais(i1,i2)
    
    def test_4(self):
        i1 = cria_intersecao("A",1)
        i2 = cria_intersecao("B",2)
        assert not intersecoes_iguais(i1,i2)

class TestMarcosIntersecaoParaStr:
    def test_1(self):
        i1 = cria_intersecao("A",1)
        assert intersecao_para_str(i1) == "A1"

    def test_2(self):
        i1 = cria_intersecao("Z",99)
        assert intersecao_para_str(i1) == "Z99"
    
class TestMarcosStrParaIntersecao:
    def test_1(self):
        i1 = "A1"
        assert str_para_intersecao(i1) == cria_intersecao("A",1)
    
    def test_2(self):
        i1 = "Z99"
        assert str_para_intersecao(i1) == cria_intersecao("Z",99)

class TestMarcosObtemIntersecoesAdjacentes:
    def test_1(self): # Canto cima esquerdo
        i1 = cria_intersecao("A",1)
        i2 = cria_intersecao("S",19)
        answer = ["B1","A2"]
        assert obtem_intersecoes_adjacentes(i1,i2) == tuple(str_para_intersecao(x) for x in answer)

    def test_2(self): # Canto cima direito
        i1 = cria_intersecao("S",1)
        i2 = cria_intersecao("S",19)
        answer = ["R1","S2"]
        assert obtem_intersecoes_adjacentes(i1,i2) == tuple(str_para_intersecao(x) for x in answer)

    def test_3(self): # Canto baixo esquerdo
        i1 = cria_intersecao("A",19)
        i2 = cria_intersecao("S",19)
        answer = ["A18","B19"]
        assert obtem_intersecoes_adjacentes(i1,i2) == tuple(str_para_intersecao(x) for x in answer)
    
    def test_4(self): # Canto baixo direito
        i1 = cria_intersecao("S",19)
        i2 = cria_intersecao("S",19)
        answer = ["S18","R19"]
        assert obtem_intersecoes_adjacentes(i1,i2) == tuple(str_para_intersecao(x) for x in answer)
    
    def test_5(self): # Meio esquerdo
        i1 = cria_intersecao("A",2)
        i2 = cria_intersecao("S",19)
        answer = ["A1","B2","A3"]
        assert obtem_intersecoes_adjacentes(i1,i2) == tuple(str_para_intersecao(x) for x in answer)

    def test_6(self): # Meio direito
        i1 = cria_intersecao("S",2)
        i2 = cria_intersecao("S",19)
        answer = ["S1", "R2", "S3"]
        assert obtem_intersecoes_adjacentes(i1,i2) == tuple(str_para_intersecao(x) for x in answer)

    def test_7(self): # Meio baixo
        i1 = cria_intersecao("R",19)
        i2 = cria_intersecao("S",19)
        answer = ["R18","Q19","S19"]
        assert obtem_intersecoes_adjacentes(i1,i2) == tuple(str_para_intersecao(x) for x in answer)
    
    def test_8(self): # Meio Cima
        i1 = cria_intersecao("R",1)
        i2 = cria_intersecao("S",19)
        answer = ["Q1","S1","R2"]
        assert obtem_intersecoes_adjacentes(i1,i2) == tuple(str_para_intersecao(x) for x in answer)

    def test_9(self): # Todos
        i1 = cria_intersecao("B",2)
        i2 = cria_intersecao("S",19)
        answer = ["B1","A2","C2","B3"]
        assert obtem_intersecoes_adjacentes(i1,i2) == tuple(str_para_intersecao(x) for x in answer)
        
class TestMarcosOrdenaIntersecoes:
    def test_1(self): # Linhas
        i1 = ("A18","A10","A1","A2","A3","A4","A5","A6","A7","A8","A9")
        i1 = tuple(str_para_intersecao(x) for x in i1)
        answer = ("A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A18")
        assert ordena_intersecoes(i1) == tuple(str_para_intersecao(x) for x in answer)

    def test_2(self): # Colunas
        i1 = ("G1","A1","K1","B1","C1","E1","F1","H1","D1","I1","J1")
        i1 = tuple(str_para_intersecao(x) for x in i1)
        answer = ("A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","K1")
        assert ordena_intersecoes(i1) == tuple(str_para_intersecao(x) for x in answer)

    def test_3(self): # Linhas e Colunas
        i1 = ("G1","A1","K1","B1","C1","E1","F1","H1","D1","I1","J1","A18","A10","A1","A2","A3","A4","A5","A6","A7","A8","A9")
        i1 = tuple(str_para_intersecao(x) for x in i1)
        answer = ("A1","A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","K1","A2","A3", "A4","A5","A6","A7","A8","A9","A10","A18")
        assert ordena_intersecoes(i1) == tuple(str_para_intersecao(x) for x in answer)

# Pedra

# FUNCOES CHECKLIST ==============================================
# eh_pedra(arg)
# eh_pedra_branca(arg) | eh_pedra_preta(arg) | eh_pedra_vazia(arg)
# pedras_iguais(pedra1,pedra2)
# pedra_para_str(pedra)
# eh_pedra_jogador(pedra):
# eh_pedra_computador(pedra):
# ================================================================

class TestMarcosEhPedra:
    def test_1(self):
        assert eh_pedra(cria_pedra_branca())
    
    def test_2(self):
        assert eh_pedra(cria_pedra_neutra())
    
    def test_3(self):
        assert eh_pedra(cria_pedra_preta())
        
    def test_4(self):
        assert eh_pedra_preta((cria_pedra_preta()))
        
    def test_5(self):
        assert eh_pedra_branca((cria_pedra_branca()))
        
    def test_6(self):
        assert not eh_pedra_jogador((cria_pedra_neutra()))
        
    def test_7(self):
        assert eh_pedra_jogador((cria_pedra_preta()))
        
    def test_8(self):
        assert eh_pedra_jogador((cria_pedra_branca()))

class TestMarcosPedraParaStr:
    def test_1(self):
        assert pedra_para_str(cria_pedra_branca()) == "O"
    
    def test_2(self):
        assert pedra_para_str(cria_pedra_preta()) == "X"
    
    def test_3(self):
        assert pedra_para_str(cria_pedra_neutra()) == "."

class TestMarcosPedrasIguais:
    def test_1(self):
        assert pedras_iguais(cria_pedra_branca(),cria_pedra_branca())
    
    def test_2(self):
        assert pedras_iguais(cria_pedra_preta(),cria_pedra_preta())
    
    def test_3(self):
        assert pedras_iguais(cria_pedra_neutra(),cria_pedra_neutra())
    
    def test_4(self):
        assert not pedras_iguais(cria_pedra_branca(),cria_pedra_preta())
    
    def test_5(self):
        assert not pedras_iguais(cria_pedra_branca(),cria_pedra_neutra())
    
    def test_6(self):
        assert not pedras_iguais(cria_pedra_preta(),cria_pedra_neutra())
    
class TestMarcosCriaGoban:
    def test_1(self):
        ip = 'A'
        ib = ()
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9,ib,ip)
        assert str(excinfo.value) == "cria_goban: argumentos invalidos"

    def test_2(self):
        ip = ()
        ib = "A"
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9,ib,ip)
        assert str(excinfo.value) == "cria_goban: argumentos invalidos" 

    def test_3(self):
        ip = ()
        ib = ()
        with pytest.raises(ValueError) as excinfo:
            cria_goban(10,ib,ip)
        assert str(excinfo.value) == "cria_goban: argumentos invalidos"
        
    def test_4(self):
        ib = ("A2",)
        ip = ("A2",)
        ip = tuple(str_para_intersecao(x) for x in ip)
        ib = tuple(str_para_intersecao(x) for x in ib)
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9,ib,ip)
        assert str(excinfo.value) == "cria_goban: argumentos invalidos"

    def test_5(self):
        ib = ("A2",)
        ip = ("A2",)
        ip = tuple(str_para_intersecao(x) for x in ip)
        ib = tuple(str_para_intersecao(x) for x in ib)
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9,ib,ip)
        assert str(excinfo.value) == "cria_goban: argumentos invalidos"
        
    def test_6(self):
        ib = ("A3",)
        ip = ("A2", "A2")
        ip = tuple(str_para_intersecao(x) for x in ip)
        ib = tuple(str_para_intersecao(x) for x in ib)
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9,ib,ip)
        assert str(excinfo.value) == "cria_goban: argumentos invalidos"
    
    def test_7(self):
        ib = ("A2", "A2")
        ip = ("A3",)
        ip = tuple(str_para_intersecao(x) for x in ip)
        ib = tuple(str_para_intersecao(x) for x in ib)
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9,ib,ip)
        assert str(excinfo.value) == "cria_goban: argumentos invalidos"
    
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban_vazio(None)
        assert str(excinfo.value) == "cria_goban_vazio: argumento invalido"
    
    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban_vazio("A")
        assert str(excinfo.value) == "cria_goban_vazio: argumento invalido"
    
    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            cria_goban_vazio(3)
        assert str(excinfo.value) == "cria_goban_vazio: argumento invalido"

    def test_10(self):
        ib = ("A20",)
        ip = tuple()
        ib = tuple(str_para_intersecao(x) for x in ib)
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9,ib,ip)
        assert str(excinfo.value) == "cria_goban: argumentos invalidos"
    
    def test_11(self):
        ib = ("A2",)
        ip = ("A20",)
        ip = tuple(str_para_intersecao(x) for x in ip)
        ib = tuple(str_para_intersecao(x) for x in ib)
        with pytest.raises(ValueError) as excinfo:
            cria_goban(9,ib,ip)
        assert str(excinfo.value) == "cria_goban: argumentos invalidos"
    

class TestMarcosObtemPedra:
    def test_1(self):
        ib = ("A2",)
        ib = tuple(str_para_intersecao(x) for x in ib)
        g = cria_goban(9,ib,())
        assert eh_pedra_branca(obtem_pedra(g,cria_intersecao("A",2)))

    def test_2(self):
        ip = ("B9",)
        ip = tuple(str_para_intersecao(x) for x in ip)
        g = cria_goban(9,(),ip)
        assert eh_pedra_preta(obtem_pedra(g,cria_intersecao("B",9)))
    
    def test_3(self):
        ib = ("A2",)
        ib = tuple(str_para_intersecao(x) for x in ib)
        g = cria_goban(9,ib,())
        assert not eh_pedra_jogador(obtem_pedra(g,cria_intersecao("A",1)))

class TestMarcosObtemCadeia:
    def test_1(self):
        ib = ("A2","A3","A4")
        ib = tuple(str_para_intersecao(x) for x in ib)
        g = cria_goban(9,ib,())
        assert obtem_cadeia(g,cria_intersecao("A",4)) == ib

    def test_2(self):
        ip = ("A2","A3","A4")
        ip = tuple(str_para_intersecao(x) for x in ip)
        g = cria_goban(9,(),ip)
        assert obtem_cadeia(g,cria_intersecao("A",2)) == ip 

    def test_3(self):
        ip = ("A1","A2","A3","B3","B4","C4","D4","D3","D2","C2","C1","B1") 
        ip = tuple(str_para_intersecao(x) for x in ip)
        g = cria_goban(9,(),ip)
        answer = ("A1","B1","C1","A2","C2","D2","A3","B3","D3","B4","C4","D4")
        answer = tuple(str_para_intersecao(x) for x in answer)
        assert obtem_cadeia(g,cria_intersecao("C",4)) == answer
        
class TestMarcosnColocaPedra:
    def test_1(self):
        g = cria_goban_vazio(9)
        coloca_pedra(g,cria_intersecao("A",1),cria_pedra_branca())
        assert eh_pedra_branca(obtem_pedra(g,cria_intersecao("A",1)))

    def test_2(self):
        g = cria_goban_vazio(9)
        coloca_pedra(g,cria_intersecao("A",1),cria_pedra_preta())
        assert eh_pedra_preta(obtem_pedra(g,cria_intersecao("A",1)))

    def test_3(self):
        g = cria_goban_vazio(9)
        coloca_pedra(g,cria_intersecao("A",1),cria_pedra_preta())
        assert not eh_pedra_jogador(obtem_pedra(g,cria_intersecao("A",2)))

    def test_4(self):
        g = cria_goban_vazio(9)
        coloca_pedra(g,cria_intersecao("A",1),cria_pedra_branca())
        coloca_pedra(g,cria_intersecao("A",1),cria_pedra_preta())
        assert eh_pedra_preta(obtem_pedra(g,cria_intersecao("A",1)))

    def test_5(self):
        g = cria_goban_vazio(9)
        coloca_pedra(g,cria_intersecao("A",1),cria_pedra_branca())
        remove_pedra(g,cria_intersecao("A",1))
        assert not eh_pedra_jogador(obtem_pedra(g,cria_intersecao("A",1)))

    def test_6(self):
        ib = ("A1","A2","A3","B3","B4","C4","D4","D3","D2","C2","C1","B1")
        ib = tuple(str_para_intersecao(x) for x in ib)
        g = cria_goban(9,ib,())
        remove_cadeia(g,ib)
        answer = ()
        for i in ib:
            answer += (obtem_pedra(g,i) if eh_pedra_jogador(obtem_pedra(g,i))else ())
        assert answer == ()

class TestMarcosEhGoban:
    def test_1(self):
        assert eh_goban(cria_goban_vazio(9))

    def test_2(self):
        assert eh_goban(cria_goban_vazio(13))

    def test_3(self):
        assert eh_goban(cria_goban_vazio(19))

    def test_4(self):
        ib = ("A1","A2","A3","B3","B4","C4","D4","D3","D2","C2","C1","B1")
        ib = tuple(str_para_intersecao(x) for x in ib)
        g = cria_goban(9,ib,())
        assert eh_goban(g)

    def test_5(self):
        g = [["" for _ in range(9)] for _ in range(9)]
        assert not eh_goban(g)
    

class TestMarcosObtemUltimaIntersecao:
    def test_1(self):
        g = cria_goban_vazio(9)
        assert obtem_ultima_intersecao(g) == cria_intersecao("I",9)
    def test_1(self):
        g = cria_goban_vazio(13)
        assert obtem_ultima_intersecao(g) == cria_intersecao("M",13)
    def test_1(self):
        g = cria_goban_vazio(19)
        assert obtem_ultima_intersecao(g) == cria_intersecao("S",19)

class TestMarcosCopiaGobanGobansIguais:
    def test_1(self):
        g = cria_goban_vazio(9)
        assert gobans_iguais(g,cria_copia_goban(g))

    def test_2(self):
        g = cria_goban_vazio(9)
        g1 = cria_copia_goban(g)
        coloca_pedra(g,cria_intersecao("A",1),cria_pedra_branca())
        assert not gobans_iguais(g,g1)
    
    def test_3(self):
        g = cria_goban_vazio(9)
        g1 = cria_copia_goban(g)
        coloca_pedra(g,cria_intersecao("A",1),cria_pedra_branca())
        remove_pedra(g,cria_intersecao("A",1))
        assert gobans_iguais(g,g1)

class TestMarcosObtemTerritorios:
    def test_1(self):
        ib = ("B1","A2","B2","A4","B4","C4","D4","D3","D2","D1","F1","F2","F3","F4","F5","F6","E6","D6","C6","B6","A6","A8","B8","C8","D8","E8","F8","G8","H8","H7","H6","H5","H4","H3","H2","H1","I9","G7","E5","C3")
        ib = tuple(str_para_intersecao(x) for x in ib)
        g = cria_goban(9,ib,())
        answer = ((['A', 1],), (['A', 3], ['B', 3]), (['A', 5], ['B', 5], ['C', 5], ['D', 5]), (['A', 7], ['B', 7], ['C', 7], ['D', 7], ['E', 7], ['F', 7]), (['A', 9], ['B', 9], ['C', 9], ['D', 9], ['E', 9], ['F', 9], ['G', 9], ['H', 9]), (['C', 1], ['C', 2]), (['E', 1], ['E', 2], ['E', 3], ['E', 4]), (['G', 1], ['G', 2], ['G', 3], ['G', 4], ['G', 5], ['G', 6]), (['I', 1], ['I', 2], ['I', 3], ['I', 4], ['I', 5], ['I', 6], ['I', 7], ['I', 8]))
        assert obtem_territorios(g) == answer
    
    def test_2(self):
        g = cria_goban(9,(),())
        answer = ((['A', 1], ['B', 1], ['C', 1], ['D', 1], ['E', 1], ['F', 1], ['G', 1], ['H', 1], ['I', 1], ['A', 2], ['B', 2], ['C', 2], ['D', 2], ['E', 2], ['F', 2], ['G', 2], ['H', 2], ['I', 2], ['A', 3], ['B', 3], ['C', 3], ['D', 3], ['E', 3], ['F', 3], ['G', 3], ['H', 3], ['I', 3], ['A', 4], ['B', 4], ['C', 4], ['D', 4], ['E', 4], ['F', 4], ['G', 4], ['H', 4], ['I', 4], ['A', 5], ['B', 5], ['C', 5], ['D', 5], ['E', 5], ['F', 5], ['G', 5], ['H', 5], ['I', 5], ['A', 6], ['B', 6], ['C', 6], ['D', 6], ['E', 6], ['F', 6], ['G', 6], ['H', 6], ['I', 6], ['A', 7], ['B', 7], ['C', 7], ['D', 7], ['E', 7], ['F', 7], ['G', 7], ['H', 7], ['I', 7], ['A', 8], ['B', 8], ['C', 8], ['D', 8], ['E', 8], ['F', 8], ['G', 8], ['H', 8], ['I', 8], ['A', 9], ['B', 9], ['C', 9], ['D', 9], ['E', 9], ['F', 9], ['G', 9], ['H', 9], ['I', 9]),)
        assert obtem_territorios(g) == answer

class TestMarcosObtemAdjacentesDiferentes:
    def test_1(self):
        ib = ("B1","A2","B2","A4","B4","C4","D4","D3","D2","D1","F1","F2","F3","F4","F5","F6","E6","D6","C6","B6","A6","A8","B8","C8","D8","E8","F8","G8","H8","H7","H6","H5","H4","H3","H2","H1","I9","G7","E5","C3")
        ib = tuple(str_para_intersecao(x) for x in ib)
        g = cria_goban(9,ib,())
        cadeia = obtem_cadeia(g,cria_intersecao("F",1))
        answer = ('E1', 'G1', 'E2', 'G2', 'E3', 'G3', 'E4', 'G4', 'A5', 'B5', 'C5', 'D5', 'G5', 'G6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7')
        answer = tuple(str_para_intersecao(x) for x in answer)
        assert obtem_adjacentes_diferentes(g,cadeia) == answer
    
class TestMarcosJogada:
    def test_1(self):
        ib = "E2,E3,E4,E5".split(",")
        ib = tuple(str_para_intersecao(x) for x in ib)
        ip = "F1,F2,F3,F4,F5,E6,D5,D4,D3,D2,D1".split(",")
        ip = tuple(str_para_intersecao(x) for x in ip)
        g = cria_goban(9,ib,ip)
        p = cria_pedra_preta()
        _ = jogada(g,cria_intersecao("E",1),p)
        assert goban_para_str(g) == REF_TEST_JOGADA["1"]

    def test_2(self):
        ib = "C1,G1,C2,G2,C3,G3,A4,B4,C4,G4,H4,I4,A6,B6,C6,D6,E6,E7,F7,G7,H7,I7".split(",")
        ip = "D1,E1,F1,D2,E2,F2,D3,E3,F3,F4,D4,E4,A5,B5,C5,D5,F5,G5,H5,I5,I6,H6,G6,F6".split(",")
        ib = tuple(str_para_intersecao(i) for i in ib)
        ip = tuple(str_para_intersecao(i) for i in ip)
        g = cria_goban(9,ib,ip)
        _ = jogada(g,cria_intersecao('E',5),cria_pedra_branca())
        assert goban_para_str(g) == REF_TEST_JOGADA["2"]
    
    def test_3(self): 
        ib = "C1,G1,C2,G2,C3,G3,A4,B4,C4,G4,H4,I4,A6,B6,C6,D6,E6,E7,F7,G7,H7,I7".split(",")
        ip = "D1,F1,D2,E2,F2,D3,E3,F3,F4,D4,E4,A5,B5,C5,D5,F5,G5,H5,I5,I6,H6,G6,F6".split(",")
        ib = tuple(str_para_intersecao(i) for i in ib)
        ip = tuple(str_para_intersecao(i) for i in ip)
        g = cria_goban(9,ib,ip)
        _ = jogada(g,cria_intersecao('E',5),cria_pedra_branca())
        assert goban_para_str(g) == REF_TEST_JOGADA["3"]

class TestMarcosCalculaPontos:
    def test_1(self):
        g = cria_goban_vazio(9)
        assert calcula_pontos(g) == (0,0)

    def test_2(self):
        ib = "A1,I9".split(",")
        ib = tuple(str_para_intersecao(i) for i in ib)
        g = cria_goban(9,ib,())
        assert calcula_pontos(g) == (81,0)
    
    def test_3(self):
        ib = "A1,I9".split(",")
        ip = "A2,I8".split(",")
        ib = tuple(str_para_intersecao(i) for i in ib)
        ip = tuple(str_para_intersecao(i) for i in ip)
        g = cria_goban(9,ib,ip)d
        assert calcula_pontos(g) == (2,2)
# goban

# FUNCOES CHECKLIST ==============================================
# calcula_pontos(goban)
# eh_jogada_legal(goban,intersecao,pedra,l)
# turno_jogador(goban,pedra,l
# go(n,ib,ip)
# =================================================================

REF_TEST_JOGADA = {"1":
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . X . . . .  6
 5 . . . X . X . . .  5
 4 . . . X . X . . .  4
 3 . . . X . X . . .  3
 2 . . . X . X . . .  2
 1 . . . X X X . . .  1
   A B C D E F G H I"""
,"2":
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . O O O O O  7
 6 O O O O O . . . .  6
 5 . . . . O . . . .  5
 4 O O O . . . O O O  4
 3 . . O . . . O . .  3
 2 . . O . . . O . .  2
 1 . . O . . . O . .  1
   A B C D E F G H I"""
,"3":
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . O O O O O  7
 6 O O O O O X X X X  6
 5 X X X X O X X X X  5
 4 O O O X X X O O O  4
 3 . . O X X X O . .  3
 2 . . O X X X O . .  2
 1 . . O X . X O . .  1
   A B C D E F G H I"""}