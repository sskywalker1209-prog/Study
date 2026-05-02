# # 12hmowork.py

# with open("test.txt", "w") as file:
#     file.write("Hello, World!")

# with open("test.txt", "r") as file:
#     print(file.read())

# print(file.closed)


path = "ch12/pizza_file1.txt"

f = open(path, 'w', encoding='utf-8')

f.write("페퍼로니피자\n")
f.write("치즈피자\n")
f.write("콤비네이션피자\n")

f.close()

f = open(path, 'a', encoding='utf-8')

f.write("불고기피자 3600\n")
f.write("해산물피자 3800\n")

f.close()

f = open(path, 'r', encoding='utf-8')

lines = f.readlines()

for line in lines:
    print(line.strip())

f.close


f = open(path, 'r', encoding="utf-8")

pizza_list = []

lines = f.readlines()

for line in lines:
    data = line.split()
    pizza_list.append(data[0])

f.close()

print(pizza_list)