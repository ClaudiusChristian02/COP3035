#******************************************************************************#
#                                PROGRAM Simple DNA Sequences                  #
# 
# AUTHOR: <Claudius Christian>
# FSU MAIL NAME: <cc08g@my.fsu.edu>
# RECITATION SECTION NUMBER: <01>
# RECITATION INSTRUCTOR NAME: <Cassie Urmano>
# CGS 3035 - Spring 2013
# PROJECT NUMBER: 5 
# DUE DATE: Tuesday 4/8/2013
# PLATFORM: Windows OS / Python 3.3.0
#
#******************************************************************************#
#                                SUMMARY                                       #
# 
#
# First, read in a DNA sequence from a file, and store it in a Python string or
# list. Note: we will keep our sequences very short, in comparison to DNA
# sequences in real life, to make programming and grading this project simpler.
# Print the sequence you read in, to show the contents read in from the file.
# This is your original DNA sequence. Provide the user with a menu. The menu
# must allow the user to choose among four operations: 
#
# (1) Determine the complement of the original DNA sequence read in, and print
# both the original and the complement in a parallel output format, for ease of
# comparison.
#
# (2) Create 5 random simulated simple mutations in the DNA sequence. That is,
# in 5 positions your program selects pseudo-randomly, insert an "M" into the
# position to replace the A, T, G or C that was previously there. Then print
# both the original and the mutated sequence in parallel output format, again, 
# for ease of comparison.
#
# (3) Allow the user to enter a substring that he or she wants to search for in
# the original DNA sequence. For example, the user might search for a sequence
# such as "AGTCA" and find out where this sequence is located. In this program,
# you only need to find the first instance of such a substring, and report at 
# what index it was located at. If the substring is not found, you must report
# that.
#
# (4) Quit the program.  
#
#******************************************************************************#
#                                INPUT                                         #
#
# The input files provided are named dna1.txt, dna2.txt and dna3.txt and are
# available from the course web site. You may also make up your own text files
# to test. You may assume that data files are not empty, do contain one DNA
# sequence, and do not contain any data errors. You must ask the user to input
# the filename they wish to use. If the file does not open with the filename 
# they entered, keep asking them for a filename until the file does open
# successfully. 
#
#******************************************************************************#
#                                OUTPUT                                        #
#
# (1) The original DNA sequence will be displayed 
# (2) For each operation the user selects, be sure to output appropriate
# information. 
# (3) Be sure to follow all class style guidelines for all required output 
# elements and formatting principles
#
#******************************************************************************#
#                                ASSUMPTIONS                                   #
#
# If the file does not open with the filename they entered, keep asking them
# for a filename until the file does open successfully.

#******************************************************************************#
#                                Import Files                                  #

import random

#******************************************************************************#
#                                Constants                                     #

COMPLEMENT     = 1                 # stores find complement choice                 
RANDOM         = 2                 # stores create 5 random  choice                        
SEARCH         = 3                 # stores search sequence choice             
QUIT           = 4                 # stores quit choice
                                                          
#******************************************************************************#
#                                Main Function                                 #
                                                     
def main ():

    randomChange = 0

    print("Welcome to Claudius' DNA Program\n\n")
    filename = input("The filename you would like to open is: ")

    # open file
    infile = open( filename, 'r' )

    # assign file contents to line1
    line1 = infile.readline()

    # close file
    infile.close()
    

    print("Choose between the following choices by by entering 1, 2, or 3: ")
    print("1. Determine complement of the original DNA sequence.")
    print("2. Create 5 random simulated simple mutations of the DNA sequence")
    print("3. Search DNA sequence for substrings.")
    print("4. Quit.")

    #stores the users choice
    userChoice = int(input('Your choice is: '))
# ======================================
# complement option was chosen (option 1)
    if( userChoice == COMPLEMENT ):

        # calls the complement function which is option 1
        complement(line1)
# ======================================
# random dna Sequence is option 2
    elif( userChoice == RANDOM ):

        # calls the random number generator
        randomChange = randomSequence()

        # call the mutation generator 
        mutationGenerator( randomChange, line1 )
# ======================================
# search a DNA sequence (option 3)
    elif( userChoice == SEARCH ):

        # calls the search DNA function
        searchDNA( line1 )

# ======================================
# quit program (option 4)

    elif( userChoice == QUIT ):

        # print parting message
        print('\nThis program has terminated.')

# ======================================
# default
# default catch all

    else:
        # print parting message
        print('There has been an unfortunate error.')
        print('this program has terminated.\n')
            

#******************************************************************************#
#                                Complement Function                           #
#
# this function will find a nucleotide and replace it with its complement
# and print the result

def complement(l1):

    strand = ''

   # loops through string converting each letter to its complement
    for ch in l1:
        if( ch == 'A' ):
            ch ='t'
            strand += ch
        elif( ch == 'T' ):
            ch = 'a'
            strand += ch
        elif( ch == 'G' ):
            ch = 'c'
            strand += ch
        elif( ch == 'C' ):
            ch = 'g'
            strand += ch
        else:
            trand = ''
            
    # converts the lowercase to upper case 
    strand = strand.upper()

    print(l1)  
    print(strand)
    
#******************************************************************************#
#                                Random Number Function                        #
#
# this function will create a random number between 1 and 4.

def randomSequence():

    number = random.randrange( 1, 5 )
    return(number)

#******************************************************************************#
#                                Mutation Function                             #
#
# this function will create a mutated DNA sequence by replacing a random
# nucleotides with a Capital M

def mutationGenerator( num, l1 ):

    strand = ''

    for ch in l1:
        if( (num == 1) & (ch == 'A') ):
            ch = 'M'
            strand += ch
            if( ch == 'T' ):
                ch = 'T'
                strand += ch
            elif( ch == 'G' ):
                ch = 'G'
                strand += ch
            elif( ch == 'C' ):
                ch = 'C'
                strand += ch
            else:
                trand = ''        
        elif( (num == 2 ) & (ch == 'T') ):
            ch = 'M'
            strand += ch
            if( ch == 'A' ):
                ch = 'A'
                strand += ch
            elif( ch == 'G' ):
                ch = 'G'
                strand += ch
            elif( ch == 'C' ):
                ch = 'C'
                strand += ch
            else:
                    trand = ''  
        elif( (ch == 3) & (ch == 'G') ):
            ch = 'M'
            strand += ch
            if( ch == 'A' ):
                ch = 'A'
                strand += ch
            elif( ch == 'T' ):
                ch = 'T'
                strand += ch
            elif( ch == 'C' ):
                ch = 'C'
                strand += ch
            else:
                    trand = ''  
        elif( (num == 4) & (ch == 'C') ):
            ch = 'M'
            strand += ch
            if( ch == 'A' ):
                ch = 'A'
                strand += ch
            elif( ch == 'G' ):
                ch = 'G'
                strand += ch
            elif( ch == 'G' ):
                ch = 'G'
                strand += ch
            else:
                trand = ''    
        else:
            strand += ch
                   
    print(l1)
    print(strand)
     
#******************************************************************************#
#                                Search Function                               #
#
# This function enables the user to search for a particular DNA sequence, and
# find the location of that sequence if it does exist

def searchDNA(l1):

    searchQuery = input("What would you like to search for: ")

    # converts the lowercase to upper case 
    searchQuery = searchQuery.upper()

    position = l1.find( searchQuery )
    
    # determines if there are results and prints them prints the results of the
    # search
    if( position != -1):
        print('the sequence', searchQuery, 'was found at index', position)
    else:
         print('The sequence', searchQuery, 'was not found.')

    
main() 
