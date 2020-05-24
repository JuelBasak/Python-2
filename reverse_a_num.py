num = int(raw_input("Enter a number :: "))
s = 0
while num > 0:
    n = num % 10
    s = s * 10 + n
    num = num / 10

print "The reverse of the number is :: %d" %s 

