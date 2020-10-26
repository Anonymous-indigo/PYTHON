#To draw a octogon, you need to have eight sides. The angle you turn must be 45 turtle steps, but the length of each angle (t.forward(#)) can be anything.
import turtle
t=turtle
for n in range(8):
  t.forward(100)
  t.right(45)