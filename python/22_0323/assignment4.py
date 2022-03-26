import turtle
import random

# 사용자 함수

def binPrint(num, binary, curX, curY): # 거북이로 2진수 찍어주는 함수
    curX = swidth / 2 # 처음 거북이 찍히는 X좌표를 화면 오른쪽 끝으로 고정

    for i in range(len(binary) - 2) : # 2진수 변환값 앞 2글자를 제외하기 위해 -2를 한다
        turtle.goto(curX, curY)
        if num & 1 : # 1일때 빨간 거북이
            turtle.color('red')
            turtle.turtlesize(2)
        else : # 0일 때 파란 거북이
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num >>= 1 # 이미 표현한 비트는 제거하기 위해 사용
    curY -= 50 # 다음줄로 넘어가기 위해
    return curY # curY값은 계속 바뀌어야 하기 때문에 값을 반환한다


# variable declaration
num1, num2, res = 0, 0, 0
swidth, sheight, = 1000, 300
curX, curY = 0, 0

# main code
if __name__ == "__main__" :
    turtle.title('거북이로 2진수 & 비트 논리곱')
    turtle.shape('turtle') # 모양은 거북이
    turtle.setup(width = swidth + 50, height = sheight + 50) # 메인 그래픽 창 크기 지정
    turtle.screensize(swidth, sheight) # 캔버스 크기 설정
    turtle.penup()
    turtle.left(90) #거북이 방향 위를 바라보게 설정(고정)

    num1 = int(input("num1를 입력하세요 : "))
    binary1 = bin(num1)
    num2 = int(input("num2를 입력하세요 : "))
    binary2 = bin(num2)
    res = num1&num2
    resbin = bin(res)

    curX = swidth / 2
    curY = 50

    curY = binPrint(num1, binary1, curX, curY)
    curY = binPrint(num2, binary2, curX, curY)
    binPrint(res, resbin, curX, curY)

turtle.done()