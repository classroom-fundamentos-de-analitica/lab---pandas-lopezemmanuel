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
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
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
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    return


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    return


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    return
