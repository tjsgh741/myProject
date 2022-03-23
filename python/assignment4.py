# 1. 첨부 소스코드는 사용자로부터 임의의 수를 입력받아 
# 거북이로 이진수형태(빨간색은 1, 파란색은 0)로 표시하는 프로그램이다. 
# 소스를 이해한 다음, 임의의 숫자 2개를 입력받아 
# 각 숫자에 대한 2진수와 비트 논리곱의 결과를 출력하는 프로그램을 작성하시오. 
# 아래 그림은 숫자1은 128, 숫자2는 238을 입력받아, 비트 논리곱을 구한 그림이다. 
# 결과 그림을 캡쳐해서 넣고 소스는 주석으로 설명을 단 보고서를 제출하시오
# (숫자 입력은 임의대로 할 것)

import turtle
import random

# variable declaration
num1, num2, bin1, bin2, myresult = 0, 0, 0, 0, 0
swidth, sheight, pSize, exitCount = 1000, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0]*7

# main code
if __name__ == "__main__" :
    turtle.title('거북이로 2진수 & 비트 논리곱')
    turtle.shape('turtle') # 모양은 거북이
    # turtle.pensize(pSize) # 펜 사이즈 설정
    turtle.setup(width = swidth + 50, height = sheight + 50) # 메인 그래픽 창 크기 지정
    turtle.screensize(swidth, sheight) # 캔버스 크기 설정
    turtle.penup()
    turtle.left(90)

    num1 = int(input("정수 a값 입력 : "))
    num2 = int(input("정수 b값 입력 : "))

    bin1 = bin(num1)
    bin2 = bin(num2)

    for i in range(len(bin1) - 2) :
        turtle.goto(curX, curY)
        if i & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
            turtle.forward(10)
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
            turtle.forward(10)

        turtle.stamp()

        curX -+ 50

        num1 >>= 1

    
turtle.done()




