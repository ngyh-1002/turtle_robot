import turtle

# 스크린 생성
s = turtle.getscreen()

#거북이 변수 지정
t = turtle.Turtle()
t.shapesize(3,3,3)
t.shape('turtle')
t.color("green", "blue")
t.pensize(5)
t.penup()
t.goto(-350,-350)
t.pendown()
t.goto(350, 350)
