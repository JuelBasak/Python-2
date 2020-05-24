def Sort():
    print "Enter 10 numbers"
    for i in range(10):
        ar.append(int(raw_input(">")))
    
    
    print "The original list is :: "
    for i in range(10):
        print "%d" % ar[i]
    
    for i in range(10):
        j = i + 1
        for j in range(10):
            if ar[i] < ar[j]:
                temp = ar[i]
                ar[i] = ar[j]
                ar[j] = temp
    
    print "The changed list is :: "
    for i in range(10):
        print "%d" % ar[i]
        
def Bsearch():
    print "Enter a number to search"
    num = int(raw_input(">"))
    lo = 0
    up = 9
    mid = 0
    while lo <= up:
        mid = (lo + up)/2
        if num < ar[mid]:
            up = mid - 1
        elif num > ar[mid]:
            lo = mid + 1
        else:
            print "The number is found at position :: %d" % (mid+1)
            return
    print "The number is not found"   
   
ar = []
Sort()            
Bsearch()
            
