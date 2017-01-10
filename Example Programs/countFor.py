# print table heading once
print ("Number     Square")
print ("======     ======")

for count in range(1, 101) :
    square = count ** 2
    print ("%5d%11d" % (count, square))
