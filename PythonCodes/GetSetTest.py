# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:38:01 2020

@author: sohum misra
"""

# import numpy as np

class Celcius:
    
    def __init__(self,temp=0):
        self.temp = temp
        
    def TempC(self):
        print("Temperature in Celcius: {}".format(self.temp))
        
    def TempF(self):
        print("Temperature in Farenheit: {}".format(1.8*self.temp+32))
        
    @property
    def temp(self):
        print("Getting Temp Value")
        return self._temp
    
    @temp.setter
    def temp(self,val):
        print("Setting Temp Value")
        if val < -273.15:
            raise ValueError("Temperature below absolute Kelvin not possible")
        self._temp = val

def main():    
#    BodyTemp = Celcius(37)
#    BodyTemp.TempC()
#    BodyTemp.TempF()
    
    RT = Celcius()
    RT._temp = -300 # Possible
    RT.TempC()
    # RT.temp = -300 # Not Possible
    
    help(RT)

if __name__ == "__main__":
    main()