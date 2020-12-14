# -*- coding: utf-8 -*-
"""

Klee's Algorithm Length of Union of Segment of Line

Created on Sun Dec 13 14:45:44 2020

@author: misra
"""

def findLenUnion(Segment):
    
    PointVec = []
    
    for i in Segment:
        TmpVec = [(i[0], False), (i[1], True)]
        PointVec.extend(TmpVec)
        
    SortedPoints = sorted(PointVec, key=sortFnc)
    
    print(SortedPoints)
    
    LenUnion = 0
    Counter = 0
    for i in range(len(SortedPoints)):
        if Counter != 0:
            LenUnion = LenUnion + (SortedPoints[i][0]-SortedPoints[i-1][0])
            
        if SortedPoints[i][1] == False:
            Counter = Counter + 1
        else:
            Counter = Counter - 1
            
        print("Counter: {}\nLen: {}\n".format(Counter,LenUnion))
    
def sortFnc(Point):
    return(Point[0])


if __name__ in "__main__":
    
    Segment = [(2, 5), (4, 8), (9, 12)]
    
    findLenUnion(Segment)
