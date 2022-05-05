import turtle

fluffy = turtle.Turtle()
fluffy.shape("turtle")
park = turtle.Screen()

for i in range(3): 

   fluffy.forward(60)
   fluffy.left(120)
   fluffy.forward(60)

fluffy.forward(100)

for i in range(4):
    fluffy.forward(100)
    fluffy.left(90)
    
