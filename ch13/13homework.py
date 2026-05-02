# # 13homework.py

# try:
#    raise KeyError("Key is missing!")
# except KeyError as e:
#     print(e)

# add = lambda x,y:x+y

# print(add(3,5))


per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except ValueError:
        print(0)




# # numbers = [10, 20, 30]

# # try:
# #     index = int(input("인덱스를 입력하세요."))
# #     print(numbers[index])
# # except IndexError:
# #     print("잘못된 인덱스입니다.")
# # except ValueError:
# #     print("숫자를 입력해야합니다.")
    

# try:
#     x = int("abc")
# except ValueError:
#     print("ValueError occurred!")
# finally:
#     print("Execution finished.")


# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")