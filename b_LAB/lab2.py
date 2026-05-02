# lab2.py

# height = 1.80
# weight = 78.2
# bmi = weight / height**2
# print(bmi)

# radius = 10
# area = 3.14 * radius**2
# print(f"피자 면적은 {area}")

# radius = 20
# area = 3.14 * radius**2
# print(f"피자 면적은 {area}")

# radius = 30
# area = 3.14 * radius**2
# circumference = 2 * 3.14 * radius

# print("피자 면적은", area)
# print("피자 둘레는", circumference)

# radius = 42
# area = 3.14 * radius**2
# circumference = 2 * 3.14 * radius

# print("피자 면적은", area)
# print("피자 둘레는", circumference)

# -----------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# radius = 50
# t.circle(radius)

# radius = 100
# t.circle(radius)

# radius = 200
# t.circle(radius)


# # import turtle

# # t = turtle.Turtle()
# # t.shape("turtle")

# # radius = 50
# # t.circle(radius)


# import turtle
# t = turtle.Turtle()

# # (1) 반지름 50인 원 그리기
# t.circle(50)




#     import turtle
# t = turtle.Turtle()

# # (1) 반지름 50인 원 그리기
# t.circle(50)

# # (2) 왼쪽으로 90도 돌고 더 큰 원 그리기 패턴
# t.left(90)
# t.circle(60) # 50보다 큰 반지름


# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# radius = 50
# t.circle(radius)
# radius = 100
# t.circle(radius)
# radius = 200
# t.circle(radius)

# t.left(90)

# radius = 50
# t.circle(radius)
# radius = 100
# t.circle(radius)
# radius = 200
# t.circle(radius)

# t.left(90)

# radius = 50
# t.circle(radius)
# radius = 100
# t.circle(radius)
# radius = 200
# t.circle(radius)
# t.left(90)

# radius = 50
# t.circle(radius)
# radius = 100
# t.circle(radius)
# radius = 200
# t.circle(radius)




import turtle

t = turtle.Turtle()
t.shape("turtle")

R = [50,100,200]

for i in range(4):
    for radius in R:
        t.circle(radius)
    t.left(90)













#------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# radii = [50, 100, 200]

# for i in range(4):              # 방향 4번
#     for radius in radii:        # 50, 100, 200
#         t.circle(radius)
#     t.left(90)

#-------------------------------------------------------

# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# radius = 100

# for i in range(4):
#     t.circle(radius)
#     t.left(90)

#-----------------------------------------------------

# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# for radius in [50, 100, 200]:
#     t.circle(radius)
#     t.left(90)



principal = 100000000
years = 5
interest_rate = 0.03

money = principal * (1.0 + interest_rate) ** years

print("원금:", principal)
print("이율:", interest_rate)
print("기간:", years)
print("수령액:", money)