## variable ##
num1, num2, out = 0, 0, 0
result = True 
answer = [0] #리스트 값 0으로 초기화

## main code ##
num1 = int(input("2이상의 정수 num1을 입력하세요 : "))
num2 = int(input("2이상의 정수 num2을 입력하세요 : "))

for i in range(num1, num2+1) : # 두 숫자 사이의 값 차례로 i값에 대입, num2값까지 포함하기위해 +1을 함
    for j in range(2, i): # 2이상 자기 자신 -1숫자를 구하는 for문
        if i%j == 0 : # 나머지가 0일때
            result = False # 결과값은 False
            break # 나머지 0 즉 소수가 아니기에 바로 for문을 중단한다
        else:
            result = True # 소수 일때 True
    if result == True:
        answer.append(i) # 소수인 숫자만 answer리스트에 넣는다

for i in range(len(answer)): # 모든 소수를 합한다
    out = out + int(answer[i])
print(out) # 합한 소수 출력