from turtle import *
import tkinter
from random import randint
player1=input("enter 1 player name")
player2=input("enter 2 player name")
player3=input("enter 3 player name")
player4=input("enter 4 player name")
penup()
goto(-50,200)
pendown()
write("TURTLE RACE",True,font=("Times",20,"bold"))
speed(0)
bgcolor("pink")
penup()
goto(-140,140)
pendown()
for i in range(0,4):
    write(i)
    right(90)
    forward(300)
    left(90)
    penup()
    forward(80)
    pendown()
    left(90)
    forward(300)
    right(90)
a=Turtle()
a.shape("turtle")
a.color("blue")
a.penup()
a.goto(-140,120)
a.write(player1)
a.right(360)
a.pendown()
b=Turtle()
b.shape("turtle")
b.color("maroon")
b.penup()
b.goto(-140,60)
b.write(player2)
b.right(360)
b.pendown()
c=Turtle()
c.shape("turtle")
c.color("purple")
c.penup()
c.goto(-140,0)
c.write(player3)
c.right(360)
c.pendown()
d=Turtle()
d.shape("turtle")
d.color("black")
d.penup()
d.goto(-140,-60)
d.write(player4)
d.right(360)
d.pendown()
su,sum,sw,swe=0,0,0,0
while(su<300 or sum<300 or sw<300 or swe<300):
      i=randint(1,100)
      j=randint(1,110)
      k=randint(1,120)
      l=randint(1,130)
      a.forward(i)
      su=su+i
      if(su>300):
          break
      b.forward(j)
      sum=sum+j
      if (sum > 300):
          break
      c.forward(k)
      sw=sw+k
      if (sw > 300):
          break
      d.forward(l)
      swe=swe+l
      if (swe > 300):
          break
if(su>300):
    b.ht()
    c.ht()
    d.ht()
    a.right(450)
    write("player1 wins",font=("Times",20,"bold"))
elif(sum>300):
    a.ht()
    c.ht()
    d.ht()
    b.right(450)
    write("player2 wins",font=("Times",20,"bold"))
elif(sw>300):
    a.ht()
    b.ht()
    d.ht()
    c.right(450)
    write("player3 wins",font=("Times",20,"bold"))
else:
    a.ht()
    b.ht()
    c.ht()
    d.right(450)
    write("player4 wins",font=("Times",20,"bold"))
tkinter.mainloop()