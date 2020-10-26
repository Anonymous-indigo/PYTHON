#To draw a pentagon, you will obviously need to have five sides. Of coarse, you can change the size of the pentagon by adjusting how much forward you go. In this case, I have made it so that the turtle goes forward by 100 steps each time. However, you can not change the angle you turn, and changing how much times you do it is just wasting time for it to stop.
import turtle
t=turtle
for n in range(5):
  t.forward(100)
  t.right(72)