import pandas as pd
import math

interestarr = []
unempoymentarr = []
gpdarr = []
inflationarr = []
arr = []
interest = pd.read_excel('./API_FR.INR.RINR_DS2_en_excel_v2_2445277.xls')
index = interest.iloc[2]
ainterest = interest.iloc[11]
unempoyment = pd.read_excel('./API_SL.UEM.TOTL.ZS_DS2_en_excel_v2_2445633.xls')
aunempoyment = unempoyment.iloc[11]
gpd = pd.read_excel('./API_NY.GDP.MKTP.KD.ZG_DS2_en_excel_v2_2445274.xls')
agpd = gpd.iloc[11]
inflation = pd.read_excel('./API_FP.CPI.TOTL.ZG_DS2_en_excel_v2_2445767.xls')
ainflation = inflation.iloc[11]
for x in ainterest:
    if(type(x) != str):
        if(math.isnan(x) == False): # taking interest rates and put them to the array
          interestarr.append(x)
for (x, y) in zip(aunempoyment, index):
    if(type(x) != str):
        if(y >= 1995 and y<2020):
            if(math.isnan(x) == False):
                unempoymentarr.append(x) # taking unempoyment rates and put them to the array
for (x, y) in zip(agpd, index):
    if(type(x) != str):
        if(y >= 1995 and y<2020):
            if(math.isnan(x) == False): # taking gpd rates and put them to the array
                gpdarr.append(x)
for (x, y) in zip(ainflation, index):
    if(type(x) != str):
        if(y >= 1995 and y<2020):
            if(math.isnan(x) == False): # taking  rates and put them to the array
              inflationarr.append(x)
for (a, b ,c ,d) in zip(interestarr, unempoymentarr, gpdarr, inflationarr):
    arr.append(a + b + c + d)
    
HAMI = pd.DataFrame({'1995': [arr[0]],
                       '1996': [arr[1]],
                       '1997': [arr[2]],
                       '1998': [arr[3]],
                       '1999': [arr[4]],
                       '2000': [arr[5]],
                       '2001': [arr[6]],
                       '2002': [arr[7]],
                       '2003': [arr[8]],
                       '2004': [arr[9]],
                       '2005': [arr[10]],
                       '2006': [arr[11]],
                       '2007': [arr[12]],
                       '2008': [arr[13]],
                       '2009': [arr[14]],
                       '2010': [arr[15]],
                       '2011': [arr[16]],
                       '2012': [arr[17]],
                       '2013': [arr[18]],
                       '2014': [arr[19]],
                       '2015': [arr[20]],
                       '2016': [arr[21]],
                       '2017': [arr[22]],
                       '2018': [arr[23]],
                       '2019': [arr[24]]})

HAMI.to_excel('./HAMI-Armenia.xls')
    