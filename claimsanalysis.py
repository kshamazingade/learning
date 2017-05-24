# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 17:01:40 2017

@author: Kshama Zingade
"""

import pandas as pd
import numpy as np
import xlwt 

#loading data from CSV file
healthdf = pd.read_csv('claims_data.csv')

print healthdf.head(4)

print healthdf.shape

s = pd.isnull(healthdf).any(axis=0)
nc = s.to_frame()
writer = pd.ExcelWriter('output3.xlsx',engine='xlsxwriter')


nc.to_excel(writer ,sheet_name='null_columns')
nc.to_excel(writer, sheet_name='nc2')


'''wb = xlwt.Workbook()
ws1 = wb.add_sheet('null_cols1')
ws2 =''' 

#checking for null valued columns and removing them
list_nc =[]        
for col in healthdf:
    s = healthdf[col].value_counts(dropna=False)
    if pd.isnull(s.axes).any():
        if s.loc[np.nan]==13541:
            list_nc.append(col)

print list_nc 
s1 = pd.DataFrame(list_nc)    
s1.to_excel(writer, sheet_name='empty_cols')
writer.save()



mod1_hdf = healthdf.drop(labels=list_nc, axis=1) 

print mod1_hdf.shape
'''s = healthdf['CARDType'].value_counts(dropna=False)
print s
l = np.asarray(s.axes)
if pd.isnull(s.axes).any():
    print s.loc[np.nan]'''
 
#unique value counts in each column 

print mod1_hdf.HeadMemberID.unique()
print mod1_hdf.TerminalID.unique()
print mod1_hdf.HospitalCode.unique().shape
print mod1_hdf.HospitalName.unique().shape
print mod1_hdf.HospitalState.unique()
print mod1_hdf.HospitalAuthorityCode.unique().shape
print mod1_hdf.RegistrationDesc.unique().shape
print mod1_hdf.MemberDist.unique().shape
print mod1_hdf.HospitalDistrict.unique()
print mod1_hdf.PackageCode.unique().shape

print mod1_hdf.ProcedureName.unique().shape

print mod1_hdf.PackageCost.unique().shape

print mod1_hdf.Mortality.value_counts(dropna=False)
mod1_hdf["NoofDaysActual"] = pd.to_numeric(mod1_hdf["NoofDaysActual"], errors='coerce')
print mod1_hdf.NoofDaysActual.value_counts(dropna=False)
