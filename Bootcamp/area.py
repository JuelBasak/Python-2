print "Enter the shape to calcualte its area"
print "1. Square"
print "2. Circle"
print "3. Rectangle"
choice = input("->")

if choice == 1:
    side = input("Enter the side :: ")
    area = side * side
elif choice == 2:
    radius = input("Enter the radius :: ")
    area = 3.14 * (radius**2)
elif choice == 3:
    length = input("Enter the length :: ")
    breadth = input("Enter the breadth :: ")
    area = length * breadth 
print "The area is :: %0.2f" % area
