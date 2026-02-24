import json 
import pandas as pd

#1

file = open('dados/vendas.json')
data = json.load(file)
#print(data)

#2

df = pd.DataFrame.from_dict(data)
#print(df)

#3

#print(df["Data da Compra"])

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'],format='%d/%m/%Y')

file.close()