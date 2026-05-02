# homework.py
score = int(input("점수를 입력하세요: "))

if 81 <= score <= 100:
    print("학점A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41 <= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
elif 0 <= score <= 20:
    print("grade is E")