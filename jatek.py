import random
nehezseg=int(input("Nehézségi szint 1, 2 vagy 3: "))
valasz=0
if nehezseg==1:
    szam1=random.randrange(1, 10)
    szam2=random.randrange(1, 10)
    megoldas=szam1*szam2
    while valasz!=megoldas:
        print(szam1,"*",szam2,end=" ")
        valasz=int(input("= "))
        if valasz!=megoldas:
            print("Helytelen")
    print("Helyes megoldas")
if nehezseg==2:
    szam1=random.randrange(1, 101)
    szam2=random.randrange(1, 10)
    megoldas=szam1*szam2
    while valasz!=megoldas:
        print(szam1,"*",szam2,end=" ")
        valasz=int(input("= "))
        if valasz!=megoldas:
            print("Helytelen")
    print("Helyes megoldas")
if nehezseg==3:
    szam1=random.randrange(50, 101)
    szam2=random.randrange(1, 101)
    megoldas=szam1*szam2
    while valasz!=megoldas:
        print(szam1,"*",szam2,end=" ")
        valasz=int(input("= "))
        if valasz!=megoldas:
            print("Helytelen")
    print("Helyes megoldas")