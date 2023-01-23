
z = input("first number in reverse ")
x = input("second number in reverse ")
z = z.split() # z = [9, 9, 9, 9, 9, 9, 9]
x = x.split() # x = [9, 9, 9, 9]


def sum_of(zz, xx):
    x1 = ""
    z1 = ""
    sumList = []
    xx = list(map(str, xx))
    zz = list(map(str, zz))
    l_xx = len(xx)
    l_zz = len(zz)

    while l_xx > 0:
        x1 = x1 + xx[l_xx - 1]
        l_xx -= 1

    x1 = int(x1)

    while l_zz > 0:
        z1 = z1 + zz[l_zz - 1]
        l_zz -= 1

    z1 = int(z1)

    for i in str(z1 + x1):
        sumList.append(i)

    sumList.reverse()
    return sumList


print(sum_of(z, x))
