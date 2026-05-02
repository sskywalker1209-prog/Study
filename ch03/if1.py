# if1.py

# if 조건식 : 
#     코드블록

score = 90      # 초기화
# socre = 79    # 재할당
# if score > 80 :
#     print("합격입니다.")
# print("프로그램 종료입니다.")

# print ("---------------------")

# score = 60
# if score > 80 : 
#     print ("합격입니다.")
# else :
#     print("불합격입니다.")
# print("프로그램 종료")

# na = 21
# if na % 2 == 0 :
#     print(na, "짝수")

# else :
#     print(na, "홀수")
# print("if 문 종료 됨")


# tscore = 700

# if tscore >= 900 :
#     print("당신의 토익 점수는", tscore, "상위 점수입니다.")
# elif tscore >= 700 :
#     print("당신의 토익 점수는", tscore, "중위원입니다.")
# else :
#     print("당신의 토익점수는", tscore, "하위권입니다.")
# print("if문 종료됨.")

tscore = 200

if tscore >= 900 :
    print("당신의 토익 점수는", tscore, "상위권입니다.")
elif tscore >= 600 :
    print("당신의 토익 점수는", tscore, "중상위원입니다.")
elif tscore >= 300 :
    print("당신의 토익 점수는", tscore, "중위원입니다.")
else :
    print("당신의 토익점수는", tscore, "하위권입니다.")
print("if문 종료됨.")