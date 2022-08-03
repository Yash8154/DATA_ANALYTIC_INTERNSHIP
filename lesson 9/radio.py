# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:24:17 2022

@author: Mehta Yash
"""

"""
Create a Radio class with characteristics and functionality discussed
 in the session/video.
      
Create the object of the Radio class and start the radio and play 
a song.

Hint:

Characteristics    |   Functionality
---------------------------------------
color              |
brand              |
ACPower            |
headphone          |
                   |
power_led          | power_switch  ( ON / OFF)
mode_led           | mode_switch   ( AM / FM )
frequency          | band_tuner    ( 88 - 108 )
volume             | volume_tuner  ( 1 - 10 )
---------------------------------------


Characteristics are mapped into data/variables
Functionality are mapped into methods/functions
Class is a blueprint for creating instances (objects)


How should I be able use Radio class: 

I should be able to 
Go to the market and buy a new Radio
Switch ON the radio
Set the mode to FM
Set the frequency to 102.2
Set the volume to 8
Listen to your song
Switch OFF the radio
Destroy the Radio
"""

class Radio:
    color="Red"
    Brand="BoAt"
    Ac_power="false"
    Headphone="false"
    def __init__(self):
        self.powermode="on"
        self.mode=None
        self.frequency=0.0
        self.volume=0
        print("your radio is all set to listen a music")
        
        
    def power_switch(self,powertype):
        self.powermode=powertype
        print("your radio power is",self.powermode)
    def mode_switch(self,mode):
        self.mode=mode
        print("your radio mode set by you is",self.mode)
    def band_tuner(self,value):
        self.frequency=value
        print("your radio frequency is",self.frequency)
    def volume_tuner(self,rate):
        self.volume=rate
        print("your radio volume is",self.volume)
        
my_radio=Radio()
print("color of radio is",Radio.color)
print("brand of radio",Radio.Brand)
my_radio.power_switch("ON")
my_radio.mode_switch("fm")
my_radio.band_tuner("98.98")
my_radio.volume_tuner("7")
my_radio.power_switch("OFF")

        
        
        
        
        
            
        





























































