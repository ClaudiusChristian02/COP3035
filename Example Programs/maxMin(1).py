# create constants and variables
NUM_GAMES = 5
yards = 0
max = 0
min = 0
count = 1

# read 1st value & initialize min & max
yards = int(input("Enter a yardage: "))
min = yards
max = yards

while ( count < NUM_GAMES ):
    # process next value
    yards = int(input("Enter a yardage: "))
    if ( yards < min ):
        min = yards
    elif ( yards > max ):
        max = yards
    count += 1
    
# output final results
print ("Lowest was: ", min)
print ("Highest was: ", max)
print ("Now send bill to ESPN!")
