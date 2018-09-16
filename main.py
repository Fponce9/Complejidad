import pandas as pd

def CrearNodo():
    archive = "Coordenas_Pueblos.xlsx"
    Info = pd.read_excel(archive, usecols="F,P,Q")
    coordx = Info.iloc[1, 1]
    print(coordx)
    print(Info.head())

CrearNodo()


