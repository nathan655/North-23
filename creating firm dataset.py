# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 12:13:59 2022

@author: ppastory
"""

#this is a code to dowload data
import eikon as ek
ek.set_app_key('')

index, e = ek.get_data(['.STOXX'], ['TR.IndexConstituentRIC', 'TR.IndexConstituentName','TR.IndexConstituentWeightPercent'])

list_ric = list(index['Constituent RIC'])
start_year = 1995
end_year = 2020

try:
   sp,err = ek.get_data(list_ric, fields=['TR.CoRPrimaryCountry','TR.CLOSEPRICE.date', 'TR.CLOSEPRICE',
    'TR.TRESGScore','TR.TRESGScoreGrade','TR.ESGCScore','TR.TRESGCScoreGrade',
    'TR.EnvironmentPillarScore','TR.SocialPillarScore','TR.fdfdf',
    'TR.TRESGResourceUseScore','TR.ControvAntiCompetition','TR.ControvBusinessEthics',
    'TR.ControvCopyrights','TR.ControvCriticalCountries','TR.ControvPublicHealth','TR.ControvRespMarketing',
    'TR.ControvResponsibleRD','TR.ControvEnv'],
    parameters = {'SDate':'0',
                                    'EDate':'-20',
                                    'Period':'FY0',
                                    'Frq':'FY'})

except ek.EikonError:
    print('eikon error')
    #try after some time

sp1 = sp


##########do not touch sp1
    
df = sp
    
import numpy as np
import pandas as pd


sp['Primary Country of Risk'] = sp['Primary Country of Risk'].replace('',np.nan)

sp['Primary Country of Risk'].fillna(method='ffill', inplace=True)

sp.to_excel(r'C:\Users\ppastory\OneDrive - UGent\Documenten\programming\hackethon\data_set_firms.xlsx')
#change the year

sp['year'] = sp['Date'].str[:4]

list_countries = list(sp['Primary Country of Risk'].unique())

country_e = pd.read_csv(r'C:\Users\ppastory\OneDrive - UGent\Documenten\programming\hackethon\Greenhouse gas emissions in effort sharing decision (ESD) sectors.csv')

country_e['geo'] = country_e['geo'].replace('FR','France')
country_e['geo'] = country_e['geo'].replace('IT','Italy')
country_e['geo'] = country_e['geo'].replace('UK','United Kingdom')
country_e['geo'] = country_e['geo'].replace('NL','Netherlands')
country_e['geo'] = country_e['geo'].replace('SE','Sweden')
country_e['geo'] = country_e['geo'].replace('CH','Switzerland')
country_e['geo'] = country_e['geo'].replace('SP','Spain')
country_e['geo'] = country_e['geo'].replace('FI','Finland')
country_e['geo'] = country_e['geo'].replace('PT','Portugal')
country_e['geo'] = country_e['geo'].replace('DE','Germany')
country_e['geo'] = country_e['geo'].replace('DK','Denmark')
country_e['geo'] = country_e['geo'].replace('FI','Finland')














