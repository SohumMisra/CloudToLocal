# -*- coding: utf-8 -*-
"""
Point Manipulation

Created on Sun Dec 13 16:33:14 2020

@author: misra
"""

import numpy as np
import matplotlib.pyplot as plt

""" Point on left or right """
def leftRightPnt():
    SP = (1,1)
    EP = (5,5)
    Pnt = (6, 7)
    # SP = tuple(map(int, input().split()))
    # EP = tuple(map(int, input().split()))
    
    Line1 = tuple([EP[i] - SP[i] for i in range(len(SP))])
    Line2 = tuple([Pnt[i] - SP[i] for i in range(len(SP))])
    
    plt.figure
    plt.plot([SP[0], EP[0]], [SP[1], EP[1]], '-or')
    plt.plot([SP[0], Pnt[0]], [SP[1], Pnt[1]], '-.b')
    plt.plot(Pnt[0], Pnt[1], 'xb')
    # plt.show()
    
    Out = np.cross(Line1,Line2)
    
    if Out > 0:
        print("Point is on the Left")
    elif Out == 0:
        print("Point is on the Line")
    elif Out < 0:
        print("Point is on the Right")
        
def pointsOnALine(PntSet):
    
    if len(PntSet) <= 2:
        return len(PntSet)
    
    MaxCount = 0
    LineMC = ()
    
    for ei, i in enumerate(PntSet):
        PntSubSet = PntSet[ei+1:]
        if len(PntSubSet) > 0:
            Pivot = [(i,j) for j in PntSubSet]
        
            MCList = list(map(findMC,Pivot))
            print(MCList)
            
            SetMC = set(MCList)
            Dup = MCList.count((float('inf'),float('inf')))
            
            for j in SetMC:
                Cnt = MCList.count(j) + Dup
                # print(Cnt)
                if Cnt > MaxCount:
                    LineMC = j
                MaxCount = max(Cnt,MaxCount)
                
    return(MaxCount+1, LineMC)
 
def findMC(Pnts):
    
    P1 = Pnts[0]
    P2 = Pnts[1]
    
    Thresh = 1e-8    
    if P1 == P2:
        M = float('inf')
        C = float('inf')
    elif abs(P1[0]-P2[0]) <= Thresh:
        M = float('inf')
        C = P1[0]
    else:
        M = round((P2[1]-P1[1])/(P2[0]-P1[0]),4)
        C = round(P1[1] - M*P1[0],4)
        
    return((M,C))

if __name__ in "__main__":
    
    points = [(-1, 1), (0, 0), (0, 0), (1, 1), (1, 1), (2, 2), (3, 3), (3, 4)] 
    POL, LEq = pointsOnALine(points)
    
    print("Max: {} on line with slope and intercept: {}".format(POL,LEq))
    
