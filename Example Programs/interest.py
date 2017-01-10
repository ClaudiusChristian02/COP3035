# create constants and variables
MONTHS_PER_YEAR = 12
GOAL_FACTOR = 2.0

month = 0           	# for counting loop - count months

originalAmt = 0.0
balance = 0.0
annualRate = 0.0
goalBalance = 0.0	# why are these 2 needed?
monthlyRate = 0.0

# read in initial data
originalAmt = float(input("Enter the original amount deposited -> "))
annualRate = float(input("Enter the annual interest rate -> "))

# initialize variables needed
balance = originalAmt
goalBalance = GOAL_FACTOR * originalAmt
monthlyRate = (annualRate / MONTHS_PER_YEAR) / 100.0

while balance < goalBalance:
    balance = balance + (monthlyRate * balance)
    month = month + 1   

# output result
print ("Number of months to at least double: ", month)
