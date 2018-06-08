from turtle import *

colors = ["red","blue","brown","yellow","grey"]

# for i in range(5):
#     pencolor(colors[i])
#     for _ in range(i+3):
#         forward(50)
#         left(360/(i+3))

for i in range(4):
    fillcolor(colors[i])
    pencolor(colors[i])
    begin_fill()
    for _ in range(4):
        forward(100)
        left(90)
    forward(50)
    end_fill()
fillcolor(colors[4])
pencolor(colors[4])
begin_fill()
for _ in range(2):
    forward(50)
    left(90)
    forward(100)
    left(90)
end_fill()

mainloop()