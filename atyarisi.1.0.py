import random
from time import sleep

tahmin = input("Tahmininiz nedir?(A, B, C, D): ")
okuyucu = input("Hizli mod icin 'h' yavaş mod için 'y' yaziniz: ")

if okuyucu == "h":
    A = 0
    B = 0
    C = 0
    D = 0
    dongu = 1

    print(
        """ 
               
               
               
               
               
               
               
               
            
               
               
               
               
               
               
               
               
               
               
               
               
               
        """
    )
    print(" o-----------------------------------------o")
    print("          MÜSABAKA BAŞLIYOR!")
    print("          A[][][][][][][][][]")
    print("          B[][][][][][][][][]")
    print("          C[][][][][][][][][]")
    print("          D[][][][][][][][][]")
    print(" o-----------------------------------------o")

    while dongu == 1:
        sleep(1)
        print(
            """ 
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
            """
        )
        print(" o-----------------------------------------o")
        A = random.randint(0, 1) + A
        B = random.randint(0, 1) + B
        C = random.randint(0, 1) + C
        D = random.randint(0, 1) + D

        if A < 1:
            print("          A[][][][][][][][][]")
        if 1 <= A < 2:
            print("          []A[][][][][][][][]")
        if 2 <= A < 3:
            print("          [][]A[][][][][][][]")
        if 3 <= A < 4:
            print("          [][][]A[][][][][][]")
        if 4 <= A < 5:
            print("          [][][][]A[][][][][]")
        if 5 <= A < 6:
            print("          [][][][][]A[][][][]")
        if 6 <= A < 7:
            print("          [][][][][][]A[][][]")
        if 7 <= A < 8:
            print("          [][][][][][][]A[][]")
        if 8 <= A < 9:
            print("          [][][][][][][][]A[]")
        if 9 <= A < 10:
            print("          [][][][][][][][][]A")
        if A == 10:
            print("          A A A A A A A A A A")

        if B < 1:
            print("          B[][][][][][][][][]")
        if 1 <= B < 2:
            print("          []B[][][][][][][][]")
        if 2 <= B < 3:
            print("          [][]B[][][][][][][]")
        if 3 <= B < 4:
            print("          [][][]B[][][][][][]")
        if 4 <= B < 5:
            print("          [][][][]B[][][][][]")
        if 5 <= B < 6:
            print("          [][][][][]B[][][][]")
        if 6 <= B < 7:
            print("          [][][][][][]B[][][]")
        if 7 <= B < 8:
            print("          [][][][][][][]B[][]")
        if 8 <= B < 9:
            print("          [][][][][][][][]B[]")
        if 9 <= B < 10:
            print("          [][][][][][][][][]B")
        if B == 10:
            print("          B B B B B B B B B B")

        if C < 1:
            print("          C[][][][][][][][][]")
        if 1 <= C < 2:
            print("          []C[][][][][][][][]")
        if 2 <= C < 3:
            print("          [][]C[][][][][][][]")
        if 3 <= C < 4:
            print("          [][][]C[][][][][][]")
        if 4 <= C < 5:
            print("          [][][][]C[][][][][]")
        if 5 <= C < 6:
            print("          [][][][][]C[][][][]")
        if 6 <= C < 7:
            print("          [][][][][][]C[][][]")
        if 7 <= C < 8:
            print("          [][][][][][][]C[][]")
        if 8 <= C < 9:
            print("          [][][][][][][][]C[]")
        if 9 <= C < 10:
            print("          [][][][][][][][][]C")
        if C == 10:
            print("          C C C C C C C C C C")

        if D < 1:
            print("          D[][][][][][][][][]")
        if 1 <= D < 2:
            print("          []D[][][][][][][][]")
        if 2 <= D < 3:
            print("          [][]D[][][][][][][]")
        if 3 <= D < 4:
            print("          [][][]D[][][][][][]")
        if 4 <= D < 5:
            print("          [][][][]D[][][][][]")
        if 5 <= D < 6:
            print("          [][][][][]D[][][][]")
        if 6 <= D < 7:
            print("          [][][][][][]D[][][]")
        if 7 <= D < 8:
            print("          [][][][][][][]D[][]")
        if 8 <= D < 9:
            print("          [][][][][][][][]D[]")
        if 9 <= D < 10:
            print("          [][][][][][][][][]D")
        if D == 10:
            print("          D D D D D D D D D D")

        if (A == 10) and (B != 10) and (C != 10) and (D != 10):
            print("A kazandi! ")
            print(" ")
            if (tahmin == "A") or (tahmin == "a"):
                print("tebrikler kazandiniz!!! ")
            else:
                print("malesef kaybettiniz...")
            dongu += 1

        if (B == 10) and (A != 10) and (C != 10) and (D != 10):
            print("B kazandi! ")
            print(" ")
            if (tahmin == "B") or (tahmin == "b"):
                print("tebrikler kazandiniz!!! ")
            else:
                print("malesef kaybettiniz...")
            dongu += 1

        if (C == 10) and (B != 10) and (A != 10) and (D != 10):
            print("C kazandi! ")
            print(" ")
            if (tahmin == "C") or (tahmin == "c"):
                print("tebrikler kazandiniz!!! ")
            else:
                print("malesef kaybettiniz...")
            dongu += 1

        if (D == 10) and (B != 10) and (C != 10) and (A != 10):
            print("D kazandi! ")
            print(" ")
            if (tahmin == "D") or (tahmin == "d"):
                print("tebrikler kazandiniz!!! ")
            else:
                print("malesef kaybettiniz...")
            dongu += 1

        if (
            ((A == 10) and (B == 10))
            or ((A == 10) and (C == 10))
            or ((A == 10) and (D == 10))
            or ((B == 10) and (C == 10))
            or ((B == 10) and (D == 10))
            or ((C == 10) and (D == 10))
        ):
            print("Beraberlik! ")
            print("Belki birdahaki sefere kazanirsiniz... ")
            dongu += 1

        print(" o-----------------------------------------o")

    tekrarlama = input("Tekrar oynamak ister misiniz? (e: evet, h: hayir): ")
    if tekrarlama == "e":
        dongu += 1
    elif tekrarlama == "h":
        print("program 3 saniye içinde kapanicaktir, bilginize...")
        sleep(3)
        exit
    else:
        print("düzgün tuşa basmadiğin için 5 saniye içinde atilcaksin...")
        sleep(1)
        print("... ")
        sleep(1)
        print("bb ")
        sleep(3)
        exit
