import turtle
import math
import random
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
for i in range(3):
    t.fd(100)
    t.lt(120)

# 장애물 지정
t.penup()
t.goto(-50,-50)
t.pendown()

for i in range(4):
    t.fd(100)
    t.lt(90)

#거북이 이동 경로
def turtle_drive(t,a,b,x,y):
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.goto(-70, -70)
    if check_collision(t) == 1:
        print('충돌이 발생했습니다!')
        return
    elif check_collision(t) == 2:
        avoid_obstacle(t)
    t.goto(x, y)
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

# 충돌 감지 함수
def check_collision(t):
    t_x = t.xcor()
    t_y = t.ycor()
    obstacle_distance_square = (0-t_x) ** 2 + (0-t_y) ** 2
    obstacle_distance = math.sqrt(obstacle_distance_square)
    if obstacle_distance <= (24 + 70) :
        return 1
    elif obstacle_distance <= (34 + 70) :
        return 2     
    return 3

#장애물회피함수
def avoid_obstacle(t):
    print("장애물 감지! 회피하겠습니다.")
    direction = random.choice([1, -1])
    if direction == 1:
        turn_angle = random.randint(90, 150)
        t.left(turn_angle)
        print(f"좌회전 {turn_angle}도")

    if direction == -1:
        turn_angle = random.randint(0, 60)
        t.right(turn_angle)
        print(f"우회전 {turn_angle}도")
    
    move_distance = random.randint(200, 300)
    t.forward(move_distance)

    print(f"{move_distance}픽셀 이동 완료")
    
#프로그램실행   
turtle_drive(t, -350, -350, 350, 350)
