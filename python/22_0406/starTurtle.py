import random
import turtle

## variable ##
swidth, sheight, pSize = 1000, 700, 3
r, g, b, x, y, i = 0, 0, 0, 0, 0, 0

## main code ##
turtle.title('star turtle')
turtle.shape('turtle') # 모양은 거북이
turtle.pensize(pSize) # 펜 사이즈 설정
turtle.setup(width = swidth + 30, height = sheight + 30) # 메인 그래픽 창 크기 지정
turtle.screensize(swidth, sheight) # 캔버스 크기 설정
turtle.speed(5)

while True:
    r = random.random() # r, g, b값을 랜덤값으로 설정
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b)) # pencolor를 랜덤하게 설정

    x = random.randrange(-swidth/2, swidth/2) #캔버스 내  랜덤좌표값 설정
    y = random.randrange(-sheight/2, sheight/2) 
    dist = random.randrange(1, 150) # dits값을 1~150사이 랜덤한 값으로 설정

    #펜을 그리지않고 랜덤한 장소로 이동
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    dist = random.randrange(10, 200) #별 하나의 변 길이

    for i in range(5):
        turtle.left(144)
        turtle.forward(dist)


turtle.done()