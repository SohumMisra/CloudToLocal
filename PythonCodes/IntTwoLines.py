# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:56:13 2020

@author: misra
"""
import matplotlib.pyplot as plt
from math import sqrt

def findIntLineSeg(L1,L2):
    
    Pnt = findInt(L1,L2)
    
    if Pnt != (float('inf'), float('inf')):
        if onSegment(L1[0], L1[1], Pnt) and onSegment(L2[0], L2[1], Pnt):
            print("The line segments intersect at {}".format(Pnt))
        else:
            print("The line segments do not intersect")
            
    visualize(L1, L2, Pnt)
    
def onSegment(P1, P2, PInt): 
    if ( (PInt[0] <= max(P1[0], P2[0])) and (PInt[0] >= min(P1[0], P2[0])) and 
           (PInt[1] <= max(P1[1], P2[1])) and (PInt[1] >= min(P1[1], P2[1]))): 
        return True
    return False
    
    

def findInt(L1,L2):
    
    Thresh = 1e-8
    if eucDist(L1[0], L1[1]) <= Thresh or eucDist(L2[0], L2[1]) <= Thresh:
        Pnt = (float('inf'), float('inf'))
    else:
        A1,B1,C1 = lineCoeff(L1)
        A2,B2,C2 = lineCoeff(L2)
        
        # Cramer's rule
        D  = A1*B2 - A2*B1
        Dx = C1*B2 - C2*B1
        Dy = A1*C2 - A2*C1
        
        if D != 0:
            XInt = Dx/D
            YInt = Dy/D
            Pnt  = (XInt, YInt)
        else:
            print("Parallel Lines")
            
            if L1[1] == L2[0] and L1[0] != L2[1]:
                Pnt = L1[1]
            elif L1[0] == L2[1] and L1[1] != L2[0]:
                Pnt = L1[1]
            elif L1[1] == L2[1] and L1[0] != L2[0]:
                Pnt = L1[1]
            elif L1[0] == L2[0] and L1[1] != L2[1]:
                Pnt = L1[1]
            else:
                print("No or multiple intersection points")
                Pnt = (float('inf'), float('inf'))
    
    return(Pnt)    
        
        
def lineCoeff(Line):
    A = Line[0][1] - Line[1][1]
    B = Line[1][0] - Line[0][0]
    C = Line[0][1]*B + Line[0][0]*A
    
    return(A,B,C)        
        
    
def eucDist(P1,P2):
    Dist = sqrt(pow(P1[0]-P2[0],2)+pow(P1[1]-P2[1],2))
    return(Dist)


def visualize(L1, L2, Pnt):
    plt.figure
    plt.plot([L1[0][0], L1[1][0]], [L1[0][1], L1[1][1]], ':g')
    plt.plot([L2[0][0], L2[1][0]], [L2[0][1], L2[1][1]], ':b')
    plt.plot(Pnt[0], Pnt[1], 'or')


if __name__ in "__main__":
    
    L1 = [(1,1),(5,5)]
    L2 = [(2,0),(4,8)]
    
    # L1 = [(0,0),(10,0)]
    # L2 = [(0,-1),(0,10)]
    
    # L1 = [(0,0),(5,5)]
    # L2 = [(10,10),(5,5)]
    
    # L1 = [(0,0),(5,5)]
    # L2 = [(0,1),(5,6)]
    
    
    findIntLineSeg(L1,L2)
    