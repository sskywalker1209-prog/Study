# selectSorting1.py
# 정렬의 종류
# ca = [21,10,11,15,13]
# 오름차순 => 10 11 13 15 21
# 내림차운 => 21 15 13 11 10


# 1. 제일 작은수의 인텍스 번호 찾기
# 2. 찾은 인덱스를 활용해 0번 인덱스에 최소값을 위치 하기
ca = [21,10,11,15,13]
mina = ca[0] # 현 최소값
minix = 0    # 현 최고값 위치(인덱스) 

for sb in range(1,5,1) : 
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb

temp = ca[0]
ca[0] = ca[minix]
ca[minix] = temp

print(ca)

print('------------------------')
mina = ca[1] # 현 최소값
minix = 1    # 현 최고값 위치(인덱스) 

for sb in range(2,5,1) : 
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb

temp = ca[1]
ca[1] = ca[minix]
ca[minix] = temp

print(ca)