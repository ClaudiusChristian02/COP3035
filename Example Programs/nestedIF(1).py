# ##############################################################################
# PROGRAM NestedIf Example
#
# AUTHOR: A. Ford Tyson
# Example program for use in lecture
#
# The purpose of this program is to illustrate the use of a nested if
# statement, as well as other concepts appropriate at this point in the
# course. The program will be discussed and demonstrated during lecture.
#
# SUMMARY
#
# This program takes as input a character code representing an 
# arithmetic operation (either '+', '-', '*' or '/') and two double 
# values. It then calculates the floating point result of the chosen
# operation when performed on the two input values, simulating a
# simple calculator.
#
# INPUT
#
# This program uses as input the standard input stream in Python,
# the keyboard. The character code and numeric values are prompted for 
# and read in interactively. The numeric values must be entered as valid
# real numbers or integers for the program to work correctly.  
#
# BAD DATA CHECKING: The character code entered is tested. If it is not
# a valid operator, the program does not perform any calculations, and
# a message indicating an invalid operator is printed. In addition, if
# division is requested, the denominator is checked, and division
# performed only if the denominator is non-zero.
#
# OUTPUT
#
# - echoprinted operator code and the two numeric operands
# - operation result if calculated, as a floating point value with 3 digits 
#   after the decimal point
# - error messages, if any (invalid operator, division by zero)
#
# ASSUMPTIONS
#
# - that the user enters valid numeric data for the two operands
# ##############################################################################

def main ():

    # create variables and initialize
    code = ''           # code representing an arithmetic operation
    x = 0.0	        # the first operand
    y = 0.0             # second operand			        
    result = 0.0        # the result of the operation requested
    haveResult = True   # a flag: true if the calculation
                        # can be performed
	
    # print the introductory output title
    print ("*******************************************************")
    print ("                 Calculator Program")
    print ("*******************************************************\n")
	
    # interactively read in an operation code and the two numeric operands
    code = input("Enter an operation code, +, - , *, or / => ")
    x = float(input("\nEnter the first operand => "))
    y = float(input("\nEnter the second operand => "))
 
    # do the calculation requested if possible	
    # the flag haveResult was initialized to True earlier
    # we have 5 "CASES" to handle here, 4 operators and invalid operator
    if code == '+':                 # addition
        result = x + y
    elif code == '-':               # subtraction
        result = x - y
    elif code == '*':               # multiplication
        result = x * y
    elif code == '/':               # do floating point division if safe
        if y != 0.0:                # check for attempt to divide by zero
            result = x / y
        else:   # handler for attempt to divide by zero
            print ("Sorry, we can't divide by zero!")
            haveResult = False      # reset flag to signal the error									/* failed */
    else:       # handler for invalid operator								/* user typed in an */								/* invalid operation code */
        print ("Sorry, the operator is not valid!  ")
        haveResult = False          # reset flag to signal the error

    # print a calculated result only if there is one
    if haveResult:
        print ("\nThe result is: %.3f" % result)
    else:
        print ("Error: no result can be calculated.")
		
    # print a closing message
    print ("\n<-- Program Execution Terminated -->")

# call the main function to start program execution
main()
	
# ##############################################################################
#                             END OF PROGRAM
# ##############################################################################
