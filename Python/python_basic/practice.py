# from random import *
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매일 " + str(date) + " 일로 선정되었습니다")

### SLICING ###
# jumin = "990120-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지 
# print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지


### 문자열 처리 함수 ###
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index+1)
# print(index)

# print("a" + "b")
# print("a", "b")

# method 1
# print("I am %d years old." % 20) # replaces integer
# print("I like %s." % "Python") # replaces string
# print("Apple starts with %c." % "A") # replaces character
# # %s
# print("I am %s years old." % 20)
# print("I like color %s and %s." % ("Blue", "Red"))

# method 2
# print("I am {} years old.".format(20))
# print("I like color {0} and {1}.".format("Blue", "Red"))
# print("I like color {1} and {0}.".format("Blue", "Red"))

# method 3
# print("I am {age} years old and I like color {color}.".format(age = 20, color="Red"))
# print("I am {age} years old and I like color {color}.".format(color="Red", age = 20))

# method 4 (v3.6 over~)
# age = 20
# color = "Red"
# print(f"I am {age} years old, I like color {color}.")

# \n: start new line
# print("I like new line\nprint new line.")

# \" \' : quotation marks within sentences
# I am "Minjoo".
# print("I am 'Minjoo'.")
# print('I am "Minjoo".')
# print("I am \'Minjoo\'.")
# print('I am \"Minjoo\".')

# \\ : \ within sentences
# print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace>")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : backspace (deletes one letter)
# print("Redd\bApple") 

# \t :  tab
# print("Red\tApple")

"""
Quiz 3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
            (nav)             (5)           (1)          (!)
예) 생선된 비밀번호 : nav51!
"""

# My solution
# def creates_password1(website):
#     pw = website[7:]
#     # print(pw)
#     end_index = pw.index(".")
#     pw = pw[:end_index]
#     # print(pw)
#     pw = pw[:3] + str(len(pw)) + str(pw.count("e")) + "!"
#     return pw

# print(creates_password1("http://naver.com"))

# url = "http://daum.net"
# Model solution
# def creates_password2(url):
#     my_str = url.replace("http://", "") # 규칙1
#     #print(my_str)
#     my_str = my_str[:my_str.index(".")] # 규칙2
#     # my_str[0:5] -> 0 ~5 직전까지. (0, 1, 2, 3, 4)
#     #print(my_str)
#     password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
#     return ("{0}'s password is {1}.".format(url, password))

# print(creates_password2(url))

# List []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용 
# mix_list = ["조세호", 20, True]
# print(mix_list)

# 리스트 확장
# num_list.extend(mix_list)
# print(num_list)


# Dictionary
# cabinet = {3:"유재석", 100:"김태호"} # {key, value}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet[3])
# # print(cabinet[5]) # KeyError: 5
# print(cabinet.get(5)) # print None
# # print("hi")
# print(cabinet.get(5, "사용가능")) # if the value for key 5 is not found, then we output "사용가능" instead

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # 떠난 손님
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)


# Tuple - cannot modify, but faster than list. 

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)



# Set
# 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set) # {1, 2, 3}

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (java 와 python 을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (java 도 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 수 있는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java 를 잊었어요
# java.remove("김태호")
# print(java)



# 자료구조의 변경
# 커피숍
# menu = {"coffee", "milk", "juice"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))


"""
Quiz 4) 당신의 학교에서는 파이썬 코딩 대회를 주회합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3: random 모듈의 shuffle 과 sample 을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
1st = [1,2,3,4,5]
print(1st)
shuffle(1st)
print(1st)
print(sample(1st, 1))
"""

# My answer
# from random import *
# candidates = list(range(0,20))
# print(candidates)
# chicken = choice(candidates)
# # print(chicken)
# candidates.pop(candidates.index(chicken))
# coffee1 = choice(candidates)
# candidates.remove(coffee1)
# coffee2 = choice(candidates)
# candidates.remove(coffee2)
# coffee3 = choice(candidates)
# winners = [chicken, coffee1, coffee2, coffee3]
# print(winners)

# Model answer
# from random import *
# users = range(1, 21)
# #print(type(users)) #type: iterable
# users = list(users)
# #print(type(users)) #type: list

# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

# print(" -- 당첨자 발표 -- ")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 -- ")



# IF

# weather = input("오늘 날씨는 어때요?") 
# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")



# FOR LOOP

# for waiting_no in [0, 1, 2, 3, 4]:
# for waiting_no in range(1,6): # 1, 2, 3, 4, 5
    # print("대기번호 : {0}".format(waiting_no))
    
    

# WHILE LOOP
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True: # infinite loop
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회.".format(customer, index))

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")
# print("Here is your coffee. ")



# CONTINUE / BREAK

# absent = [2, 4] # 결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#     if student in absent:
#         continue # go to the next index
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break # break for loop
#     print("{0}, 책을 읽어봐".format(student))



# ONE LINE FOR LOOP

# # 출석번호가 1, 2, 3, 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# # 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)


""" 
Quiz 5) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수(random number)로 정해집니다.
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분
"""
from random import *

# My answer
# customers = list(range(1,51))
# time_customers = {} 
# matched = []
# for i in customers:
#     time_customers[i] = randrange(5,51)
#     if 5 <= time_customers[i] <= 15:
#         matched.append((i, time_customers[i]))
# print(len(matched), matched)

# Model answer
# cnt = 0 # 총 탑승 승객 수
# for i in range(1, 51):
#     time = randrange(1, 51) # 5분 ~ 50분 소요 시간 
#     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님 (매칭 성공), 탑승 승객 수 증가 처리
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else: # 매칭 실패한 경우
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print(f"총 탑승 승객 : {cnt}")



# FUNCTION
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else: 
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): # 저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission

# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500) 
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))



# BASIC VALUE (기본값)

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#           .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업. 

# def profile(name, age=17, main_lang="python"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#           .format(name, age, main_lang))
    
# profile("유재석") # output: 이름 : 유재석   나이 : 17   주 사용 언어 : python
# profile("김태호") # output: 이름 : 김태호   나이 : 17   주 사용 언어 : python



# KEYWORD 

# def profile(name, age, main_lang):
#     print(name, age, main_lang)
    
# profile(name="유재석", main_lang="파이썬", age=20) # output: 유재석 20 파이썬
# profile(main_lang="자바", age=25, name="김태호") # output: 김태호 25 자바



# 가벼 인자
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" " 를 쓰면 프린트할때 줄바꿈을 하지 않고 " " 이렇게만 끝남
#     # print(lang1, lang2, lang3, lang4, lang5)
#     for lang in language:
#         print(lang, end= " ")
#     print()
    
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kotlin", "Swift")



# 지역변수와 전역변수 Local variable and Global variable

# gun = 10

# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계 근무 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총: {0}".format(gun))
    


"""
Quiz 6 ) 표준 체중을 구하는 프로그램을 작성하시오

표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
 남자 : 키(m) x 키(m) x 22
 여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        함수명 : std_weight
        전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""

# My answer 
# def std_weight(height, gender): 
#     sw = 0
#     height /= 100
#     if gender == "m":
#         sw = height * height * 22
#         sw = float("{:.2f}".format(sw)) # represent until 2nd d.p.
#     else: 
#         sw = height * height * 21
#         sw = float("{:.2f}".format(sw)) # represent until 2nd d.p.
#     return sw
#
# print(std_weight(175, "m")) # prints 67.38

# Model answer
# def std_weight(height, gender): # 키 m 단위 (실수), 성별 "남자" / "여자"
#     if gender == "남자":
#         return height * height * 22
#     else: 
#         return height * height * 21

# height = 175 # cm 단위
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다")



# 표준 입출력

# import sys
# print("Python", "Java") # Python Java
# print("Python" + "Java") # PythonJava
# # sep : separation between "Python" and "Java"
# print("Python", "Java", "Javascript", sep=" vs ") # Python vs Java vs Javascript
# print("Python", "Java", "Javascript", sep=",", end="?")
# print("무엇이 더 재밌을까요?")
# # the two lines above print consecutively on the same line: Python,Java,Javascript?무엇이 더 재밌을까요?

# print("Python", "Java", file=sys.stdout) # Python Java
# print("Python", "Java", file=sys.stderr) # Python Java

# 시험 성적
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items(): # (key,value)
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")  # ljust(8) : 왼쪽 정렬 8칸
#     # 수학      :   0
#     # 영어      :  50
#     # 코딩      : 100    

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))
    
# answer = input("아무 값이나 입력하세요 : ") # type(answer) = str
# answer = 10 # type(answer) = int
# print(type(answer))
# print("입력하신 값은 " + answer + " 입니다.")    



# 다양한 출력 포맷

# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500)) # > 왼쪽 #       +500
# print("{0: >+10}".format(-500)) #       -500
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500)) # < 오른쪽 # +500______
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(10000000000)) # 10,000,000,000
# # 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기 
# print("{0:+,}".format(10000000000)) # +10,000,000,000
# print("{0:+,}".format(-10000000000)) # -10,000,000,000
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
# print("{0:^<+30,}".format(10000000000000)) # +10,000,000,000,000^^^^^^^^^^^
# # 소수점 출력
# print("{0:f}".format(5/3)) # 1.666667
# # 소수점 특정 자릿수 까지만 표시
# print("{0:.2f}".format(5/3)) # 1.67



# 파일 입출력 FILE INPUT

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # "a": 이어쓰기
# score_file.write("\n과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # "r": reading
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# 위에 방법들은 파일안에 줄이 몇개인지 알때 사용. 
# 지금 아래 방법은 파일안에 줄이 몇개인지 몰라~ 그때 사용!
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="") # end="" : simply skips line instead of adding a whole empty new line in between elements
# score_file.close()

# 리스트에다가 값을 넣어서 처리하기
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
    
# score_file.close() # always remember to close your file



# pickle
# 피클 : 프로그램상 우리가 사용하고 있는 내용을 파일 형태로 저장해줌. 
 
# import pickle
# # profile_file = open("profile.pickle", "wb") # "w" : write in file ; "b" : binary - essential for using pickle 
# # profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# # profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()



# With

# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")
    
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())



"""
Quiz 7) 당신의 회에는 매 1회 작성해야 하는 보고서가 있습니다.
보서는 항상 아래와 같은 형태로 출력되어야 합니다. 

- X 주차 주간보고 -
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
"""

# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- " + str(i) + " 주차 주간보고 -")
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")
        


# CLASS

# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유신의 체력
# damage = 5 # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format( \
#         name, location, damage))
    
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# from random import *

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성 되었습니다.".format(name))
#         # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0 : 
#             print("{} : 파괴되었습니다.".format(self.name))
        
# # # marine1 = Unit("마린", 40, 5)
# # # marine2 = Unit("마린", 40, 5)
# # # tank = Unit("탱크", 150, 35)

# # # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# # wraith1 = Unit("레이스", 80, 5)
# # print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # # 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것 (빼앗음)
# # wraith2 = Unit("레이스", 80, 5)
# # wraith2.clocking = True

# # if wraith2.clocking == True:
# #     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# # # if wraith1.clocking == True:
# # #     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# # 공격 유닛
# class AttackUnit(Unit): # 유닛 클래스 상속 받음
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))
        

# # 마린 
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)
        
#     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
            
# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가. 
#     seize_developed = False # 시즈모드 개발 여부         
    
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False       
    
#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return 
        
#         # 현재 시즈모드가 아닐 때 -> 시즈모드 
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
        
#         # 현재 시즈모드일 때 -> 시즈모드 해제
#         if self.seize_mode == True:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False
# """
# # # 메딕 : 의무병
        
# # # 파이어뱃 : 공격 유닛, 화염방사기
# # firebat1 = AttackUnit("파이어뱃", 50, 16)
# # firebat1.attack("5시")

# # # 공격 2번 받는다고 가정
# # firebat1.damaged(25)
# # firebat1.damaged(25)
# """

# ### 다중 상속 ###

# # 드랍쉽 : 공중 유닛, 수송기. 마린 / 파어뱃 / 탱크 등을 수송. 공격 X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
        
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
       
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False # 클로킹 모드 (해제 상태)
        
#     def clocking(self): # 클로킹 모드 -> 모드 해제
#         if self.clocked == True:
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name)) 
#             self.clocked = False
#         else: # 클로킹 모드 해제 -> 모드 설정
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True
        
# """        
# # # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사. 
# # valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# # valkyrie.fly(valkyrie.name, "3시") 

# # 메소드 오버라이딩

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음. 
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# ### PASS ###
# ### SUPER ###

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__.init__(self, name, hp, 0) # 건물은 이동 못하니까 speed = 0
#         super().__init__(name, hp, 0)
#         self.location = location
#         # pass
    
# # # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# # supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
        
# """

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg") # good game
#     print("[Player ] 님이 게임에서 퇴장하셨습니다.")

# # 실제 게임 시작
# game_start()

# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# #레이스 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리 (생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine): 
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")
    
# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5~20)

# # 게임 종료
# game_over()


"""
# Quiz 8) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
# class House:
#     # 매물 초기화 
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         pass
    
#     # 매물 정보 표시
#     def show_detail(self):
#         pass

class House:
    # 매물 초기화 
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    # 매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}년".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))
        
houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010")
house2 = House("마포", "오피스텔", "전세", "5억", "2007")
house3 = House("송파", "빌라", "월세", "500/50", "2000")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    House.show_detail(house)
"""


### 예외 Exception ###

# try:        
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError: 
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err: # 나머지 에러 처리 가능. 
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)


# ### 사용자 정의 예외처리 ### 
# ### FINALLY : 예외처리 구문에서 정상적으로 수행이 되건 오류가 발생하건 무조건 실행되는 구문 ###

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg= msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")
    

"""
Quiz 9) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다. 
대기 손님의 치킨 요리 시칸을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리 
        출력 메시지 : "잘못된 값을 입력하였습니다."
조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        출력 메시지 : "제고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]
# """
# class SoldOutError(Exception):
#     def __init__(self, msg):
#         self.msg= msg
    
#     def __str__(self):
#         return self.msg
    
# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작
# can_order = True
# try: 
#     while(can_order):
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken: # 남은 치킨보다 주문량이 많을때
#             print("재료가 부족합니다.")
#         elif order > chicken:
#             can_order = False
#             raise SoldOutError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
#                 .format(waiting, order))
#             waiting += 1 
#             chicken -= order
# except ValueError:
#     print("잘못된 값을 입력하였습니다.")
# except SoldOutError:
#     print("제고가 소진되어 더 이상 주문을 받지 않습니다.")
    
    


### MODULE ###

# import theater_module
# theater_module.price(3) # 3명에서 영화 보러 갔을 때 가격
# # 3명 가격은 30000원 입니다.
# theater_module.price_morning(4) #4명에서 조조 할인 영화 보러 갔을때 
# theater_module.price_soldier(4) #5명의 군인이 영화 보러 갔을 때

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7)

# from theater_module import price_soldier as price
# price(5)



### PACKAGE ### 
# package : module 들을 모아둔 집합

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
 
# # # from random import *
# from travel import *
# # # trip_to = vietnam.VietnamPackage()
# # trip_to = thailand.ThailandPackage()
# # trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))



### PIP INSTALL ###

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())



### 내장 함수 ###

# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# lst = [1,2,3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))


"""
Google에 "list of python builtins" 검색 --> 파이썬 내에서 쓸수 있는 내장 함수 리스트 있음. 
"""


### 외장 함수 ###

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py 인 모든 파일 

# os : 운영체제에서 제공하는 기본 기능
# import os 
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"
 
# if os.path.exists(folder): 
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은", today + td)



"""
Quiz #10) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

조건 : 모듈 파일명은 byme.py 로 작성

(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com
"""

import byme
byme.sign()