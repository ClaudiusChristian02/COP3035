# print table heading once
print ("Number     Square")
print ("======     ======")
count = 1			# initialize counter

while count <= 100:
    square = count ** 2
    print ("%5d%11d" % (count, square))
    count = count + 1	# update counter
