#To draw a square, you obviously need to repeat drawing sides four times. You can make the square as big as you like, but you will need to adjust how much steps you go each time.

import turtle
t=turtle
for n in range(4):
  t.forward(100)
  t.right(90)