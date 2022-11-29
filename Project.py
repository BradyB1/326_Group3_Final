import sys
import argparse
import pandas as pd
import unittest


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


def parse_company():
    pass


def parse_typeName():
    pass


def parse_inches():
    pass


def parse_resolution():
    pass


def parse_rpu():
    pass


def parse_ram():
    pass


def parse_memory():
    pass


def parse_gpu():
    pass


def parse_opSys():
    pass


def parse_weight():
    pass


def parse_price():
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
