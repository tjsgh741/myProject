#변수 선언 부분
money, c50000, c10000, c5000, c1000, c500, c100, c50, c10 = 0,0,0,0,0,0,0,0,0

# main code
money = int(input("교환할 돈은 얼마? : "))

c50000 = money // 50000 # 50000으로 나눈 몫
money %= 50000 # 50000으로 나눈 나머지

c10000 = money // 10000 # 10000으로 나눈 몫
money %= 10000 # 10000으로 나눈 나머지

c5000 = money // 5000 # 5000으로 나눈 몫
money %= 5000 # 5000으로 나눈 나머지

c1000 = money // 1000 # 1000으로 나눈 몫
money %= 1000 # 1000으로 나눈 나머지

c500 = money // 500 # 500으로 나눈 몫
money %= 500 # 500으로 나눈 나머지

c100 = money // 100 # 100으로 나눈 몫
money %= 100 # 100으로 나눈 나머지

c50 = money // 50 # 50으로 나눈 몫
money %= 50 # 50으로 나눈 나머지

c10 = money // 10 # 10으로 나눈 몫
money %= 10 # 10으로 나눈 나머지 

print('\n오만원\t==> %d 개'%c50000)
print('만원\t==> %d 개'%c10000)
print('오천원\t==> %d 개'%c5000)
print('천원\t==> %d 개'%c1000)
print('오백원\t==> %d 개'%c500)
print('백원\t==> %d 개'%c100)
print('오십원\t==> %d 개'%c50)
print('십원\t==> %d 개'%c10)
print('잔돈\t==> %d 원'%money)