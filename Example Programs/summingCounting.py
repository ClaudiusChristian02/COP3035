# create constants and variables
QUIT_CODE = -1
score = 0
numScores = 0
sum = 0
mean = 0

# priming read
score = int(input ("Enter a score (-1 to quit): "))
while score != QUIT_CODE:
    sum = sum + score
    numScores += 1
    score = int(input ("Enter a score: "))
    
# calculate mean and print
mean = sum / numScores
print ("Mean is: ", mean)
