# Brady Buttrey, Matthew Krivitskiy, Carlos Osorio, Luis Valderrama
# Professor Bill Farmer
# INST 326: Final Project
# 12/15/2022

# for ease of copy paste
#UserCompany, UserTypeName, UserInches, UserResolution, UserCpu, UserRam, UserMemory, UserGpu, UserOpSys, UserWeight, UserPrice

import sys
import argparse
import pandas as pd
import re
import unittest
'''
Using this software, users can input their desired laptop components and if two of more of the components match from an individual laptop, the laptop ID# along with the matching specs will be returned for the user.

'''
# NEED 1 class and 8 methods

# order
# 1: SearchOption()
# 2:
# if by specs -> UserDesires() -> PriceConversion-> Matches()
# Matches needs to create list of matching laptop objects
# after creating laptop objects -> write all objects in list to a txt file to make it easily readable
# if by Price -> --New Function here-- -> PriceConversion -> Decending_Price_display()
# i think we need a stand alone function to ask for price with this method of searching since they don't need the whole list of specs.

# Two options:
# 1 Price Order
# low to high OR high to low
# Price Range
# if user inputs 1200
# display everything +- $x

# for this we need
# def price_range: ask user price range (make it +- $x)
# def price_option = low to high or high to low within price range. ----------- FIGURE OUT HOW TO CREATE THE PRICE RANGE WITH THE USERS PRICE
# def price_option: asks the user how the want to have the laptops displayed
# def price_display: function to display the way the user wants depending on input of price_option


# def Price_Matches: function to search for all matching laptops within the given price range. Also make those Laptops an object and append them to a list.
# Possibly combine these two into one function
# def write_to_file: Write the matching Laptop Objects inside the list to a txt file. Likly using a loop to iterate through the list. for example. for i in objectList:

# 3
#

def SearchOption():
    '''This function will ask the user if they want to search by specs or price alone.'''
    searchBy = input(
        "Would you like to search by specs or by price? (Please enter 'specs' or 'price)\n")

    if searchBy not in ["Specs", "specs", "Price", "price"]:
        raise ValueError("You must enter a valid response")
    elif searchBy == "specs" or "Specs":
        userDesires()
    elif searchBy == 'price' or "Price":
        descending_price_display()


def descending_price_display(laptop_data):
    '''This function works to display the prices in decending order (lowest -> highest)'''
    laptop_data.sort_values(laptop_data.columns[11],
                            axis=0,
                            ascending=[False],
                            inplace=True)

    # displaying sorted data frame
    print(laptop_data)


def ascending_price_display(laptop_data):
    '''This function works to display the prices in ASCENDING order (lowest -> highest)'''
    laptop_data.sort_values(laptop_data.columns[11],
                            axis=0,
                            ascending=[True],
                            inplace=True)

    # displaying sorted data frame
    print(laptop_data)


def price_range():
    '''This function will collect the users price and create a price range'''
    # Need to figure out how to create that actual price range with a method
    #
    #
    dollar_range = 200
    dollar_amount = input("What price would you like to search around?")
    Price = int(dollar_amount) / .0121
    print(
        f"Searching for Laptops around {Price} dollars and diplaying Laptops within +-{dollar_range}")

    return Price


def price_option():
    '''This fuction with ask the upser how they want the laptops displayed (ascending or decending)'''
    display_choice = input(
        "Would you like it displayed in descending or , or ascending order? \nPlease only enter descending or ascending")

    return display_choice


def price_display():
    '''This function displays the price output based on the users desire'''
    if price_option() in ["descending", "Descending"]:
        descending_price_display()  # call descending display function
    elif price_option() in ["ascending", "Ascending"]:
        ascending_price_display()  # call ascending display function
    else:
        raise ValueError(
            "You must enter either 'descending', 'Descending', 'ascending', or 'Ascending'")


def price_matches(laptop_data):
    '''This function will search for all matching laptops within the given price range. Also make those Laptops an object and append them to a list.'''
    PriceLaptops = []
    # ask Sai how to create the loop for this.
    pass


class Laptop():
    '''this class will be the laptop objects created from matching laptops'''

    def __init__(self, company, typeName, inches, resolution, cpu, ram, memory, gpu, opSys, weight, price):
        self.company = company
        self.typeName = typeName
        self.inches = inches
        self.resolution = resolution
        self.cpu = cpu
        self.ram = ram
        self.memory = memory
        self.gpu = gpu
        self.opSys = opSys
        self.weight = weight
        self.price = price


def userDesires():
    '''This function will take the user desire/inputed components
Args:
    UserCompany(str): users desired company
    UserTypeName (str): users desired laptop type
    UserInches(str): users desired screen length in inches
    UserResolution(str):Users desired screen resolution
    UserCpu (str): users desired Cpu
    UserRam(str): users desired amount of RAM
    UserMemory(str):users desired storage memory amount
    UserGpu(str):users desired GPU
    UserOpSys(str): Users desired operating system
    UserWeight(str): Users desired laptop weight
    Userprice(str): Users desired price

returns: userInput

    '''

    # This list will hold the values of the user input
    specs = []

    UserCompany = input(
        "What company are you searching for? (if none say 'NA')")

    UserTypeName = input("What type are you looking for? (if none say 'NA')")

    UserInches = input(
        "How many Inches would you like the screen? (if none say 'NA')")

    UserResolution = input(
        "What Screen resolution are you looking for? (if none say 'NA')")

    UserCpu = input("What cpu are you looking for? (if none say 'NA')")

    UserRam = input("How much Ram are you looking for? (if none say 'NA')")

    UserMemory = input(
        "How much storage memory(please specify amount and type SSD, HDD, or flash storage )")

    UserGpu = input("What Gpu are you looking for? (if none say 'NA')")

    UserOpSys = input(
        "What Operating System are you looking for? (if none say 'NA')")

    UserWeight = input("What Weight are you looking for? (if none say 'NA')")

    dollarAmount = input(
        "What Price are you looking around? (if none say 'NA')")
    # make this its own conversion function
    # add budget/price range instead of hard price
    # display it from high to low
    # conversion from USD to INR

    # create array and append these to it

    # Series of if/else statements to check if the value is equal to something other then NA.
    # if NA pop it off the list
    # else append it to the list
    if UserCompany not in ["NA", "na", 'None', 'none']:
        specs.append(UserCompany)

    if UserTypeName not in ["NA", "na", 'None', 'none']:
        specs.append(UserTypeName)

    if UserInches not in ["NA", "na", 'None', 'none']:
        specs.append(UserInches)

    if UserResolution not in ["NA", "na", 'None', 'none']:
        specs.append(UserResolution)

    if UserCpu not in ["NA", "na", 'None', 'none']:
        specs.append(UserCpu)

    if UserRam not in ["NA", "na", 'None', 'none']:
        specs.append(UserRam)

    if UserMemory not in ["NA", "na", 'None', 'none']:
        specs.append(UserMemory)

    if UserGpu not in ["NA", "na", 'None', 'none']:
        specs.append(UserGpu)

    if UserOpSys not in ["NA", "na", 'None', 'none']:
        specs.append(UserOpSys)

    if UserWeight not in ["NA", "na", 'None', 'none']:
        specs.append(UserWeight)

    return specs

    # Make this a Userdisplay method


def UserDisplay(UserCompany, UserTypeName, UserInches, UserResolution, UserCpu, UserRam, UserMemory, UserGpu, UserOpSys, UserWeight, UserPrice):
    '''This will display what the user inputs '''
    print(f"Company desired: {UserCompany}")

    print(f"Type: {UserTypeName}")

    print(f"Inches: {UserInches}")

    print(f"Screen Resolution: {UserResolution}")

    print(f"Cpu: {UserCpu}")

    print(f"Ram: {UserRam}")

    print(f"Storage Memory: {UserMemory}")

    print(f"Gpu: {UserGpu}")

    print(f"Operating system: {UserOpSys}")

    print(f"Laptop Weight: {UserWeight}")

    print(f"Price Range: {UserPrice}")


# class TestBot(unittest.TestCase):

    # pass


def matches(specs, laptop_data):
    '''This function will check if at least two or more components are matching the users desires.

    returns: matching laptops
            "There are no matching laptops
    '''
    output = []
    spec_count = 0

    for row in laptop_data:
        for column in row:
            if column in specs:
                spec_count += 1
    if spec_count >= 2:
        laptop = Laptop(row[0], row[1], row[2], row[3], row[4],
                        row[5], row[6], row[7], row[8], row[9], row[10], row[11])

        # need to make sure Laptop objects are correctly created.
        # need to write the list of Laptop objects to a Txt file.
        # Might want to find a way to include Laptop ID

    return output


# CODE TO SHOW ASCENDING PRICES

def main(filename, laptop_data):
    '''
    openes and reads into the laptop_data file 
    '''
    laptop_data = pd.read_csv(filename)
    # df = pd.read_csv(filename)
    print(laptop_data)


if __name__ == "__main__":
    # userDesires()
    #args = parse_args(sys.argv[1:])
    # main(args.filename)
