import turtle
import random

# variable declaration

swidth, sheight, pSize, exitCount = 300, 300, 3, 0
# r, g, b, angle, dist, curX, curY = [0]*7

# main code

turtle.title('거북이가 맘대로 다니기')
turtle.shape('turtle') # 모양은 거북이
turtle.pensize(pSize) # 펜 사이즈 설정
turtle.setup(width = swidth + 100, height = sheight + 100) # 메인 그래픽 창 크기 지정
turtle.screensize(swidth, sheight) # 캔버스 크기 설정

turtle.penup()
turtle.goto(0, 160)
turtle.pendown()
s = 'exit count : ' + str(exitCount)
turtle.write(s, False, font=("Arial", 20))
turtle.penup()
turtle.goto(0, 0)

while True : # while 무한 반복
    r = random.random() ; g = random.random() ; b = random.random()
    # r, g, b값을 랜덤값으로 설정
    turtle.pencolor((r, g, b)) # pencolor를 랜덤하게 설정

    angle = random.randrange(0, 360) # andgle(각도)값을 0~360사이 랜덤한 값으로 설정
    dist = random.randrange(1, 100) # dits값을 1~100사이 랜덤한 값으로 설정
    turtle.left(angle) # 왼쪽으로 angle값 만큼 회전
    turtle.forward(dist) # 앞으로 dist값 만큼 이동
    curX = turtle.xcor() # 거북이의 현재 x좌표
    curY = turtle.ycor() # 거북이의 현재 y좌표

    # 거북이의 좌표를 캔버스 크기와 비교해서 캔버스 안에 있다면 조건문 실행
    if(-swidth / 2 <= curX and curX <= swidth / 2) and (-swidth / 2 <= curY and curY <= swidth / 2) :
        pass
    else : # 캔버스 밖으로 나간 거북이 위치를 (0, 0)으로 이동
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

        exitCount += 1
        if exitCount >= 5 : #캔버스 밖으로 5번 나가면 while 무한루프를 빠져나감
            break

turtle.done()