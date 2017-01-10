# =================================================================================================
# PROGRAM Software Sales 
#
# AUTHOR: <Claudius Christian>
# FSU MAIL NAME: <cc08g@my.fsu.edu>
# RECITATION SECTION NUMBER: <7>
# RECITATION INSTRUCTOR NAME: <Cassie Urmano>
# CGS 3035 - Spring 2013
# PROJECT NUMBER: 2 
# DUE DATE: Tuesday 2/5/2013
# PLATFORM: Windows OS / Python 3.3.0
# 
# SUMMARY
#
# A software company sells a package that retails for $99.00.
# Quantity discounts are given according to the following table:
#
# Quantity    Discount 
# 10-19          20% 
# 20-49          30% 
# 50-99          40% 
# 100 or more    50% 
#
# Write a program that asks the user to enter the number of units
# sold (as a whole number) and calculates the total cost of the
# purchase.  Output the cost per unit after the discount is
# calculated, as well as the total price of the whole sale.  
#
# INPUT
#
# The Program must write friendly and informative prompts to ask
# the user for input and as you run it, you will type in the input
# yourself. You will also print out well-formatted, clear output
# for the user.
# 
# Input Validation: Make sure the number of units input is greater
# than zero.  If it is less than or equal to zero, do not calculate
# a discount or a cost, and simply exit the program. See below for
# more information.
#
# OUTPUT
#
# The program prints an output title, echoprints the user's input in
# a readable fashion, and then prints out the calculated results.
#
# ASSUMPTIONS
#
# Assume that the user types in a valid integer. If the
# user types in a zero or negative value, consider that bad data,
# print a message to that effect, and do not do any calculations. 



# =================================================================================================
#                                constants 

NO_DISCOUNT             = 1      # used for purchases of quanities of 1-9
TWENTY_PERCENT_DISCOUNT = 0.2    # used for purchases of quanities of 10-19
THIRTY_PERCENT_DISCOUNT = 0.3    # used for purchases of quanities of 20-49
FORTY_PERCENT_DISCOUNT  = 0.4    # used for purchases of quanities of 50-99
FIFTY_PERCENT_DISCOUNT  = 0.5    # used for purchases of quanities of 100 or more
COST_PER_UNIT           = 99     # retail price for the software

def main ():

# =================================================================================================
#                                create variables and initialize

 purchaseQuantity     = 0.0     # user input
 purchaseSubTotal     = 0.0     # hold the purchase total before applying the discount
 totalAfterDiscount   = 0.0     # hold the purchase total after applying the discount
 effectiveCostPerUnit = 0.0     # hold the cost per unit after applying the discount
 haveResult           = False   # a flag: false if the calculation cannot be performed

# =================================================================================================
#                                print an output title

 # print an output title
 print ('\n')
 print ('=========================================')
 print ('Welcome to the Steam Punk Software Store ')
 print ('=========================================')
 print ('\n')   

 # asks the user to enter the number of units sold as a whole number
 purchaseQuantity = int(input('Please enter enter the number of units sold as a whole number: \n'))

 # make sure the number of units input is greater than zero
 if purchaseQuantity > 0.0:

     # change have result setting
     haveResult = True

     if( (purchaseQuantity > 0) & (purchaseQuantity <= 9) ):

         # calculate the total cost of the purchase
         purchaseSubTotal = purchaseQuantity * COST_PER_UNIT

         # calculate the total after the discount has been applied
         totalAfterDiscount = purchaseSubTotal

         # calculate the the price per unit after applying the discount
         effectiveCostPerUnit = totalAfterDiscount / NO_DISCOUNT

     # for a purchase quantity between 10 and 19
     if( (purchaseQuantity >= 10) & (purchaseQuantity <= 19) ): 

         # calculate the total cost of the purchase
         purchaseSubTotal = purchaseQuantity * COST_PER_UNIT

         # calculate the total after the discount has been applied
         totalAfterDiscount = purchaseSubTotal - ( purchaseSubTotal * TWENTY_PERCENT_DISCOUNT )

         # calculate the the price per unit after applying the discount
         effectiveCostPerUnit = totalAfterDiscount / purchaseQuantity

     # for a purchase quantity between 20 and 49    
     if( (purchaseQuantity >= 20) & (purchaseQuantity <= 49) ):

         # calculate the total cost of the purchase
         purchaseSubTotal = purchaseQuantity * COST_PER_UNIT

         # calculate the total after the discount has been applied
         totalAfterDiscount = purchaseSubTotal - ( purchaseSubTotal * THIRTY_PERCENT_DISCOUNT )

         # calculate the the price per unit after applying the discount
         effectiveCostPerUnit = totalAfterDiscount / purchaseQuantity

     # for a purchase quantity between 50 and 99
     if( (purchaseQuantity >= 50) & (purchaseQuantity <= 99) ):

         # calculate the total cost of the purchase
         purchaseSubTotal = purchaseQuantity * COST_PER_UNIT

         # calculate the total after the discount has been applied
         totalAfterDiscount = purchaseSubTotal - ( purchaseSubTotal * FORTY_PERCENT_DISCOUNT )

         # calculate the the price per unit after applying the discount
         effectiveCostPerUnit = totalAfterDiscount / purchaseQuantity

     # for a purchase quantity greater than 99
     if( purchaseQuantity >= 100 ):

         # calculate the total cost of the purchase
         purchaseSubTotal = purchaseQuantity * COST_PER_UNIT

         # calculate the total after the discount has been applied
         totalAfterDiscount = purchaseSubTotal - ( purchaseSubTotal * FIFTY_PERCENT_DISCOUNT )

         # calculate the the price per unit after applying the discount
         effectiveCostPerUnit = totalAfterDiscount / purchaseQuantity

 # If it is less than or equal to zero, do not calculate a discount or a cost, and simply exit the program
 else:
     
     # pring error message
     print('Units sold must be greater than zero. The program has ended normally \n')

 if haveResult:

     # echoprint the user's input
     print('Total units were sold were ',purchaseQuantity)

     # print the effective cost per unit
     print("Your effective cost per unit is $%.2f" % effectiveCostPerUnit)

     # output the total price of the whole sale
     print("The total cost of the purchase is $%.2f" % totalAfterDiscount)


# call the main function to start program execution
main ()

# =================================================================================================
#                                end of the program




