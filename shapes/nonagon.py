#To draw a nonagon, you need to have nine sides. Each angle also needs to be 40 degrees. To change the size, change how much turtle steps you go each time creating a side. That does not affect the angle.
import turtle
t=turtle
for n in range(9):
  t.forward(100)
  t.right(40)