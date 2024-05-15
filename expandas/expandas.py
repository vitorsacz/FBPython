import pandas as pd
import os 
import openpyxl


os.system("cls")
feminicidio_df = pd.read_csv("data/Feminicidio.csv")
vendas_df = pd.read_excel("data/Vendas.xlsx")

print("-"*60)
print(feminicidio_df)
print("-"*60)

print("\n")

print("-"*60)
print(vendas_df)
print("-"*60)
