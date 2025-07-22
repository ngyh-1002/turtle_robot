import turtle

# 스크린 생성
s = turtle.getscreen()
s.setup(width=900, height=900)
#거북이 변수 지정
t = turtle.Turtle()
t.shapesize(2,2,2)
t.shape('turtle')
t.color("green", "blue")
t.pensize(5)

t.penup()
t.goto(-350,-375)
t.pendown()
t.circle(50)

t.penup()
t.goto(325,325)
t.pendown()
for i in range(4):
    t.fd(100)
    t.lt(90)

t.penup()
t.goto(0,0)
t.pendown()

for i in range(3):
    t.fd(100)
    t.lt(120)
    
t.penup()
t.goto(-350,-350)
t.pendown()
t.goto(-50, -50)
t.lt(60)
t.fd(200)
t.goto(350, 350)
