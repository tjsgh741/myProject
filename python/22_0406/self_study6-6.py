hap = 0
a, b = 0, 0

while True :
    a = input("더할 첫 번째 수를 입력하세요 : ")
    if a=="$":
        break
    a = int(a)
    b = int(input("계산할 첫 번째 수를 입력하세요 : "))
    hap = a + b
    print("%d + %d = %d" %(a, b, hap))
    
print("$을 입력해 반복문을 탈출했습니다.")