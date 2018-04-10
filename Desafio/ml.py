from pandas.io.json import json_normalize
import requests
import pandas as pd
import numpy as np
import os

def search(product, limit) : # trae una busqueda
    path = "https://api.mercadolibre.com/sites/MLA/search?q={}%207&limit={}#jso".format(product,limit)
    r = requests.get(path) 
    results = json_normalize(r.json()['results'])
    return results
###ITEM  
def get_item(id_item): # # trae un item
    path = "https://api.mercadolibre.com/items/{}".format(id_item)
    r= requests.get(path)
    return json_normalize(r.json())


def get_item_attributes(id_item): # trae los atributos de un item
    path = "https://api.mercadolibre.com/items/{}".format(id_item)
    r= requests.get(path)
    return json_normalize(r.json()['attributes'])

def get_item_full(id_item): # # trae un item con todos sus atributos en columnas
    path = "https://api.mercadolibre.com/items/{}".format(id_item)
    r= requests.get(path)
    item= json_normalize(r.json())
    attr = json_normalize(r.json()['attributes'])    
    for index, row in attr.iterrows():   # recorro los atributos para agregarlos en columnas
        new_variable = pd.DataFrame(data= [row['value_name']]  ) 
        new_variable.columns = [['item_'+row['id']]]
        item = pd.concat([item,new_variable], axis = 1)
    return item
  
###CATALOG
def get_catalog_product(catalog_product_id): # trae un catalogo 
    path = "https://api.mercadolibre.com/catalog_products/{}".format(catalog_product_id)
    r= requests.get(path)
    catalog = json_normalize(r.json())
    attr = json_normalize(r.json()['attributes'])    
    for index, row in attr.iterrows():   # recorro los atributos para agregarlos en columnas
        new_variable = pd.DataFrame(data= [row['value_name']]  ) 
        new_variable.columns = [['catal_'+row['id']]]
        catalog = pd.concat([catalog,new_variable], axis = 1)
    return catalog
    
def get_atrrib_catalog_product(catalog_product_id): # trae los atributos de un catalogo
    path = "https://api.mercadolibre.com/catalog_products/{}".format(catalog_product_id)
    r= requests.get(path)
    return json_normalize(r.json()['attributes'])

###CATEGORY
def get_category(category_id): # trae una categoria
    path = "https://api.mercadolibre.com/categories/{}".format(category_id)
    r= requests.get(path)
    return json_normalize(r.json())