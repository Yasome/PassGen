import random, pyclip, os

r = random


def Occur(type, len):
    temp = len // type
    if not temp: return 1
    return temp


def PassGen(Len, Ultra=True):
    # الحروف المستعملة - Used characters
    CharBank = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '*!@#$%^&|+?', '123456789']
    Password = ''

    # صنع كلمة السر - Generating password
    for i in range(Len):
        Type = CharBank[r.randint(0, 1000) % 4]
        Let = str(Type[r.randint(0, 1000) % (len(Type) - 1)])

        # UltraPassGardTec - يمنع تواجد الحرف او الرقم اكثر من مرة واحدة
        if Ultra:
            while len(Password) > 0 and (
                    Type.count(Password[-1].lower()) != 0 or Type.count(Password[-1].upper()) != 0):
                Type = CharBank[r.randint(0, 1000) % 4]
            Let = str(Type[r.randint(0, 1000) % (len(Type) - 1)])
            Con = Password.count(Let)

            while Con == Occur(len(Type), Len):
                Let = str(Type[r.randint(0, 1000) % (len(Type) - 1)])
                Con = Password.count(Let)
            Password += Let
        else:
            Password += Let

    return Password


os.system("pip install pyclip")
print("\nPassword Length : ", end="")
Len = int(input())
print("Do you want AutoCopy [y,N]: ", end="")
AutoCopy = True if ord(input()) - 78 == 121 - 78 else False
Pass = PassGen(Len)

if AutoCopy:
    pyclip.copy(Pass)
print(Pass)
