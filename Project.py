# Brady Buttrey, Matthew Krivitskiy, Carlos Osorio, Luis Valderrama
# Professor Bill Farmer
# INST 326: Final Project
# 12/15/2022

import sys
import argparse
import pandas as pd
import unittest
'''
Using this software, users can input their desired laptop components and if two of more of the components match from an individual laptop, the laptop name information will be returned for the user.

'''


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
    UserPrice = input("What Price are you looking around? (if none say 'NA')")

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


def main(filename, laptop_data):
    '''
    openes and reads into the laptop_data file 
    '''
    laptop_data = pd.read_csv(filename)
    # df = pd.read_csv(filename)
    print(laptop_data)

    userDesires()


def parse_company():
    '''This function will parse the csv file to find matching company values 

    '''
    pass


def test_companyParse():
    '''This function will test if the parse_company function is working  

    '''
    pass


def parse_typeName():
    '''this function this will parse the csv file to find matching Type Name values 

    '''
    pass


def test_TypeParse():
    '''This function will test if the parse_TypeName function is working  

    '''
    pass


def parse_inches():
    '''this functino will parse the csv file to find matching inches values 
    '''
    pass


def test_inchesParse():
    '''This function will test if the parse_inches function is working  

    '''
    pass


def parse_resolution():
    '''this functino will parse the csv file to find matching resolution values 
    '''
    pass


def test_resParse():
    '''This function will test if the parse_resolution function is working  

    '''
    pass


def parse_cpu():
    '''this functino will parse the csv file to find matching cpu values 
    '''
    pass


def test_cpuParse():
    '''This function will test if the parse_cpu function is working  

    '''
    pass


def parse_ram():
    '''this functino will parse the csv file to find matching RAM values 
    '''
    pass


def test_ramParse():
    '''This function will test if the parse_ram function is working  

    '''
    pass


def parse_memory():
    '''this functino will parse the csv file to find matching memory values 
    '''
    pass


def test_memoryParse():
    '''This function will test if the parse_memory function is working  

    '''
    pass


def parse_gpu():
    '''this functino will parse the csv file to find matching gpu values 
    '''
    pass


def test_gpuParse():
    '''This function will test if the parse_gpu function is working  

    '''
    pass


def parse_opSys():
    '''this functino will parse the csv file to find matching OS values 
    '''
    pass


def test_opSysParse():
    '''This function will test if the parse_opSys function is working  

    '''
    pass


def parse_weight():
    '''this functino will parse the csv file to find matching weight values 
    '''
    pass


def test_weightParse():
    '''This function will test if the parse_weight function is working  

    '''
    pass


def parse_price():
    '''this functino will parse the csv file to find matching price range values 
    '''
    pass


def test_priceParse():
    '''This function will test if the parse_price function is working  

    '''
    pass


def matches():
    '''This function will check if at least two or more components are matching the users desires.

    returns: matching laptops
            "There are no matching laptops
    '''
    pass


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments

    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('--filename', type=str, help='Name of the file.')
    # parser.add_argument('--species', type = str, help = 'IM JUST USING THIS AS A HOLDER FOR THE MOMENT.')

    args = parser.parse_args(args_list)

    return args


if __name__ == "__main__":

    args = parse_args(sys.argv[1:])
    main(args.filename)
