from turtle import*
fillcolor('purple')
begin_fill()
sides=5
distance=100
for _ in range(50*sides):
    distance+=20
    forward(distance)
    right(2*360.0/sides+1)
    end_fill()
