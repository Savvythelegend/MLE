import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Draw a square
for _ in range(4):
    my_turtle.forward(100)  # Move forward by 100 units
    my_turtle.right(90)     # Turn right by 90 degrees

# Draw a triangle
for _ in range(3):
    my_turtle.forward(100)
    my_turtle.right(120)

# Draw a circle
my_turtle.circle(100)

# Draw an oval
for _ in range(2):
    my_turtle.circle(100, 90)
    my_turtle.circle(50, 90)

# Draw a heptagon (7-sided polygon)
sides = 7
angle = 360 / sides
for _ in range(sides):
    my_turtle.forward(100)
    my_turtle.right(angle)

# Draw a rectangle
for _ in range(2):
    my_turtle.forward(200)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)

# Draw a hexagon
sides = 6
angle = 360 / sides
for _ in range(sides):
    my_turtle.forward(100)
    my_turtle.right(angle)

# Draw a star
for _ in range(5):
    my_turtle.forward(100)  # Move forward 100 units
    my_turtle.right(144)    # Turn 144 degrees to the righti

# Close the turtle window on click
turtle.Screen().exitonclick()
