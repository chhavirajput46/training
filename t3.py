from turtle import *
#library=module
speed('fastest')
pencolor('yellow')
bgcolor('#303030')
pensize(4)
i=100
while i>0:
    fd(i)
    lt(90)
    i-=4
    dot(10,"red") 
    write(i,font=("calibri",14,'bold'))
mainloop()