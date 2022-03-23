import turtle

## 전역번수 ##
num1, num2, res = 0, 0, 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

## 2진수를 거북이로 처리하는 함수 ##
def binToTurtle(binary, num):
    curX = swidth / 2
    for i in range(len(binary) - 2) :

        turtle.goto(curX, curY)

        if num & 1 :

            turtle.color('red')

            turtle.turtlesize(2)

        else :

            turtle.color('blue')

            turtle.turtlesize(1)

        turtle.stamp()

        curX -+ 50

        num >>= 1

 

## 메인 코드 부분 ##

if __name__ == "__main__" :
    turtle.title('두개의 숫자로 논리곱하여 거북이로 표현')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

 

    ## 두 개의 숫자 입력 ##

    num1, num2 = map(int, input("숫자를 두개 입력하세요 : ").strip().split(' '))

    curY=0

    binToTurtle(bin(num1), num1)

    curY = -50

    binToTurtle(bin(num2), num2)

    curY = -100

    res = num1 & num2

    binToTurtle(bin(res), res)

 

turtle.done()