import pandas as pd
import numpy as np
from datetime import datetime, date



def age_calc(born):
    """"takes in the date of a customer and calulates the age"""
    born = born.date()
    today = date.today()
    return today.year - born.year - ((today.month, 
                                      today.day) < (born.month, 
                                                    born.day))


def bogo(df):
    """Calculates if a customer took up the BOGO offer. Takes in a data frame"""
    if df['offer_type']=='bogo':
        if df['offer_completed']==df['offer_viewed']:
            return df['offer_completed']
        if df['offer_completed']>df['offer_viewed']:
            return df['offer_viewed']
        if df['offer_completed']<df['offer_viewed']:
            return df['offer_completed']
        else:
            return 0
    else:
        return 0

def discount(df):
    """Calculates if a customer took up the Discount offer. Takes in a data frame"""
    if df['offer_type']=='discount':
        if df['offer_completed']==df['offer_viewed']:
            return df['offer_completed']
        if df['offer_completed']>df['offer_viewed']:
            return df['offer_viewed']
        if df['offer_completed']<df['offer_viewed']:
            return df['offer_completed']
        else:
            return 0
    else:
        return 0


def info(df):

    """Calculates if a customer viewed an Informational offer. Takes in a data frame"""
    if df['offer_type']=='informational':
        if df['offer_viewed']==df['offer_received']:
            return df['offer_viewed']
        if df['offer_viewed']< df['offer_received']:
            return df['offer_viewed']
        if df['offer_viewed']==df['offer_received']:
            return df['offer_received']                  
    else:
        return 0
    

    
def offer_time(df):
    """Calculates how quickly an offer waas taken up after it was viewed. Takes in a data frame"""
    if df['discount_taken']>0 or df['bogo_taken']>0:
        return (df['offer_completed']- df['offer_viewed'])
    else:
        return 0

def info_time(df):
    """Calculates how quickly an informational offer is viewed. Takes in a data frame"""
    if df['info_viewed']>0:
        return (df['offer_viewed']-df['offer_received'])
    else:
        return 0