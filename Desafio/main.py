
from pandas.io.json import json_normalize
import requests
import pandas as pd
import numpy as np
import os
os.chdir(os.path.dirname('C:\\Users\\Dor\\Desktop\\DesafioMl\\Desafio\\'))
import ml
os.chdir(os.path.dirname('C:\\Users\\Dor\\Desktop\\DesafioMl\\Desafio\\output\\'))

###################################


palabras_busqueda = ['iphone 7','samsung galaxy s7', 'huawei P9']
cant = 20

x=0
for palabra_busqueda in palabras_busqueda:
    try:
        busqueda = ml.search(palabra_busqueda, cant) 
        for index,row in busqueda.iterrows():
            try:
                item = ml.get_item_full(row['id'])
                if(row['catalog_product_id'] is not None):
                    catalog = ml.get_catalog_product(row['catalog_product_id'])
                    catalog = catalog.drop(['id','attributes','domain_id', 'last_updated'],1) # quito columnas repetidas
                    item = pd.concat([item,catalog], axis = 1) 
                item = pd.concat([item,pd.DataFrame(data = [palabra_busqueda], columns = ['palabra_busqueda']), pd.DataFrame(data = [index+1], columns = ['posic_busqueda'])], axis = 1) 
                if index == 0:
                    item_s = item.copy()
                    #item_s = item_s.transpose()
                else:
                    item_s = pd.concat([item_s,item])
            except:
                pass
        if x == 0:
            todo = item_s.copy()
            x=x+1
        else:
            todo = pd.concat([todo,item_s])
            x=x+1
    except:
        pass

todo.to_csv('base_4prueba.csv')




