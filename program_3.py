print "This is the program that is used to find out the simple interest"

p = float(raw_input("Enter the principle :: "))
r = float(raw_input("Enter the rate :: "))
t = float(raw_input("Enter the time :: "))

si = (p * t * r) / 100
amt = p + si

print "The simple interest is :: ", si
print "The amount calculated is :: ", amt   
