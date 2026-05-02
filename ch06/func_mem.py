# func_mem.py

# na = 10
# nb = 11

# pa = na
# pb = nb

# nc = pa + pb # 21
# print(nc)


# print('-------------')
# def funca(pa,pb):
#     nc = pa + pb

# na = 10
# nb = 11

# funca(pa,pb)
# print(na, '+', nb, '=', nc)


# print('-------------')
# def funca(pa,pb):
#     nc = pa + pb
#     return nc

# na = 10
# nb = 11
# nd = funca(pa,pb)
# print(na, '+', nb, '=', nd)


def myabs(arg):
    if arg < 0:
        result = arg * -1
    else:
        result = arg
    return result