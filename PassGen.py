import random, pyclip, os
r = random


def PassGen(Len,Duplicate = False,Sequenctial = False, Ultra = False):
    # الحروف المستعملة - Used characters
    CharBank = ['abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ','*!@#$%^&|+?','123456789']
    Password = ''

    # صنع كلمة السر - Generating password
    for i in range(Len):
        Type = CharBank[r.randint(0, 1000) % 4]

        # UltraPassGardTec - يمنع تواجد الحرف او الرقم اكثر من مرة واحدة
        if Ultra:
            while len(Password) > 0 and (Type.count(Password[-1].lower()) !=0 or Type.count(Password[-1].upper()) !=0):
                Type = CharBank[r.randint(0, 1000) % 4]

            Let = str(Type[r.randint(0, 1000) % (len(Type) - 1)])
            Con = Password.count(Let)

            while Con != 0:
                Let = str(Type[r.randint(0, 1000) % (len(Type) - 1)])
                Con = Password.count(Let)

            Password += Let

        else:
            Password += str(Type[r.randint(0, 1000) % (len(Type) - 1)])


    # منع تتالي الحروف المتكررة و تكرار الجرف اكثر من 3 مرات - PassGardTec
    for i in Password:

        if Sequenctial:
            if Password.count(i) == 2 and (Password.rfind(i) - 1) == Password.find(i):
                Password = PassGen(Len, Duplicate, Sequenctial)

        if Duplicate:
            if Password.count(i) >=3:
                Password = PassGen(Len, Duplicate, Sequenctial)
    return Password


os.system("pip install pyclip")

print("\nPassword Length : ", end="")
Len = int(input())
print("Do you want to use PassGardTec [y,N]: ", end="")
PassGardTec = True if ord(input())-78 == 121-78 else False
print("Do you want to use UltraPassGardTec -Recommended for len < 26- [y,N]: ", end="")
UltraPassGardTec = True if ord(input())-78 == 121-78 else False
print("Do you want AutoCopy [y,N]: ", end="")
AutoCopy = True if ord(input())-78 == 121-78 else False
Pass = PassGen(Len, PassGardTec, PassGardTec, UltraPassGardTec)

if AutoCopy:
    pyclip.copy(Pass)
print(Pass)
