import xlsxwriter
import pandas as pd
import numpy as np
import mysql.connector

australia=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='Australia')
brunei=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='Brunei')
cambodia=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='Cambodia')
china=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='China')
indonesia=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='Indonesia')
japan=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='Japan')
lao=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='Lao')
malaysia=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='Malaysia')
myanmar=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='Myanmar')
new_zeland=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='New Zeland')
philipines=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='Philipines')
singapore=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='Singapore')
thailand=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='Thailand')
vietnam=pd.read_excel(r'\Users\jesica\Desktop\RCEP_economic_analysis.xlsx', sheet_name='Vietnam')


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = ""
)

mycursor = mydb.cursor()

sqlformula1 = "INSERT INTO australia VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(australia['Year'], australia['RGDP'], australia['NGDP'], australia['GDP_pc'], australia['Inflation'], australia['Unemployment_Rate'], australia['Net_LB'], australia['Account_Balance']):
    mycursor.execute(sqlformula1, [a, b, c, d, e, f, g, h])

sqlformula2 = "INSERT INTO brunei VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(brunei['Year'], brunei['RGDP'], brunei['NGDP'], brunei['GDP_pc'], brunei['Inflation'], brunei['Unemployment_Rate'], brunei['Net_LB'], brunei['Account_Balance']):
    mycursor.execute(sqlformula2, [a, b, c, d, e, f, g, h])

sqlformula3 = "INSERT INTO cambodia VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(cambodia['Year'], cambodia['RGDP'], cambodia['NGDP'], cambodia['GDP_pc'], cambodia['Inflation'], cambodia['Unemployment_Rate'], cambodia['Net_LB'], cambodia['Account_Balance']):
    mycursor.execute(sqlformula3, [a, b, c, d, e, f, g, h])

sqlformula4 = "INSERT INTO china VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(china['Year'], china['RGDP'], china['NGDP'], china['GDP_pc'], china['Inflation'], china['Unemployment_Rate'], china['Net_LB'], china['Account_Balance']):
    mycursor.execute(sqlformula4, [a, b, c, d, e, f, g, h])

sqlformula5 = "INSERT INTO indonesia VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(indonesia['Year'], indonesia['RGDP'], indonesia['NGDP'], indonesia['GDP_pc'], indonesia['Inflation'], indonesia['Unemployment_Rate'], indonesia['Net_LB'], indonesia['Account_Balance']):
    mycursor.execute(sqlformula5, [a, b, c, d, e, f, g, h])

sqlformula6 = "INSERT INTO japan VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(japan['Year'], japan['RGDP'], japan['NGDP'], japan['GDP_pc'], japan['Inflation'], japan['Unemployment_Rate'], japan['Net_LB'], japan['Account_Balance']):
    mycursor.execute(sqlformula6, [a, b, c, d, e, f, g, h])

sqlformula7 = "INSERT INTO lao VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(lao['Year'], lao['RGDP'], lao['NGDP'], lao['GDP_pc'], lao['Inflation'], lao['Unemployment_Rate'], lao['Net_LB'], lao['Account_Balance']):
    mycursor.execute(sqlformula7, [a, b, c, d, e, f, g, h])

sqlformula8 = "INSERT INTO malaysia VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(malaysia['Year'], malaysia['RGDP'], malaysia['NGDP'], malaysia['GDP_pc'], malaysia['Inflation'], malaysia['Unemployment_Rate'], malaysia['Net_LB'], malaysia['Account_Balance']):
    mycursor.execute(sqlformula8, [a, b, c, d, e, f, g, h])

sqlformula9 = "INSERT INTO myanmar VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(myanmar['Year'], myanmar['RGDP'], myanmar['NGDP'], myanmar['GDP_pc'], myanmar['Inflation'], myanmar['Unemployment_Rate'], myanmar['Net_LB'], myanmar['Account_Balance']):
    mycursor.execute(sqlformula9, [a, b, c, d, e, f, g, h])

sqlformula10 = "INSERT INTO new_zeland VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(new_zeland['Year'], new_zeland['RGDP'], new_zeland['NGDP'], new_zeland['GDP_pc'], new_zeland['Inflation'], new_zeland['Unemployment_Rate'], new_zeland['Net_LB'], new_zeland['Account_Balance']):
    mycursor.execute(sqlformula10, [a, b, c, d, e, f, g, h])

sqlformula11 = "INSERT INTO philipines VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(philipines['Year'], philipines['RGDP'], philipines['NGDP'], philipines['GDP_pc'], philipines['Inflation'], philipines['Unemployment_Rate'], philipines['Net_LB'], philipines['Account_Balance']):
    mycursor.execute(sqlformula11, [a, b, c, d, e, f, g, h])

sqlformula12 = "INSERT INTO singapore VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(singapore['Year'], singapore['RGDP'], singapore['NGDP'], singapore['GDP_pc'], singapore['Inflation'], singapore['Unemployment_Rate'], singapore['Net_LB'], singapore['Account_Balance']):
    mycursor.execute(sqlformula12, [a, b, c, d, e, f, g, h])

sqlformula13 = "INSERT INTO thailand VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(thailand['Year'], thailand['RGDP'], thailand['NGDP'], thailand['GDP_pc'], thailand['Inflation'], thailand['Unemployment_Rate'], thailand['Net_LB'], thailand['Account_Balance']):
    mycursor.execute(sqlformula13, [a, b, c, d, e, f, g, h])

sqlformula14 = "INSERT INTO vietnam VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
for a, b, c, d, e, f, g, h in zip(vietnam['Year'], vietnam['RGDP'], vietnam['NGDP'], vietnam['GDP_pc'], vietnam['Inflation'], vietnam['Unemployment_Rate'], vietnam['Net_LB'], vietnam['Account_Balance']):
    mycursor.execute(sqlformula14, [a, b, c, d, e, f, g, h])


mydb.commit()
