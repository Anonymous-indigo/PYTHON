#To draw a hexagon, you need to go right or right 60 degrees each time you turn. You obviously need to have six sides, so repeat it six times. To change the size of the hexagon, you change how many turtle steps you go each time.
import turtle
t=turtle
for n in range(6):
  t.forward(100)
  t.right(60)