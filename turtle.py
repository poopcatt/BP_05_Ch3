# vsc 터틀그래픽

5. # 4번문제에서 계산한 거리가 맞는지, 터틀그래픽으로 확인해보자. 거북이를 왼쪽으로 45도회전하여 141만큼 전진시킨다.
   # 다시 거북이를 (0, 0)으로 이동하고 0도를 가리키게 한 후에 100만큼 전진하고 왼쪽으로 90도 회전하여 100만큼 전진한다. 화면에 그려진 직선이 일치 하는가?


import turtle
t = turtle.Turtle()
t.shape("turtle")
t.left(45)
t.fd(141)
t.setheading(0)
t.goto(0,0)
t.fd(100)
t.left(90)
t.fd(100)
t.screen.exitonclick()

6. #사용자로부터 두 점을 입력받아서 터틀 그래픽을 이용하여 두 점을 연결하는 직선을 그린다. 직선의 끝점에 직선의 길이를 계산하여 츨력해보자.

import turtle
t = turtle.Turtle()
t.shape("turtle")
x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
d = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)
t.write("두 점 사이의 거리" + str(d))
t.screen.exitonclick()