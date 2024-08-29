import pandas as pd
from main import preencher

plan = pd.read_excel('aula10/Dados.xlsx')

for (i, linha) in plan.iterrows():
    preencher(linha['Atleta'], linha['Modalidade'],
              linha['Medalha'], linha['Comitê'])
