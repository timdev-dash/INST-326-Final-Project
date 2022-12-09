""" 
Driver: Mujahid Syed, Tim Scott, George Chen, Jeremy Yee
Assignment: Team 11 Project
Date: 11/28/2022
INST326-ESG1 Farmer Fall 2022
"""
import csv
import argparse
import sys
import pandas as pd
import re
import requests

    
#This function removes unnecessary columns from the dataframe
def FrameCleaner(dataframe):
    cols = [3,5,6,7,8,9,10,11]
    cleaned_dataframe = dataframe.drop(dataframe.columns[cols], axis = 1)
    return cleaned_dataframe
    
#Takes extracted data and organizes each item    
def Uniquefilter(self):
    '''This function looks through the dataframe and removes duplicate items'''
    pass
        

def DataframeMaker():
    '''
    This function takes data from a csv url and converts it into a dataframe
    
    Arguments:
        - rawdata: The original data file
    
    Returns:
        - rawdata as a dataframe
    
    '''
    Medicines = pd.read_csv("https://download.medicaid.gov/data/nadac-national-average-drug-acquisition-cost-12072022.csv")
    return Medicines

def DataframeSorter(dataframe):
    '''Takes dataframe argument and sorts the information by cost from lowest to highest
    
    Argument
        - dataframe: dataframe containing items and their prices
    
    Returns: 
        - Dataframe sorted by costs'''
    pass

def FileWriter(dataframe):
    '''Writes information to a text file using the dataframe argument
    
    Argument
        - dataframe: dataframe containing items and their prices
    
    Returns: 
        - txt file containing dataframe'''
    pass

def ShowPrices(dataframe):
    ''' Takes dataframe argument and displays information to the user
    
    Argument
        - dataframe: dataframe containing items and their prices
    
    Returns: 
        - Dataframe output to the user'''
    pass

def UnecessaryItems(dataframe):
    '''Removes items that are not a part of the users query
    
    
    Argument
        - dataframe: dataframe containing items and their prices
    
    Returns: 
        - Filtered dataframe containing only relevant items'''
    pass

def FileSaver(textfile):
    '''Takes textfile argument and saves it
    
    Argument
        - textfile: textfile containing filtered and sorted dataframe
    '''
    pass

def main(dataframe):
    """
    The main function

    Parameters:
        dataframe (str)
    """
    UpdatedFrame = FrameCleaner(dataframe)
    print(UpdatedFrame)
    return None

def parse_args(args_list):
    '''
    Takes a string from the command prompt and passes it through as an argument
    
    Args:
        args_list(list): the list of strings from the command prompt
    Returns:
        args(ArgumentParser)
    '''
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--medicine_type', type = str, help = 'The type of medicine a user wants to search for')
    args = parser.parse_args(args_list)
    return args



if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    
    #Creat Medicine dataframe then pass dataframe through main to filter and sort data
    Medicine = DataframeMaker()
    RequestedProduct = main(Medicine)