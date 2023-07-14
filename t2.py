from turtle import *

speed('slowest')
pencolor('red')
for i in range(0,10):#step based loop#repeating task 
#range(stop) #range(start,stop) #range(start, stop, gap/step)
    fd(100)
    lt(36) #rt right #lt left
    dot(10,"green")
    write(i, font=("calibri",20,"bold"))

#reverse
goto(100,100)
for i in range(10,0,-1):
    fd(60)
    rt(360/10)
    dot(20,"red")
    write(i, font=("calibri",20,"bold"))
mainloop()


# while n<8: conditition based #user based intrection #traversing #asyncronous codes #infinite
