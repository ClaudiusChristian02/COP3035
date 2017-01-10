# ===========================================================================
# PROGRAM Imperial unit to metric unit conversion program 
#
# AUTHOR: <Claudius Christian>
# FSU MAIL NAME: <cc08g@my.fsu.edu>
# RECITATION SECTION NUMBER: <01>
# RECITATION INSTRUCTOR NAME: <Cassie Urmano>
# CGS 3035 - Spring 2013
# PROJECT NUMBER: 3 
# DUE DATE: Tuesday 2/19/2013
# PLATFORM: Windows OS / Python 3.3.0
# 
# SUMMARY
#
# write a menu-driven program which allows a person to type in a command and
# an English unit of measurement, and convert the measurement to its
# equivalent in Metric units. This can be quite a useful application to
# have. Such a program is often incorporated into a small hand-held
# calculator, just as a foreign language dictionary (word for word can be.  
#
# INPUT
#
# All input will be interactive. You must ask the user to enter a command,
# and a numeric value for the measurement they want to convert. For example,
# if they enter a 2 for the command, then you would ask them to enter the
# number of feet they wish to convert to meters.

# The program must allow the user to enter menu commands and numbers to
# convert, until they choose to stop. You must use 1, 2, 3, 4, 5 and 6 to
# represent the commands.
#
# OUTPUT
#
# Your output must contain a menu - that is, you need to tell the user what
# the commands are and what they mean. Prompts and error messages should be
# printed as needed, and of course, the results of the conversion which was
# performed. Don’t forget titles, headings, blank lines etc. as needed to
# make your output clear and informative. Print your real numbers to 3
# digits of precision.
#
# ASSUMPTIONS
#
# It is possible that the user may enter an invalid command, or a negative
# number of English units. Your program must check for both of these errors,
# and ask the user to re-enter a value when necessary, until a valid data
# item is entered.
#
# You should test your program with a wide variety of numeric values, some
# negative, some zero, and some positive. Also be sure to test all of the
# possible commands. The graders will also run your program to test it
# during the grading process. You may assume that the user enters a valid
# number when asked for a number (i.e. they won't type something which is
# a non-numeric value). 



# ===========================================================================
#                                constants 

INCHES_TO_CENTIMETERS = 2.5400    # used to convert 1 inche to centimeters
FEET_TO_METERS        = 0.3048    # used to convert 1 foot to meters
MILES_TO_KILOMETERS   = 1.6094    # used to convert 1 mile to kilometers
POUNDS_TO_KILOGRAMS   = 0.4536    # used to convert 1 pound to kilograms
GALLONS_TO_LITERS     = 3.7853    # used to convert 1 gallon to liters
INCHES_CHOICE         = 1         # inch conversion choice     
FEET_CHOICE           = 2         # feet conversion choice 
MILES_CHOICE          = 3         # mile conversion choice 
POUNDS_CHOICE         = 4         # pound conversion choice 
GALLONS_CHOICE        = 5         # gallon conversion choice
QUIT_CHOICE           = 6         # quit program 

                                             
# ===========================================================================
#                                Main function

def main ():
    
                                                 
# ======================================
# create variables and initialize 
                                                 
 amountToConvert      = 0.0       # holds positive real number the user wants
                                  # to convert
 conversionChoice     = 0         # holds the users choice
 finalConversion      = 0.0       # holds the converted imperial unit

                                  
# ======================================
# welcome message and menu

 print ('\n')
 print ('****************************************')
 print ('Welcome to The Metric Conversion Program')
 print ('****************************************')
 print ('\n')
 
 print ('Please choose an option from the menu below for the type of')
 print ('conversion you wish to perform. Then enter a non-negative')
 print ('number and it will be converted for you. Choose the last')
 print ('menu option (6) to quit.\n')

 print ('Choose a number from the menu.')
 print ('1. Inches to centimeters')
 print ('2. Feet to meters')
 print ('3. Miles to kilometers')
 print ('4. Pounds to kilograms')
 print ('5. Gallons to liters')
 print ('6. Quit the program\n')

# ======================================
# user menu choice

 # asks the user to input a menu choice and checks to determine if it is valid
 # if the input is invalid ask the user to reenter
 while (( conversionChoice < INCHES_CHOICE ) | ( conversionChoice >
          QUIT_CHOICE )):

     # asks the user to input an integer number and stores the input in
     # conversionChoice  
     conversionChoice = int(input('Please enter a menu choice from above: '))

# ======================================
# inches to centimeters

# This checks to see if the user choice matches the appropriate option
 if ( conversionChoice == INCHES_CHOICE ):

     # asks user to input a real number, store it in amountToConvert
     amountToConvert = float(input('Please enter the length in inches: '))
     
     # if the number entered is less than zero the program asks the user to
     # enter
     # a number greater than zero until repeatedly until the user does so
     while ( amountToConvert < 0 ):

         # promts the user to enter a number
         amountToConvert = float(input('Please enter the length in inches: '))

     # verifies the number entered is greater than zero
     if( amountToConvert >= 0 ):

         # makes the appropriate imperial unit to metric unit conversion
         finalConversion = amountToConvert * INCHES_TO_CENTIMETERS
         
         # print conversion results to four decimal places
         print( amountToConvert,'inch(es) is equivalent to %.4f'
                % finalConversion,'centimenters' )

# ======================================
# feet to meters

# This checks to see if the user choice matches the appropriate option
 elif ( conversionChoice == FEET_CHOICE ):

     # asks user to input a decimal number, store it in amountToConvert
     amountToConvert = float(input('Please enter the length in feet: '))
     
     # if the number entered is less than zero the program asks the user to
     # enter
     # a number greater than zero until repeatedly until the user does so
     while ( amountToConvert < 0 ):

         # promts the user to enter a number
         amountToConvert = float(input('Please enter the length in feet: '))

     # verifies the number entered is greater than zero
     if( amountToConvert >= 0 ):

         # makes the appropriate imperial unit to metric unit conversion
         finalConversion = amountToConvert * FEET_TO_METERS

         # print conversion results to four decimal places
         print( amountToConvert,'feet is equivalent to %.3f'
                % finalConversion,'meters' )

# ======================================
# miles to kilometers

# This checks to see if the user choice matches the appropriate option
 elif ( conversionChoice == MILES_CHOICE ): 

     # asks user to input a decimal number, store it in amountToConvert
     amountToConvert = float(input('Please enter the length in miles: '))
     
     # if the number entered is less than zero the program asks the user to
     # enter
     # a number greater than zero until repeatedly until the user does so
     while ( amountToConvert < 0 ):

         # promts the user to enter a number
         amountToConvert = float(input('Please enter the length in miles: '))

     # verifies the number entered is greater than zero
     if( amountToConvert >= 0 ):

         # makes the appropriate imperial unit to metric unit conversion
         finalConversion = amountToConvert * MILES_TO_KILOMETERS

         # print conversion results to four decimal places
         print( amountToConvert,'miles is equivalent to %.4f'
                % finalConversion,'kilometers' )

# ======================================
# convert pounds to kilograms

 # This checks to see if the user choice matches the appropriate option
 elif ( conversionChoice == POUNDS_CHOICE ): 

     # asks user to input a decimal number, store it in amountToConvert
     amountToConvert = float(input('Please enter the weight in pounds: '))
     
     # if the number entered is less than zero the program asks the user to
     # enter
     # a number greater than zero until repeatedly until the user does so
     while ( amountToConvert < 0 ):
         
         # promts the user to enter a number
         amountToConvert = float(input('Please enter the weight in pounds: '))

     # verifies the number entered is greater than zero
     if( amountToConvert >= 0 ):

         # makes the appropriate imperial unit to metric unit conversion
         finalConversion = amountToConvert * POUNDS_TO_KILOGRAMS

         # print conversion results to four decimal places
         print( amountToConvert,'pounds is equivalent to %.4f'
                % finalConversion,'kilograms' )

# ======================================
# convert gallons to liters

 # This checks to see if the user choice matches the appropriate option
 elif ( conversionChoice == GALLONS_CHOICE ): 

     # asks user to input a decimal number, store it in amountToConvert
     amountToConvert = float(input('Please enter the volume in gallons: '))

     # if the number entered is less than zero the program asks the user to
     # enter
     # a number greater than zero until repeatedly until the user does so
     while ( amountToConvert < 0 ):

         # promts the user to enter a number
         amountToConvert = float(input('Please enter the volume in gallons: '))

     # verifies the number entered is greater than zero
     if( amountToConvert >= 0 ):

         # makes the appropriate imperial unit to metric unit conversion
         finalConversion = amountToConvert * GALLONS_TO_LITERS

         # print conversion results to four decimal places
         print( amountToConvert,'gallons is equivalent to %.4f'
                % finalConversion,'liters' )

# ======================================
# quit program choice

 # This checks to see if the user choice matches the appropriate option
 elif( conversionChoice == QUIT_CHOICE ):

     # print parting message
     print('\nThis program has terminated.')

# ======================================
# default

 # default catch all
 else:
     
     # print parting message
     print('There has been an unfortunate error.')
     print('this program has terminated.\n')

     
main ()
# ===========================================================================
#                                End of program
