## variable ##
answer, num1, num2, num3 = 0, 0, 0, 0

## main code ##

num1 = int(input(" ***첫 번째 숫자를 입력하세요 : "))
num2 = int(input(" ***두 번째 숫자를 입력하세요 : "))
num3 = int(input(" ***더할 숫자를 입력하세요 : "))

for i in range(num1, num2+1, num3): # num1부터 num2까지(num2포함) num3만큼 증가
    answer = answer + i
print("%d + %d ... + %d는 %d입니다. " %(num1, num1 + num3, num2, answer))