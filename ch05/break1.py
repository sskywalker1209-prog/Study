# break1.py

count = 0
while count < 3:
    count = count + 1
    if count == 2:
        break
    print(count)


print('--------------')
users = ['kim','lee','park']
for user in users : 
    if user == 'lee':
        print('발견!')
        break

while True :
    cmd = input("프롬프트:")
    if cmd == "파이썬3":
        print('파이썬 프로그램 실행')
    elif cmd == '종료':
        print("종료되었습니다")
    break