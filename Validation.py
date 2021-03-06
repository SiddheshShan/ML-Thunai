import pandas as pd
import numpy as np

def openinputfile(filename):
    filename_list=filename.split(".")
    if(filename_list[1]=="xlsx"):
        data=pd.read_excel(filename) 
    elif(filename_list[1]=="csv"):
        data=pd.read_csv(filename)
    return data
def validation(data):
    class Error(Exception):
        """Base class for other exceptions"""
    pass


    class ValueTooSmallError(Error):
        """Raised when the input value is too small"""
    pass


    class ValueTooLargeError(Error):
        """Raised when the input value is too large"""
    pass
    try:
        nrows=len(data.values)
        ncol=len(data.columns)
        if nrows < 200:
            raise ValueTooSmallError 
        elif nrows > 2500:
            raise ValueTooLargeError
        if ncol < 2:
            raise ValueTooSmallError
        elif ncol > 100:
            raise ValueTooLargeError
    except ValueTooSmallError:
        print("value is too small, try again!")
    except ValueTooLargeError:
        print("value is too large, try again!")
    
    
filename='Swimming Dataset.xlsx'
data=openinputfile(filename)
validation(data)
