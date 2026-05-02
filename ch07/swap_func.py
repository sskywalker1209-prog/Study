# swap_func.py

def funca(pa,pb):
    temp = pa
    pa = pb
    pb = temp

na = 10
nb = 11
print ('na값:', na, end=" ")
print ("nb값:", nb)

funca(na, nb)
    
print("na값:" , na, end=" ")
print("nb값:", nb)


def funca(pa, pb):
    temp = pa
    pa = pb
    pb = temp
    return pa, pb

na = 10
nb = 11

print("na값:", na, end=" ")
print("nb값:", nb)

na, nb = funca(na, nb)

print("na값:", na, end=" ")
print("nb값:", nb)