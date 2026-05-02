
# na = 10
# nb = 11
# print("na 값:", na, end=" ")
# print("nb 값:", nb)

# temp = na
# na = nb
# nb = temp 
# print("na 값:", na, end=" ")
# print("nb 값:", nb)


# na = 10
# nb = 11
# print("na 값:", na, end=" ")
# print("nb 값:", nb)

# na, nb = nb, na
# print("na 값:", na, end=" ")
# print("nb 값:", nb)


def scope_test():
    a = 1
    print("함수 안 a:", a)

a = 0
print("함수 밖 a:", a)

scope_test()

print("함수 호출 후 a:", a)

scope_test()