import pytest 
import projName as fp # <--- Change the name projName to the file name with your project

# Testes públicos extra para o projeto 1 de FP (2023-2024)
# by Marcos Machado
# Git: @mc8mac


class TestEhTerritorio:

    def test_1(self):
        t = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert fp.eh_territorio(t)
    
    def test_2(self):
        t = ((0,1,0,0),(0,0,0,0),(0,0,2,0),(1,0,0,0),(0,0,0,0))
        assert not fp.eh_territorio(t)

    def test_3(self):
        t = ((0,1,0,0),(0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert not fp.eh_territorio(t)
    
    def test_4(self):
        t = ((0,1,0,0),(0,0,0,"A"),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert not fp.eh_territorio(t)

    def test_5(self):
        t = ((0,1,0,0),[0,0,0,0],(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert not fp.eh_territorio(t)

    def test_6(self): 
        t = (1,0,1,0)
        assert not fp.eh_territorio(t)

    def test_7(self):
        t = ()
        assert not fp.eh_territorio(t)

    def test_8(self):
        t = ((1,),)
        assert fp.eh_territorio(t)
    
    def test_9(self):
        t = tuple(tuple(1 for _ in range(99)) for _ in range(26))
        assert fp.eh_territorio(t)

    def test_10(self):
        t = tuple(tuple(1 for _ in range(100)) for _ in range(26))
        assert not fp.eh_territorio(t)

    def test_11(self): # Large territory
        t = tuple(tuple(1 for _ in range(99)) for _ in range(27))
        assert not fp.eh_territorio(t)

    def test12(self):
        t = ((1,1.0),),
        assert not fp.eh_territorio(t)

    def test13(self):
        t = ((True,True),),
        assert not fp.eh_territorio(t)
    
class TestObtemUltimaIntersecao:

    def test_1(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert fp.obtem_ultima_intersecao(t) == ('C', 3)

    def test_2(self):
        t = ((0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 0))
        assert fp.obtem_ultima_intersecao(t) == ('C', 4)

    def test_3(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0), (0, 0, 0))
        assert fp.obtem_ultima_intersecao(t) == ('D', 3)

    def test_4(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 1), (0, 0, 0))
        assert fp.obtem_ultima_intersecao(t) == ('G', 3)

    def test_5(self):
        t = ((0, 0), (0, 1), (0, 0), (0, 0), (0, 0))
        assert fp.obtem_ultima_intersecao(t) == ('E', 2)

    def test_6(self):    
        grid = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert fp.obtem_ultima_intersecao(grid) == ('E', 4)

    def test_7(self):    
        grid = ((0,1,0,0,0),(0,0,0,0,1),(0,0,1,0,1))
        assert fp.obtem_ultima_intersecao(grid) == ('C', 5)

class TestEhIntersecao:

    def test_1(self):
        assert fp.eh_intersecao(('A', 1))

    def test_4(self):
        assert fp.eh_intersecao(('Z', 99))

    def test_5(self):
        assert not fp.eh_intersecao(('AA', 1))

    def test_6(self):
        assert not fp.eh_intersecao(('A', 0))

    def test_7(self):
        assert not fp.eh_intersecao(('A', 100))
    
    def test_8(self):
        assert not fp.eh_intersecao(('A', 'A'))

    def test_9(self):
        assert not fp.eh_intersecao((1, 1))
    
    def test_10(self):
        assert not fp.eh_intersecao((1, 'A'))
    
    def test_11(self):
        assert not fp.eh_intersecao((1.0, 'A'))
    
    def test_12(self):
        assert not fp.eh_intersecao([1, 'A'])

    def test_13(self):
        assert not fp.eh_intersecao((1, 'A', 1))

    def test_14(self):
        assert not fp.eh_intersecao((1,))

class TestEhIntersecaoValida:

    def test_1(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert fp.eh_intersecao_valida(t, ('C', 3))
    
    def test_2(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert not fp.eh_intersecao_valida(t, ('D', 3))

    def test_3(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert not fp.eh_intersecao_valida(t, ('C', 4))

    def test_4(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert not fp.eh_intersecao_valida(t, ('D', 4))

    def test_5(self):
        t = ((1,),)
        assert fp.eh_intersecao_valida(t, ('A', 1))

    def test_6(self):
        t = tuple(tuple(1 for _ in range(99)) for _ in range(26))
        assert fp.eh_intersecao_valida(t, ('Z', 99))

class TestEhIntersecaoLivre:

    def test_1(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert fp.eh_intersecao_livre(t, ('C', 3))

    def test_2(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert not fp.eh_intersecao_livre(t, ('B', 2))
    
    

class TestObtemIntersecoesAdjacentes:

    def test_1(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert fp.obtem_intersecoes_adjacentes(t, ('B', 2)) == (('B', 1), ('A', 2), ('C', 2), ('B', 3))
    
    def test_2(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert fp.obtem_intersecoes_adjacentes(t, ('C', 3)) == (('C', 2), ('B', 3))

    def test_3(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert fp.obtem_intersecoes_adjacentes(t, ('A', 1)) == (('B', 1), ('A', 2))

    def test_4(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert fp.obtem_intersecoes_adjacentes(t, ('A', 3)) == (('A', 2), ('B', 3))

    def test_5(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert fp.obtem_intersecoes_adjacentes(t, ('C', 1)) == (('B', 1),('C', 2))

    def test_6(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        assert fp.obtem_intersecoes_adjacentes(t, ('C', 2)) == (('C', 1), ('B', 2), ('C', 3))

    def test_7(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 1))
        assert fp.obtem_intersecoes_adjacentes(t, ('B', 3)) == (('B', 2), ('A', 3), ('C', 3))

    def test_8(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 1))
        assert fp.obtem_intersecoes_adjacentes(t, ('B', 1)) == (('A', 1),('C', 1), ('B', 2))

    def test_9(self):
        t = ((0, 0, 0), (0, 1, 0), (0, 0, 1))
        assert fp.obtem_intersecoes_adjacentes(t, ('A', 2)) == (('A', 1), ('B', 2), ('A', 3))

class TestOrdenaIntersecoes:

    def test_1(self):
        tup = (('A',1), ('A',2), ('A',3), ('B',1), ('B',2), ('B',3) )
        assert fp.ordena_intersecoes(tup) == (('A',1), ('B',1), ('A',2), ('B',2), ('A',3), ('B',3) )

    def test_2(self):
        tup = (('A',1), ('A',2), ('A',3), ('B',1), ('B',2), ('B',3), ('C',1), ('C',2), ('C',3) )
        assert fp.ordena_intersecoes(tup) == (('A',1), ('B',1), ('C',1), ('A',2), ('B',2), ('C',2), ('A',3), ('B',3), ('C',3) )

    def test_3(self):
        tup = (('A',1),)
        assert fp.ordena_intersecoes(tup) == (('A',1),)

    def test_4(self):
        tup = ()
        assert fp.ordena_intersecoes(tup) == ()

class TestTerritorioParaStr:

    def test_1(self):
        t = ((0,1,0,0),(0,0,0,0))
        assert fp.territorio_para_str(t) == '   A B\n 4 . .  4\n 3 . .  3\n 2 X .  2\n 1 . .  1\n   A B'
    
    def test_2(self):
        t = t=((1,1,1,0,0,0,0,0,1,1),)
        assert fp.territorio_para_str(t) == '   A\n10 X 10\n 9 X  9\n 8 .  8\n 7 .  7\n 6 .  6\n 5 .  5\n 4 .  4\n 3 X  3\n 2 X  2\n 1 X  1\n   A'
     
    def test_3(self):
        t = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert fp.territorio_para_str(t) == '   A B C D E\n 4 . . . . .  4\n 3 . . X . .  3\n 2 X . . . .  2\n 1 . . . X .  1\n   A B C D E'
    
    def test_4(self):
        str1 = '   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z\n99 X X X X X X X X X X X X X X X X X X X X X X X X X X 99\n98 X X X X X X X X X X X X X X X X X X X X X X X X X X 98\n97 X X X X X X X X X X X X X X X X X X X X X X X X X X 97\n96 X X X X X X X X X X X X X X X X X X X X X X X X X X 96\n95 X X X X X X X X X X X X X X X X X X X X X X X X X X 95\n94 X X X X X X X X X X X X X X X X X X X X X X X X X X 94\n93 X X X X X X X X X X X X X X X X X X X X X X X X X X 93\n92 X X X X X X X X X X X X X X X X X X X X X X X X X X 92\n91 X X X X X X X X X X X X X X X X X X X X X X X X X X 91\n90 X X X X X X X X X X X X X X X X X X X X X X X X X X 90\n89 X X X X X X X X X X X X X X X X X X X X X X X X X X 89\n88 X X X X X X X X X X X X X X X X X X X X X X X X X X 88\n87 X X X X X X X X X X X X X X X X X X X X X X X X X X 87\n86 X X X X X X X X X X X X X X X X X X X X X X X X X X 86\n85 X X X X X X X X X X X X X X X X X X X X X X X X X X 85\n84 X X X X X X X X X X X X X X X X X X X X X X X X X X 84\n83 X X X X X X X X X X X X X X X X X X X X X X X X X X 83\n82 X X X X X X X X X X X X X X X X X X X X X X X X X X 82\n81 X X X X X X X X X X X X X X X X X X X X X X X X X X 81\n80 X X X X X X X X X X X X X X X X X X X X X X X X X X 80\n79 X X X X X X X X X X X X X X X X X X X X X X X X X X 79\n78 X X X X X X X X X X X X X X X X X X X X X X X X X X 78\n77 X X X X X X X X X X X X X X X X X X X X X X X X X X 77\n76 X X X X X X X X X X X X X X X X X X X X X X X X X X 76\n75 X X X X X X X X X X X X X X X X X X X X X X X X X X 75\n74 X X X X X X X X X X X X X X X X X X X X X X X X X X 74\n73 X X X X X X X X X X X X X X X X X X X X X X X X X X 73\n72 X X X X X X X X X X X X X X X X X X X X X X X X X X 72\n71 X X X X X X X X X X X X X X X X X X X X X X X X X X 71\n70 X X X X X X X X X X X X X X X X X X X X X X X X X X 70\n69 X X X X X X X X X X X X X X X X X X X X X X X X X X 69\n68 X X X X X X X X X X X X X X X X X X X X X X X X X X 68\n67 X X X X X X X X X X X X X X X X X X X X X X X X X X 67\n66 X X X X X X X X X X X X X X X X X X X X X X X X X X 66\n65 X X X X X X X X X X X X X X X X X X X X X X X X X X 65\n64 X X X X X X X X X X X X X X X X X X X X X X X X X X 64\n63 X X X X X X X X X X X X X X X X X X X X X X X X X X 63\n62 X X X X X X X X X X X X X X X X X X X X X X X X X X 62\n61 X X X X X X X X X X X X X X X X X X X X X X X X X X 61\n60 X X X X X X X X X X X X X X X X X X X X X X X X X X 60\n59 X X X X X X X X X X X X X X X X X X X X X X X X X X 59\n58 X X X X X X X X X X X X X X X X X X X X X X X X X X 58\n57 X X X X X X X X X X X X X X X X X X X X X X X X X X 57\n56 X X X X X X X X X X X X X X X X X X X X X X X X X X 56\n55 X X X X X X X X X X X X X X X X X X X X X X X X X X 55\n54 X X X X X X X X X X X X X X X X X X X X X X X X X X 54\n53 X X X X X X X X X X X X X X X X X X X X X X X X X X 53\n52 X X X X X X X X X X X X X X X X X X X X X X X X X X 52\n51 X X X X X X X X X X X X X X X X X X X X X X X X X X 51\n50 X X X X X X X X X X X X X X X X X X X X X X X X X X 50\n49 X X X X X X X X X X X X X X X X X X X X X X X X X X 49\n48 X X X X X X X X X X X X X X X X X X X X X X X X X X 48\n47 X X X X X X X X X X X X X X X X X X X X X X X X X X 47\n46 X X X X X X X X X X X X X X X X X X X X X X X X X X 46\n45 X X X X X X X X X X X X X X X X X X X X X X X X X X 45\n44 X X X X X X X X X X X X X X X X X X X X X X X X X X 44\n43 X X X X X X X X X X X X X X X X X X X X X X X X X X 43\n42 X X X X X X X X X X X X X X X X X X X X X X X X X X 42\n41 X X X X X X X X X X X X X X X X X X X X X X X X X X 41\n40 X X X X X X X X X X X X X X X X X X X X X X X X X X 40\n39 X X X X X X X X X X X X X X X X X X X X X X X X X X 39\n38 X X X X X X X X X X X X X X X X X X X X X X X X X X 38\n37 X X X X X X X X X X X X X X X X X X X X X X X X X X 37\n36 X X X X X X X X X X X X X X X X X X X X X X X X X X 36\n35 X X X X X X X X X X X X X X X X X X X X X X X X X X 35\n34 X X X X X X X X X X X X X X X X X X X X X X X X X X 34\n33 X X X X X X X X X X X X X X X X X X X X X X X X X X 33\n32 X X X X X X X X X X X X X X X X X X X X X X X X X X 32\n31 X X X X X X X X X X X X X X X X X X X X X X X X X X 31\n30 X X X X X X X X X X X X X X X X X X X X X X X X X X 30\n29 X X X X X X X X X X X X X X X X X X X X X X X X X X 29\n28 X X X X X X X X X X X X X X X X X X X X X X X X X X 28\n27 X X X X X X X X X X X X X X X X X X X X X X X X X X 27\n26 X X X X X X X X X X X X X X X X X X X X X X X X X X 26\n25 X X X X X X X X X X X X X X X X X X X X X X X X X X 25\n24 X X X X X X X X X X X X X X X X X X X X X X X X X X 24\n23 X X X X X X X X X X X X X X X X X X X X X X X X X X 23\n22 X X X X X X X X X X X X X X X X X X X X X X X X X X 22\n21 X X X X X X X X X X X X X X X X X X X X X X X X X X 21\n20 X X X X X X X X X X X X X X X X X X X X X X X X X X 20\n19 X X X X X X X X X X X X X X X X X X X X X X X X X X 19\n18 X X X X X X X X X X X X X X X X X X X X X X X X X X 18\n17 X X X X X X X X X X X X X X X X X X X X X X X X X X 17\n16 X X X X X X X X X X X X X X X X X X X X X X X X X X 16\n15 X X X X X X X X X X X X X X X X X X X X X X X X X X 15\n14 X X X X X X X X X X X X X X X X X X X X X X X X X X 14\n13 X X X X X X X X X X X X X X X X X X X X X X X X X X 13\n12 X X X X X X X X X X X X X X X X X X X X X X X X X X 12\n11 X X X X X X X X X X X X X X X X X X X X X X X X X X 11\n10 X X X X X X X X X X X X X X X X X X X X X X X X X X 10\n 9 X X X X X X X X X X X X X X X X X X X X X X X X X X  9\n 8 X X X X X X X X X X X X X X X X X X X X X X X X X X  8\n 7 X X X X X X X X X X X X X X X X X X X X X X X X X X  7\n 6 X X X X X X X X X X X X X X X X X X X X X X X X X X  6\n 5 X X X X X X X X X X X X X X X X X X X X X X X X X X  5\n 4 X X X X X X X X X X X X X X X X X X X X X X X X X X  4\n 3 X X X X X X X X X X X X X X X X X X X X X X X X X X  3\n 2 X X X X X X X X X X X X X X X X X X X X X X X X X X  2\n 1 X X X X X X X X X X X X X X X X X X X X X X X X X X  1\n   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        t = tuple(tuple(1 for _ in range(99)) for _ in range(26))
        assert fp.territorio_para_str(t) == str1

    def test_5(self):
        str1 = '   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z\n 1 . X . X . X . X . X . X . X . X . X . X . X . X . X  1\n   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        t = ((0,),(1,),(0,),(1,),(0,),(1,),(0,),(1,),(0,),(1,),(0,),(1,),(0,),(1,),(0,),(1,),(0,),(1,),(0,),(1,),(0,),(1,),(0,),(1,),(0,),(1,))
        assert fp.territorio_para_str(t) == str1

    def test_6(self):
        str1 = '   A\n99 X 99\n98 . 98\n97 X 97\n96 . 96\n95 X 95\n94 . 94\n93 X 93\n92 . 92\n91 X 91\n90 . 90\n89 X 89\n88 . 88\n87 X 87\n86 . 86\n85 X 85\n84 . 84\n83 X 83\n82 . 82\n81 X 81\n80 . 80\n79 X 79\n78 . 78\n77 X 77\n76 . 76\n75 X 75\n74 . 74\n73 X 73\n72 . 72\n71 X 71\n70 . 70\n69 X 69\n68 . 68\n67 X 67\n66 . 66\n65 X 65\n64 . 64\n63 X 63\n62 . 62\n61 X 61\n60 . 60\n59 X 59\n58 . 58\n57 X 57\n56 . 56\n55 X 55\n54 . 54\n53 X 53\n52 . 52\n51 X 51\n50 . 50\n49 X 49\n48 . 48\n47 X 47\n46 . 46\n45 X 45\n44 . 44\n43 X 43\n42 . 42\n41 X 41\n40 . 40\n39 X 39\n38 . 38\n37 X 37\n36 . 36\n35 X 35\n34 . 34\n33 X 33\n32 . 32\n31 X 31\n30 . 30\n29 X 29\n28 . 28\n27 X 27\n26 . 26\n25 X 25\n24 . 24\n23 X 23\n22 . 22\n21 X 21\n20 . 20\n19 X 19\n18 . 18\n17 X 17\n16 . 16\n15 X 15\n14 . 14\n13 X 13\n12 . 12\n11 X 11\n10 . 10\n 9 X  9\n 8 .  8\n 7 X  7\n 6 .  6\n 5 X  5\n 4 .  4\n 3 X  3\n 2 .  2\n 1 X  1\n   A'
        t = ((1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1),)
        assert fp.territorio_para_str(t) == str1

    def test_7(self):
        str1 = '   A B C D\n 4 X X X X  4\n 3 X X X X  3\n 2 X X X X  2\n 1 X X X X  1\n   A B C D'
        t = ((1,1,1,1),(1,1,1,1),(1,1,1,1),(1,1,1,1))
        assert fp.territorio_para_str(t) == str1
    
    def test_8(self):
        str1 = '   A B C D\n 4 . . . .  4\n 3 . . . .  3\n 2 . . . .  2\n 1 . . . .  1\n   A B C D'
        t = ((0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0))
        assert fp.territorio_para_str(t) == str1

    def test_9(self):
        t = ((0,1,0,2),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        with pytest.raises(ValueError) as excinfo:
            fp.territorio_para_str(t)
        assert "territorio_para_str: argumento invalido" == str(excinfo.value)

    def test_10(self):
        t = ((0,1,0,0),(0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        with pytest.raises(ValueError) as excinfo:
            fp.territorio_para_str(t)
        assert "territorio_para_str: argumento invalido" == str(excinfo.value)

    def test_11(self):
        t = ((0,1,0,0),(0,0,0,"A"),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        with pytest.raises(ValueError) as excinfo:
            fp.territorio_para_str(t)
        assert "territorio_para_str: argumento invalido" == str(excinfo.value)

    def test_12(self):
        t = ((0,1,0,0),[0,0,0,0],(0,0,1,0),(1,0,0,0),(0,0,0,0))
        with pytest.raises(ValueError) as excinfo:
            fp.territorio_para_str(t)
        assert "territorio_para_str: argumento invalido" == str(excinfo.value)

    def test_13(self): 
        t = (1,0,1,0)
        with pytest.raises(ValueError) as excinfo:
            fp.territorio_para_str(t)
        assert "territorio_para_str: argumento invalido" == str(excinfo.value)

    def test_14(self):
        t = ()
        with pytest.raises(ValueError) as excinfo:
            fp.territorio_para_str(t)
        assert "territorio_para_str: argumento invalido" == str(excinfo.value)

    def test_15(self):
        t = ((1,),)
        s = '   A\n 1 X  1\n   A'
        assert fp.territorio_para_str(t) == s

class TestObtemCadeia:

    def test_1(self):
        t = ((0,),(1,),(0,))
        c = (('B', 1),)
        assert fp.obtem_cadeia(t, ('B',1)) == c

    def test_2(self):
        t = ((0,0,1,1,1), (1,1,1,0,1),(0,0,0,0,1),(0,0,0,1,1), (0,1,1,1,0))
        c = (('B', 1), ('B', 2), ('E', 2), ('A', 3), ('B', 3), ('E', 3), ('A', 4), ('D', 4), ('E', 4), ('A', 5), ('B', 5), ('C', 5), ('D', 5))
        assert fp.obtem_cadeia(t, ('A', 5)) == c

    def test_3(self):
        t = ((0,0,1,1,1), (1,1,1,0,0),(0,0,0,0,1),(0,0,0,1,1), (0,1,1,1,0))
        c = (('B', 1), ('B', 2), ('A', 3), ('B', 3), ('A', 4), ('A', 5))
        assert fp.obtem_cadeia(t, ('A',3)) == c

    def test_4(self):
        t = ((0,0,1,1,1), (1,1,1,0,0),(0,0,0,0,1),(0,0,0,1,1), (0,1,1,1,0))
        c = (('B', 1), ('B', 2), ('A', 3), ('B', 3), ('A', 4), ('A', 5))
        assert fp.obtem_cadeia(t, ('B',1)) == c

    def test_5(self):
        t = ((0,0,1,1,1), (1,1,1,0,0),(0,0,0,0,1),(0,0,0,1,1), (0,1,1,1,0))
        c = (('A', 1), ('A', 2))
        assert fp.obtem_cadeia(t, ('A',1)) == c

    def test_6(self):
        t = (0,1,0,1)
        c = ('A', 1),
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_cadeia(t, c)
            assert "obtem_cadeia: argumentos invalidos" == str(excinfo.value)

    def test_7(self):
        t = ((0,0,1,1,1), (1,1,1,0,0),(0,0,0,0,1),(0,0,0,1,1), (0,1,1,1,0))
        c = ("F",6),
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_cadeia(t, c)
            assert "obtem_cadeia: argumentos invalidos" == str(excinfo.value)

class TestObtemVale:

    def test_1(self):
        t = ((0,),(1,),(0,))
        c = (('A', 1), ('C', 1))
        assert fp.obtem_vale(t, ('B',1)) == c

    def test_2(self):
        t = ((0,0,1,1,1), (1,1,1,0,1),(0,0,0,0,1),(0,0,0,1,1), (0,1,1,1,0))
        c = (('A', 1), ('C', 1), ('E', 1), ('A', 2), ('C', 2), ('D', 2), ('C', 3), ('D', 3), ('B', 4), ('C', 4), ('E', 5))
        assert fp.obtem_vale(t, ('A', 5)) == c

    def test_3(self):
        t = ((1,1,1,1,1),(1,1,1,1,1),(1,1,0,1,1),(1,1,1,1,1),(1,1,1,1,1))
        c = (('C', 3),)
        assert fp.obtem_vale(t, ('A',1)) == c

    def test_4(self):
        t = t = ((1,1,1,1,1),(1,1,1,1,1),(1,1,0,1,1),(1,1,1,1,1),(1,1,1,1,1))
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_vale(t, ('A',6))
        assert "obtem_vale: argumentos invalidos" == str(excinfo.value)
    
    def test_5(self):
        t = t = ((1,1,1,1,1),(1,1,1,1,1),(1,1,0,1,1),(1,1,1,1,1),(1,1,1,1,1))
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_vale(t, ('C',3))
        assert "obtem_vale: argumentos invalidos" == str(excinfo.value)
    
    def test_6(self):
        t = t = ((1,1,1,1,1),(1,1,1,1,1),(1,1,0,1,1),(1,1,1,1,1),(1,1,1,1,1))
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_vale(t, ('F',3))
        assert "obtem_vale: argumentos invalidos" == str(excinfo.value)

class TestVerificaConexao:

    def test_1(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.verifica_conexao(t, ('A',1), ('A',3))
        
    def test_2(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert not fp.verifica_conexao(t, ('A',1), ('C',3))

    def test_3(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.verifica_conexao(t, ('A',4), ('B',1))

    def test_4(self):
        t = ((0,1,0,2),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        with pytest.raises(ValueError) as excinfo:
            fp.verifica_conexao(t, ('A',1), ('A',3))
        assert "verifica_conexao: argumentos invalidos" == str(excinfo.value)

    def test_5(self):
        t = ((0,1,0,1),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        with pytest.raises(ValueError) as excinfo:
            fp.verifica_conexao(t, ('A',0), ('A',3))
        assert "verifica_conexao: argumentos invalidos" == str(excinfo.value)

    def test_6(self):
        t = ((0,1,0,1),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        with pytest.raises(ValueError) as excinfo:
            fp.verifica_conexao(t, ('F',1), ('A',3))
        assert "verifica_conexao: argumentos invalidos" == str(excinfo.value)

    def test_7(self):
        t = ((0,1,0,1),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        with pytest.raises(ValueError) as excinfo:
            fp.verifica_conexao(t, ('A',1), ('A',0))
        assert "verifica_conexao: argumentos invalidos" == str(excinfo.value)

    def test_8(self):
        t = ((0,1,0,1),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        with pytest.raises(ValueError) as excinfo:
            fp.verifica_conexao(t, ('A',1), ('F',3))
        assert "verifica_conexao: argumentos invalidos" == str(excinfo.value)

class TestCalculaNumeroMontanhas:

    def test_1(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_numero_montanhas(t) == 5

    def test_2(self):
        t = ((1,0,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_numero_montanhas(t) == 4

    def test_3(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_numero_montanhas(t) == 5

    def test_4(self):
        t = ((0,1,0,2),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        with pytest.raises(ValueError) as excinfo:
            fp.calcula_numero_montanhas(t)
        assert "calcula_numero_montanhas: argumento invalido" == str(excinfo.value)
    
class TestCalculaNumeroCadeiasMontanhas:

    def test_1(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_numero_cadeias_montanhas(t) == 2

    def test_2(self):
        t = ((1,0,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_numero_cadeias_montanhas(t) == 4

    def test_3(self):
        t = ((1,1,1,1,1),(1,1,1,1,1),(1,1,0,1,1),(1,1,1,1,1),(1,1,1,1,1))
        assert fp.calcula_numero_cadeias_montanhas(t) == 1

    def test_4(self):
        t = ((0,0,0),(0,1,0),(0,0,0))
        assert fp.calcula_numero_cadeias_montanhas(t) == 1

    def test_5(self):
        t = ((0,0,0),(0,0,0),(0,0,0))
        assert fp.calcula_numero_cadeias_montanhas(t) == 0

    def test_6(self):
        t = ((0,1,0,2),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        with pytest.raises(ValueError) as excinfo:
            fp.calcula_numero_cadeias_montanhas(t)
        assert "calcula_numero_cadeias_montanhas: argumento invalido" == str(excinfo.value)
    

class TestCalculaTamanhoVales:

    def test_1(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_tamanho_vales(t) == 6

    def test_2(self):
        t = ((1,0,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_tamanho_vales(t) == 7
    
    def test_3(self):
        t = ((1,1,1,1,1),(1,1,1,1,1),(1,1,0,1,1),(1,1,1,1,1),(1,1,1,1,1))
        assert fp.calcula_tamanho_vales(t) == 1

    def test_4(self):
        t = ((0,0,0),(0,1,0),(0,0,0))
        assert fp.calcula_tamanho_vales(t) == 4

    def test_5(self):
        t = ((1,0,1),(0,1,0),(1,0,1))
        assert fp.calcula_tamanho_vales(t) == 4
        
    def test_6(self):
        t = ((0,1,0),(0,0,0),(0,1,0))
        assert fp.calcula_tamanho_vales(t) == 5

