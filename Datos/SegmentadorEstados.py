import pandas as pd
import csv


df = pd.read_csv("datos_covid_geo.csv",encoding='latin1')

for i,j in df.groupby(["NOMBRE_ENTIDAD_RES","NOMBRE_MUNICIPIO_RES"]):
    j.to_csv('{}.csv'.format(i),index=False)

