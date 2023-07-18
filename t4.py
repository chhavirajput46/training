from turtle import *
speed('fast')
colors=['red','yellow','blue','green']
pensize(2)
for i in range(100):
   # print(1%4,colors[i%4])
   pencolor(colors[i%4])
   fd(i*5)
   lt(60)
   circle(i*2,60)
mainloop()