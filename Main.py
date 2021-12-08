#LIBRARY
import pandas as pd
import zipfile
import re
import os
import csv
from zipfile import ZipFile
from unicodedata import normalize
#######################################################################
#OPENING CSV FILE AND MANIPULATING DATA
def arquive_excel():

    df=pd.DataFrame()
    for chunk in  pd.read_csv("natal2021.csv", encoding = "UTF-8", sep = ",", chunksize=1000):
        #capital letter
        chunk['CITY'] = chunk['CITY'].str.upper()
        #removing the space at the beginning of sentences
        chunk['CITY'] = chunk['CITY'].str.strip()
        #removing special characters from cities and adding in a new column CITY_ASCII
        city_df= chunk['CITY'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        chunk.insert(loc=3,column='CITY_ASCII', value = city_df)
        #removing special characters from the phone
        chunk['PHONE'] = chunk['PHONE'].apply(fix_phone)
        df=pd.concat([df,chunk])
        print(df.shape[0])
        
    df.to_csv('Retorno_natal2021.csv',index=False)


#REPLACE SPECIAL CHARACTER
def fix_phone(df_number):
    df_number= df_number.replace('(','').replace(')','').replace('.','').replace('-','')
    return df_number

