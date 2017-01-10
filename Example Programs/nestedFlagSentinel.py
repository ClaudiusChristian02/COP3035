# nested loop, flag outer loop, sentinel inner loop
# ask user to enter a Fahrenheit
# temperature, convert it to Celcius, then
# repeat as long as user wishes

fahrenTemp = 0    # create variables needed
celTemp = 0
response = ""
keepGoing = True

# assume user wants to convert at least
# one temperature
while keepGoing:
    # get a temp and convert it
    fahrenTemp = int(input("Enter a temperature in Fahrenheit -> "))
    celTemp = int (5.0 / 9.0  * (fahrenTemp - 32))

    print ("In Celcius that is ", celTemp)
    # ask if user wants to convert again
    print ()
    response = input ("Enter Y or N -> ")

    while (response != 'Y' and response != 'N'):
        response = input ("Please try again." +
                          " Enter Y or N -> ")
    # reset flag
    keepGoing = (response == 'Y')
    # end of while (keepGoing) loop




