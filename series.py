def fun1(n):
    s = 0.0
    for i in range(1,n+1):
        s = s + 1.0/i
    print "The sum of the series is :: %.2f" %s
    
def fun2(n):
    s = 1.0
    add = 0.0
    for i in range(1,n+1):
        add = add + s 
        s = s + 2.0              
    print "The sum of the series is :: %.2f" %add

n = int(raw_input("Enter a number :: "))
fun1(n)
fun2(n)

