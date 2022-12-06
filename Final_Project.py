""" 
Driver: Mujahid Syed, Tim Scott, George Chen, Jeremy Yee
Assignment: Team 11 Project
Date: 11/28/2022
INST326-ESG1 Farmer Fall 2022
"""

import argparse
import sys
import pandas
import selenium

class Webpage():
    '''Creating the webpage class which will use webscraping to extract data and later be converted into a dataframe for further data analysis'''
    #Initializes URL as string
    def __init__(self):
        pass
    
    #Web Scraper that reads and extract data from webpage using URL 
    def FunctionSeven(self):
        pass
    
    
    #Takes extracted data and organizes each item
    def FunctionEight(self):
        '''This might be a class method'''
        pass
        

def DataframeConverter(rawdata):
    '''Takes data from web scraping and converts it into a dataframe
    
    Argument: 
        - rawdata: the cleaned up and extracted data from webscraping the webpage object
        
    Returns:
        - rawdata as a dataframe
    '''
    pass

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
        - textfile: textfile containing dataframe
    '''
    pass


def parse_args(args_list):
    '''
    Takes a string from the command prompt and passes it through as an argument
    
    Args:
        args_list(list): the list of strings from the command prompt
    Returns:
        args(ArgumentParser)
    '''
    
    parser = argparse.ArgumentParser()
    parser.add_argument('webpage', type = str, help = 'The URl of the desired web page')
    args = parser.parse_args(args_list)
    return args

if __name__ == "__main__":
    pass