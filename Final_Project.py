""" 
Driver: Mujahid Syed, Tim Scott, George Chen, Jeremy Yee
Assignment: Team 11 Project
Date: 11/28/2022
INST326-ESG1 Farmer Fall 2022
"""
'''
Purpose: 
    - To look up the cost of specific medicaid drugs using data from a source. Initially we hoped to use web scraping for this, however given the complexity
        we needed to find an alternate source.

Challenges
    - Originally our plan was to compare product's prices from two different website, but due to the time constraint we did an alternative program.
    - Difficulty reading csv file from the medicaid website
    - csv file does not contain price values. The NCPDP Billing unit Standard fact sheet explains the pricing unit for each medicine 
    - 

'''
import argparse
import sys
import pandas as pd

def Dataframe():
    '''
    Functionality:
        - A function that takes data from a csv url and converts it into a dataframe

    Return:
        - a dataframe call Medicines  
    '''
    ## read csv file using pandas ##
    Medicines = pd.read_csv("https://download.medicaid.gov/data/nadac-national-average-drug-acquisition-cost-12072022.csv")
    return (Medicines)

def Cleanframe(dataframe):
    '''
    Functionality:
        - A function that cleans the dataframe of unnecessary columns by removing columns from the original dataframe

    Arguments: 
        - dataframe: Dataframe containing items and their prices of NDC
    
    Returns:
        - cleaned_dataframe: A cleaned dataframe

    '''
    ## selected columns that are deemed unnecessary ##
    cols = [3,5,6,7,8,9,10,11]
    ## remove columns from the dataframe ##
    cleaned_dataframe = dataframe.drop(dataframe.columns[cols], axis = 1)
    return cleaned_dataframe

def Uniquefilter(duplicates):
    '''
    Functionality:
        - A function that filters duplicate rows so only unquie rows remain in the dataframe

    Argument:
        - dupliates: identical rows in the dataframe

    Returns:
        - Unique_Frame: A dataframe with only unique rows
    '''
    ## drop duplicate rows in the dataframe ##
    Unique_Frame = duplicates.drop_duplicates(subset = "NDC Description")
    return Unique_Frame

def MedicineOutput(MedicineFrame, Medicine):
    '''
    Functionality:
        - A function stores the NDC description 

    Arguments:
        - MedicineFrame: 
        - Medicine: Dataframe of national drug data
    
    Return:
        - Specific_Medicine: Dataframe of specific medicine
    '''
    print(MedicineFrame)
    ## stores ndc description as a string 
    Specific_Medicine = MedicineFrame[MedicineFrame["NDC Description"].str.contains(Medicine)]
    return Specific_Medicine

def FileWriter(dataframe):
    '''
    Functionality:
        - A function that writes information to a text file using the dataframe argument
    
    Argument
        - dataframe: dataframe containing items and their prices of NDC
    
    Returns: 
        - txt file containing dataframe
    '''
    # open file "output.txt" with variable in write mode
    with open('Medput.txt', 'w') as f:
        f.write(dataframe)

def string_writer(dataframe):
    '''
    Functionality:
        - A function that covert dataframe to a list 

    Argument:
        - dataframe: dataframe containing items and their prices of NDC

    Return:
        - Medicine_List: A list of medicines 
    '''
    ## method to convert other data types into strings
    Medicine_List = dataframe.to_string()
    print("This is from string writer")
    #print(Medicine_List)
    return Medicine_List


def main(primary):
    '''
    Functionality:
        - Create an instance of the server-class using the created functions and save them to corresponding variables
    
    Argument:
        - primary: Command-line arguments for the program

    Return:
        - Medicine_List: A list containing selected medicine, price and price_unit
    '''
    ## create instance of Dataframe function ##
    MedicineFrame = Dataframe()
    #print("Hi")

    ## create instance of Cleanframe function using the given MedicineFrame ##
    CleanMedicineFrame = Cleanframe(MedicineFrame)
    #print(CleanMedicineFrame)

    ## create instance of Uniquefilter function using the given CleanMedicineFrame ##
    UniqueMedicineFrame = Uniquefilter(CleanMedicineFrame)
    #print(UniqueMedicineFrame)
    
    ## create instance of MedicineOutput function using the given UniqueMedicineFrame and primary ##
    SpecificMedicine = MedicineOutput(UniqueMedicineFrame, primary)

    ## create instance of string_writer function using the given SpecificMedicine ##
    Medicine_List = string_writer(SpecificMedicine)

    ## writes a specified text to the file using Medicine_List
    FileWriter(Medicine_List)
    return Medicine_List

def parse_args(args_list):
    """
    Functionality:
        - Create an instance of the ArgumentParser class from the argparse module
        - Use the add_argument() method of your ArgumentParser instance to add primary arguement

    Argument:
        - arg_list : a list of strings containing the command-line arguments for the program

    Returns:
        - The ArgumentParser object created
    """
    ## create instance of ArgumentParser class from the argparse module ##
    parser = argparse.ArgumentParser()
    ## use the add_argument method of your ArgumentParser instance to add the following arguments ##
    parser.add_argument('primary', type = str, help = 'The main medicine to search for, the full medicine name is required')
    ## parse and validate arguments ##
    args = parser.parse_args(args_list)
    ## return the ArgumentParser object created ##
    return args

if __name__ == "__main__":
    ## pass sys.argv[1:] to parse_args() and store the result in a variable ##
    args = parse_args(sys.argv[1:])
    ## get the output list from the main ##
    Output_List = main(args.primary)
    print(Output_List)