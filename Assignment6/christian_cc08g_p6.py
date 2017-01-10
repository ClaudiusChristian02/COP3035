#******************************************************************************#
#                                PROGRAM Contacts Class Objects List           #
# 
# AUTHOR: <Claudius Christian>
# FSU MAIL NAME: <cc08g@my.fsu.edu>
# RECITATION SECTION NUMBER: <01>
# RECITATION INSTRUCTOR NAME: <Cassie Urmano>
# CGS 3035 - Spring 2013
# PROJECT NUMBER: 6 
# DUE DATE: Tuesday 4/23/2013
# PLATFORM: Windows OS / Python 3.3.0
#
#******************************************************************************#
#                                SUMMARY                                       #
# 
#
# Create a Contact class that can hold information and perform operations with
# contact objects. The basic idea here is that on a mobile phone, you typically
# have a contacts list or address book. The Contact class must have the
# following private data members. Note that this table provides just the basic
# "word" names, you will have to use correct Python syntax to make these private
# members in your program.  
#
# name, address, age, phone type
#
#******************************************************************************#
#                                INPUT                                         #
#
# The only input is from the data file. 
#
#******************************************************************************#
#                                OUTPUT                                        #
#
# As usual: introduction, echoprinted input, closing termination message,
# error messages as needed, and any informative messages the user may need or
# want to see
# Elements described in this write-up
# Follow the course style guidelines
#
#******************************************************************************#
#                                ASSUMPTIONS                                   #
#
# You may assume the file data is completely correct and you do not have to do
# any error checking on file contents. You may assume that the number of
# contacts specified in the file is an integer between 1 and 5.

#******************************************************************************#
#                                Class                                         #

class Contact:

    def __init__(self, name, address, age, phone, relation):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
        self.__relation = relation

#*****************
# set functions
#*****************

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def set_relation(self, relation):
        self.__relation = relation

#*****************
# get functions
#*****************

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age
    
    def get_phone(self):
        return self.__phone

    def get_relation(self):
        return self.__relation

#*****************
# STR Function
#*****************

    def __str__(self):
        return 'The name is ' + slef.__name
        return 'The address is ' + slef.__address
        return 'The age is ' + slef.__age
        return 'The phone is ' + slef.__phone
        return 'The relation is ' + slef.__relation
        

#******************************************************************************#
#                                Constants                                     #

ONE_CONTACTS   = 1                 # for the number of possible total contacts
TWO_CONTACTS   = 2                 # for the number of possible total contacts
THREE_CONTACTS = 3                 # for the number of possible total contacts                 
FOUR_CONTACTS  = 4                 # for the number of possible total contacts                       
FIVE_CONTACTS  = 5                 # for the number of possible total contacts             

                                                          
#******************************************************************************#
#                                Main Function                                 #


def main ():

    age = 0
    address = 'empty'
    name = 'empty'
    numContacts = 0
    phone = 'empty'
    relation = 'empty'
    
    print("Welcome to Claudius' Phone Book Program\n\n")
    filename = input("The filename you would like to open is: ")

    # Open file
    infile = open( filename, 'r' )

    # Read in total number of contacts in the file
    numContacts = int(infile.readline())
    print('total contacts are:', numContacts )

    # For one contacts
    if( numContacts == TWO_CONTACTS ):

        # create three objects from the Contact class
        contact1 = Contact(name, address, age, phone, relation)

        # Read in contact 1 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 1 information
        contact1.set_name( name )
        contact1.set_address( address )
        contact1.set_age( age )
        contact1.set_phone( phone )
        contact1.set_relation( relation )

        # Print contact 1 information
        print('\nContact one information: ')
        print('the name is:', contact1.get_name())
        print('the address is:', contact1.get_address())
        print('the age is:', contact1.get_age())
        print('the phone is:', contact1.get_phone())
        print('the relation is:', contact1.get_relation())

    # For two contacts
    elif( numContacts == TWO_CONTACTS ):

        # create three objects from the Contact class
        contact1 = Contact(name, address, age, phone, relation)
        contact2 = Contact(name, address, age, phone, relation)

        # Read in contact 1 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 1 information
        contact1.set_name( name )
        contact1.set_address( address )
        contact1.set_age( age )
        contact1.set_phone( phone )
        contact1.set_relation( relation )

        # Read in contact 2 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 2 information
        contact2.set_name( name )
        contact2.set_address( address )
        contact2.set_age( age )
        contact2.set_phone( phone )
        contact2.set_relation( relation )

        # Print contact 1 information
        print('\nthe name is:', contact1.get_name())
        print('the address is:', contact1.get_address())
        print('the age is:', contact1.get_age())
        print('the phone is:', contact1.get_phone())
        print('the relation is:', contact1.get_relation())

        # Print contact 2 information
        print('the name is:', contact2.get_name())
        print('the address is:', contact2.get_address())
        print('the age is:', contact2.get_age())
        print('the phone is:', contact2.get_phone())
        print('the relation is:', contact2.get_relation())

    # For three contacts
    elif( numContacts == THREE_CONTACTS ):

        # create three objects from the Contact class
        contact1 = Contact(name, address, age, phone, relation)
        contact2 = Contact(name, address, age, phone, relation)
        contact3 = Contact(name, address, age, phone, relation)

        # Read in contact 1 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 1 information
        contact1.set_name( name )
        contact1.set_address( address )
        contact1.set_age( age )
        contact1.set_phone( phone )
        contact1.set_relation( relation )

        # Read in contact 2 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 2 information
        contact2.set_name( name )
        contact2.set_address( address )
        contact2.set_age( age )
        contact2.set_phone( phone )
        contact2.set_relation( relation )

        # Read in contact 3 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 3 information
        contact3.set_name( name )
        contact3.set_address( address )
        contact3.set_age( age )
        contact3.set_phone( phone )
        contact3.set_relation( relation )

        # Print contact 1 information
        print('\nthe name is:', contact1.get_name())
        print('the address is:', contact1.get_address())
        print('the age is:', contact1.get_age())
        print('the phone is:', contact1.get_phone())
        print('the relation is:', contact1.get_relation())

        # Print contact 2 information
        print('the name is:', contact2.get_name())
        print('the address is:', contact2.get_address())
        print('the age is:', contact2.get_age())
        print('the phone is:', contact2.get_phone())
        print('the relation is:', contact2.get_relation())

        # Print contact 3 information
        print('the name is:', contact3.get_name())
        print('the address is:', contact3.get_address())
        print('the age is:', contact3.get_age())
        print('the phone is:', contact3.get_phone())
        print('the relation is:', contact3.get_relation())

    # For four contacts
    elif( numContacts == FOUR_CONTACTS ):

        # create four objects from the Contact class
        contact1 = Contact(name, address, age, phone, relation)
        contact2 = Contact(name, address, age, phone, relation)
        contact3 = Contact(name, address, age, phone, relation)
        contact4 = Contact(name, address, age, phone, relation)

        # Read in contact 1 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 1 information
        contact1.set_name( name )
        contact1.set_address( address )
        contact1.set_age( age )
        contact1.set_phone( phone )
        contact1.set_relation( relation )

        # Read in contact 2 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 2 information
        contact2.set_name( name )
        contact2.set_address( address )
        contact2.set_age( age )
        contact2.set_phone( phone )
        contact2.set_relation( relation )

        # Read in contact 3 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 3 information
        contact3.set_name( name )
        contact3.set_address( address )
        contact3.set_age( age )
        contact3.set_phone( phone )
        contact3.set_relation( relation )

        # Read in contact 4 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 4 information
        contact4.set_name( name )
        contact4.set_address( address )
        contact4.set_age( age )
        contact4.set_phone( phone )
        contact4.set_relation( relation )

        # Print contact 1 information
        print('\nthe name is:', contact1.get_name())
        print('the address is:', contact1.get_address())
        print('the age is:', contact1.get_age())
        print('the phone is:', contact1.get_phone())
        print('the relation is:', contact1.get_relation())

        # Print contact 2 information
        print('the name is:', contact2.get_name())
        print('the address is:', contact2.get_address())
        print('the age is:', contact2.get_age())
        print('the phone is:', contact2.get_phone())
        print('the relation is:', contact2.get_relation())

        # Print contact 3 information
        print('the name is:', contact3.get_name())
        print('the address is:', contact3.get_address())
        print('the age is:', contact3.get_age())
        print('the phone is:', contact3.get_phone())
        print('the relation is:', contact3.get_relation())

        # Print contact 4 information
        print('the name is:', contact4.get_name())
        print('the address is:', contact4.get_address())
        print('the age is:', contact4.get_age())
        print('the phone is:', contact4.get_phone())
        print('the relation is:', contact4.get_relation())

    # For five contacts
    elif( numContacts == FIVE_CONTACTS ):

        # create five objects from the Contact class
        contact1 = Contact(name, address, age, phone, relation)
        contact2 = Contact(name, address, age, phone, relation)
        contact3 = Contact(name, address, age, phone, relation)
        contact4 = Contact(name, address, age, phone, relation)
        contact5 = Contact(name, address, age, phone, relation)

        # Read in contact 1 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 1 information 
        contact1.set_name( name )
        contact1.set_address( address )
        contact1.set_age( age )
        contact1.set_phone( phone )
        contact1.set_relation( relation )

        # Read in contact 2 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 2 information 
        contact2.set_name( name )
        contact2.set_address( address )
        contact2.set_age( age )
        contact2.set_phone( phone )
        contact2.set_relation( relation )

        # Read in contact 3 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 3 information 
        contact3.set_name( name )
        contact3.set_address( address )
        contact3.set_age( age )
        contact3.set_phone( phone )
        contact3.set_relation( relation )

        # Read in contact 4 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 4 information 
        contact4.set_name( name )
        contact4.set_address( address )
        contact4.set_age( age )
        contact4.set_phone( phone )
        contact4.set_relation( relation )

        # Read in contact 5 infomation
        name = infile.readline()
        address = infile.readline()
        age = infile.readline()
        phone = infile.readline()
        relation = infile.readline()

        # Assign contact 5 information 
        contact5.set_name( name )
        contact5.set_address( address )
        contact5.set_age( age )
        contact5.set_phone( phone )
        contact5.set_relation( relation )

        # Print contact 1 information
        print('\nthe name is:', contact1.get_name())
        print('the address is:', contact1.get_address())
        print('the age is:', contact1.get_age())
        print('the phone is:', contact1.get_phone())
        print('the relation is:', contact1.get_relation())

        # Print contact 2 information
        print('the name is:', contact2.get_name())
        print('the address is:', contact2.get_address())
        print('the age is:', contact2.get_age())
        print('the phone is:', contact2.get_phone())
        print('the relation is:', contact2.get_relation())

        # Print contact 3 information
        print('the name is:', contact3.get_name())
        print('the address is:', contact3.get_address())
        print('the age is:', contact3.get_age())
        print('the phone is:', contact3.get_phone())
        print('the relation is:', contact3.get_relation())

        # Print contact 4 information
        print('the name is:', contact4.get_name())
        print('the address is:', contact4.get_address())
        print('the age is:', contact4.get_age())
        print('the phone is:', contact4.get_phone())
        print('the relation is:', contact4.get_relation())
        
        # Print contact 5 information
        print('the name is:', contact5.get_name())
        print('the address is:', contact5.get_address())
        print('the age is:', contact5.get_age())
        print('the phone is:', contact5.get_phone())
        print('the relation is:', contact5.get_relation())

    else:

        # print error message
        print('There are either < 3 contacts or > 5. The assignment ' + \
                'there would be between 3 and 5.')

    # close file
    infile.close()

    # Print closing message
    print('\nThe program has closed normally.')
    
main()

#******************************************************************************#
#                                E N D   O F   P R O G R A M                   #
