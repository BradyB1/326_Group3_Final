import sys
import argparse
import pandas as pd
'''
This program will 
'''


def UserInput():

    # What company would you like?
    # what Type
    # how many inches
    # screenResolution
    # Cpu
    # Ram
    # Memory
    # Gpu
    # OpSys
    # Weight
    # Price
    userCompany = input(
        "What company are you searching for? (if none say 'NA'")
    userCPU = input("What cpu are you looking for?")

    print(f"Cpu: {userCPU}")


def main():
    columns = ["Company", "TypeName", "ScreenResolution", "CPU",
               "ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]

    laptop_data = pd.read_csv("laptop_data.csv", names=columns)


#df = pd.read_csv("laptop_data.csv", sep='\t')
# Frame = pd.DataFrame([df], columns=["Company", "TypeName",
# "ScreenResolution", "CPU", "ram", "Memory", "Gpu", "OpSys", "Weight", "Price"])
#Frame.to_csv("laptop_data.csv", sep='\t')
columns = ["Company", "TypeName", "ScreenResolution", "CPU",
           "ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]

laptop_data = pd.read_csv("laptop_data.csv", names=columns)

# print(laptop_data.to_string())
# print(laptop_data.head())

# for i in columns[0]:
# if i == "Apple":
# print(i)

#filtered = laptop_data.loc[laptop_data["Company"] == Company]


# for i in columns:
#     if row == "Company":
#         x = i

#         if x == "Apple":
#             print(x)
#         else:
#             print("this aint working")
#         # print(i)

# if i[0] == "Company":
#     print("This is on Company")
# else:
#     print("we arent on company")
# if i == "Cpu":
#     print("This is on Cpu")

# def parse_data(column_name):
#     while column_name == columns[0]:
#         for i in column_name:
#             if i == "Apple":
#                 print(i)

# parse_data()

# def hello():
#print("Hello World")

# hello()
