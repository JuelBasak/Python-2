num = int(raw_input("Enter a number ::"))
a = 0
b = 1
c = 0
for i in range(num):
    print c,
    a = b
    b = c
    c = a + b
