from re import I


i, hap = 0,0

for i in range(0, 101, 7):
    hap = hap + i

print("500과 1001사이에 있는 홀수의 합계 : %d" %hap)