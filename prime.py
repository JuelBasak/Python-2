num = int(raw_input("Enter a number :: "))
c = 0
for i in range(1,num+1):
    if num % i == 0:
        c = c + 1
if c == 2:
    print "The number is prime"
else:
    print "The number is composite" 
