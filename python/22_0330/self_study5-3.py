## variable ##
answer, num = True, 0


## main code ##
num = int(input("*** 숫자를 입력하세요 : "))

for i in range(2, num):
    if num%i == 0:
        answer = False

if answer == True:
    print("%d는 소수입니다." %num)
else :
    print("%d는 소수가 아닙니다." %num)