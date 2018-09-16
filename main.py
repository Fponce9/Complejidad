import pandas as pd

def TranferirDatos():
    archive = "Coordenas_Pueblos.xlsx"
    Info = pd.read_excel(archive, usecols="F,P,Q")
    Info.sort_values(by="XGD")
    print(Info.head())



