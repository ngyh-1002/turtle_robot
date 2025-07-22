import turtle
import math

# 스크린 생성
s = turtle.getscreen()
s.setup(width=900, height=900)

#거북이 변수 지정
t = turtle.Turtle()
t.shapesize(2,2,2)
t.shape('turtle')
t.color("green", "blue")
t.pensize(5)

#출발지점 표시
t.penup()
t.goto(-350,-375)
t.pendown()
t.circle(50)

#도착지점 표시
t.penup()
t.goto(325,325)
t.pendown()
for i in range(4):
    t.fd(100)
    t.lt(90)

# 장애물 지정
t.penup()
t.goto(0,0)
t.pendown()

for i in range(3):
    t.fd(100)
    t.lt(120)

#거북이 이동 경로
def turtle_drive(t,a,b,x,y):
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.goto(-50, -50)
    t.lt(60)
    t.fd(200)
    t.goto(x,y)
    turtle_distance(a,b,x,y)
    drive_finish(t,x,y)
    return
#출발, 도착지점 거리계산함수
def turtle_distance(a,b,x,y):
    t_distace_square = (a-x) * (a-x) + (b-y) * (b-y)
    t_distance = math.sqrt(t_distace_square)
    return print(f'거북이의 출발지에서 도착지까지 거리 : {t_distance}')

#도착확인기능함수
def drive_finish(t,x,y):
    if t.pos() >= (x-25, y-25) and t.pos() <= (x+25, y+25):
        return print("목적지에 도착했습니다!")
        
#프로그램실행   
turtle_drive(t, -350, -350, 350, 350)