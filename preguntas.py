"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
from posixpath import split
from unicodedata import numeric
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    return len(tbl0)

def pregunta_02():
    return len(tbl0.columns)

def pregunta_03():
    return tbl0['_c1'].value_counts().sort_index()

def pregunta_04():
    respuesta = tbl0[['_c1', '_c2']].groupby(['_c1']).mean()
    serie = respuesta.squeeze()
    return serie

def pregunta_05():
    respuesta = tbl0[['_c1', '_c2']].groupby(['_c1']).max()
    serie = respuesta.squeeze()
    return serie

def pregunta_06():
    unicos = tbl1['_c4'].unique()
    salida = sorted(map(lambda x: x.upper(), unicos))
    return salida

def pregunta_07():
    respuesta = tbl0[['_c1', '_c2']].groupby(['_c1']).sum()
    serie = respuesta.squeeze()
    return serie

def pregunta_08():
    sumas = tbl0.sum(numeric_only=True, axis=1).tolist()
    nuevoDf = tbl0.copy()
    nuevoDf['suma'] = sumas 
    return nuevoDf

def pregunta_09():
    c3 = tbl0['_c3'].tolist()
    years = list(map(lambda x: x.split('-')[0], c3))
    nuevoDf = tbl0.copy()
    nuevoDf['year'] = years
    return nuevoDf

def pregunta_10():
    valores = tbl0[['_c1', '_c2']].groupby(['_c1'])['_c2'].apply(list).tolist()
    c2 = []

    for letra in valores:
        texto = ''
        for valor in sorted(letra):
            texto += f'{valor}:'
        
        c2.append(texto[:-1])

    return pd.DataFrame({
        '_c2': c2
    }, index = pd.Series(['A', 'B', 'C', 'D', 'E'], name='_c1'))

def pregunta_11():
    valores = tbl1.groupby(['_c0'])['_c4'].apply(list).tolist()
    c0 = tbl1['_c0'].unique().tolist()
    c4 = []

    for numero in valores:
        texto = ''
        for valor in sorted(numero):
            texto += f'{valor},'
        
        c4.append(texto[:-1])

    return pd.DataFrame({
        '_c0': c0,
        '_c4': c4
    })

def pregunta_12():
    c5a = tbl2.groupby(['_c0'])['_c5a'].apply(list).tolist()
    c5b = tbl2.groupby(['_c0'])['_c5b'].apply(list).tolist()
    c0 = tbl1['_c0'].unique().tolist()
    
    c5 = []

    for i in range(len(c5a)):
        x = []

        for j in range(len(c5a[i])):
            x.append(f'{c5a[i][j]}:{c5b[i][j]}')
        
        texto = ''

        for valor in sorted(x):
            texto += f'{valor},'

        c5.append(texto[:-1])

    return pd.DataFrame({
        '_c0': c0,
        '_c5': c5
    })

def pregunta_13():
    join = pd.merge(tbl0, tbl2, on='_c0', how='inner')

    respuesta = join[['_c1', '_c5b']].groupby(['_c1']).sum()
    serie = respuesta.squeeze()
    return serie
