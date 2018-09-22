import pandas as pd
import math

archive = "Coordenas_Pueblos.xlsx"
Info = pd.read_excel(archive, usecols="F,P,Q")


class Vertice:
    hijos = ()
    coorx = 0.0
    coory = 0.0
    dist = ()
    color = ""
    Nombre = ""

    def __init__(self, hijosypadre: tuple, coorx, coory, dist: tuple, Nombre):
        self.hijos = hijosypadre
        self.coorx = coorx
        self.coory = coory
        self.dist = dist
        self.color = "Blanco"
        self.Nombre = Nombre

    def setColor(self,Color):
        self.color = Color
    def getColor(self):
        return self.color
    def getNombre(self):
        return self.Nombre


array = []

dicc = {}


def Peson(xo, yo, xd, yd):
    equis = xd - xo
    lle = yd - yo
    return math.sqrt((equis ** 2 + lle ** 2))


def CrearConexion():
    for fila in range(0, 145225):

        if fila < 145223:

            if fila < 3:
                if fila < 1:
                    hijos = (Info.iloc[fila + 1, 0], Info.iloc[fila + 2, 0])
                    dist = (
                     Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 1, 1], Info.iloc[fila + 1, 2]),
                     Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 2, 1], Info.iloc[fila + 2, 2]))
                    nombre = Info.iloc[fila,0]
                    dicc[Info.iloc[fila,0]] = Vertice(hijos, Info.iloc[fila, 1], Info.iloc[fila, 2], dist,nombre)
                else:
                    hijos = (Info.iloc[fila + 1, 0], Info.iloc[fila + 2, 0],Info.iloc[fila - 1, 0])
                    dist = (
                        Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 1, 1], Info.iloc[fila + 1, 2]),
                        Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 2, 1], Info.iloc[fila + 2, 2]),
                        Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 1, 1], Info.iloc[fila - 1, 2]))
                    nombre = Info.iloc[fila, 0]
                    dicc[Info.iloc[fila, 0]] = Vertice(hijos, Info.iloc[fila, 1], Info.iloc[fila, 2], dist, nombre)
            elif fila == 145218:
                hijosypadre = (
                    Info.iloc[fila + 1, 0], Info.iloc[fila + 2, 0], Info.iloc[fila - 1, 0], Info.iloc[fila - 2, 0],
                    Info.iloc[fila + 4, 0])
                dist = (Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 1, 1], Info.iloc[fila + 1, 2])
                        , Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 2, 1], Info.iloc[fila + 2, 2])
                        , Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 1, 1], Info.iloc[fila - 1, 2])
                        , Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 2, 1], Info.iloc[fila - 2, 2])
                        , Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 4, 1], Info.iloc[fila + 4, 2])
                        )
                dicc[Info.iloc[fila,0]] = Vertice(hijosypadre, Info.iloc[fila, 1], Info.iloc[fila, 2], dist,Info.iloc[fila,0])
            elif fila == 145219:
                hijosypadre = (
                    Info.iloc[fila + 1, 0], Info.iloc[fila + 2, 0], Info.iloc[fila - 1, 0], Info.iloc[fila - 2, 0],
                    Info.iloc[fila + 3, 0], Info.iloc[fila + 4, 0])
                dist = (Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 1, 1], Info.iloc[fila + 1, 2])
                        , Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 2, 1], Info.iloc[fila + 2, 2])
                        , Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 1, 1], Info.iloc[fila - 1, 2])
                        , Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 2, 1], Info.iloc[fila - 2, 2])
                        , Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 3, 1], Info.iloc[fila + 3, 2])
                        , Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 4, 1], Info.iloc[fila + 4, 2])
                        )
                dicc[Info.iloc[fila,0]] = Vertice(hijosypadre, Info.iloc[fila, 1], Info.iloc[fila, 2], dist,Info.iloc[fila,0])
            else:
                hijos = (Info.iloc[fila + 1, 0], Info.iloc[fila + 2, 0],Info.iloc[fila - 1,0],Info.iloc[fila-2,0])
                dist = (
                    Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 1, 1], Info.iloc[fila + 1, 2]),
                    Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila + 2, 1], Info.iloc[fila + 2, 2]),
                    Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 1, 1], Info.iloc[fila - 1, 2]),
                    Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 2, 1], Info.iloc[fila - 2, 2]))
                nombre = Info.iloc[fila, 0]
                dicc[Info.iloc[fila, 0]] = Vertice(hijos, Info.iloc[fila, 1], Info.iloc[fila, 2], dist, nombre)
        else:
            if fila == 145224:
                hijosypadre = (Info.iloc[fila - 3, 0], Info.iloc[fila - 4, 0],Info.iloc[fila - 2, 0],Info.iloc[fila - 1, 0])
                dist = (Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 3, 1], Info.iloc[fila - 3, 2]),
                        Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 4, 1], Info.iloc[fila - 4, 2]),
                        Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 2, 1], Info.iloc[fila - 2, 2]),
                        Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 1, 1], Info.iloc[fila - 1, 2]))
                dicc[Info.iloc[fila,0]] = Vertice(hijosypadre, Info.iloc[fila, 1], Info.iloc[fila, 2], dist,Info.iloc[fila,0])
            else :
                hijosypadre = (Info.iloc[fila - 3, 0], Info.iloc[fila - 4, 0], Info.iloc[fila - 2, 0])
                dist = (Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 3, 1], Info.iloc[fila - 3, 2]),
                        Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 4, 1], Info.iloc[fila - 4, 2]),
                        Peson(Info.iloc[fila, 1], Info.iloc[fila, 2], Info.iloc[fila - 2, 1], Info.iloc[fila - 2, 2]))
                dicc[Info.iloc[fila, 0]] = Vertice(hijosypadre, Info.iloc[fila, 1], Info.iloc[fila, 2], dist,
                                                   Info.iloc[fila, 0])


Soluciones = []

Camino_Candidato = [None] * 145225


def Algoritmo(Nodo_Inicio:Vertice, Nodos:dicc, Nodo_Actual:Vertice, Etapa: int, Peso):

    if Nodo_Inicio == Nodo_Actual and len(Nodos) == Etapa:
        Camino_Candidato[Etapa] = Nodo_Actual
        Soluciones.append(tuple(Peso,Camino_Candidato))
        return
    elif Nodo_Inicio == Nodo_Actual and Etapa < len(Nodos):
        return
    if Nodo_Actual.getColor() == "Negro":
        return
    else:
        Camino_Candidato[Etapa] = Nodo_Actual.getNombre()
        j=0
        for i in Nodo_Actual.hijos:
            if Etapa == 0:
                Nodo_Actual.setColor("Azul")
            else:
                Nodo_Actual.setColor("Negro")
            Algoritmo(Nodo_Inicio,Nodos,dicc[i],(Etapa + 1),Peso + dicc[i].dist[j])
            j=j+1
            dicc[i].setColor("Blanco")


print(Soluciones)
CrearConexion()
Algoritmo(dicc["Puerto Pardo"],dicc,dicc["Puerto Pardo"],0,0)
print (Soluciones)
