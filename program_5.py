sub1 = int(raw_input("Enter the marks in subject 1 :: "))
sub2 = int(raw_input("Enter the marks in subject 2 :: "))
sub3 = int(raw_input("Enter the marks in subject 3 :: "))
sub4 = int(raw_input("Enter the marks in subject 4 :: "))
sub5 = int(raw_input("Enter the marks in subject 5 :: "))

percent = ((sub1 + sub2 + sub3 + sub4 + sub5) * 100) / 500

print "The percentage obtained :: %0.1f %s" % (percent,"%") 
