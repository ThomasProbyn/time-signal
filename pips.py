# A python script to play the Greenwich Pips 5 seconds before the hour, every hour, from 05:59:55-22:00:00
# Import all the things we need to work with

import pygame
import datetime
from time import sleep

# Initalise Pygame and load the file, so that we don't need to do it every time we want to play the pips. Becasue it takes time to load PyGame, it'll mean that the pips will be delayed and not on time.
pygame.init()
pygame.mixer.music.load("pips.wav")

# This function, when called, will play the pips straight away
def pips():
    # sleep(0.3) #This delay can be uncommented if the pips are sounding too early. If the pips are too late, then set it to trigger at XX:59:53, and use this delay to compensate however much you need to.
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(1)


while True: #Loop forever
        current_time = datetime.datetime.now().time() #Store the current time in a variable
        lastMinute = False #Create a boolean which represents whether or not it is currently the last minute of the hour or not - set it as currently not being the last hour
        if not(datetime.time(6, 0) < current_time < datetime.time(22, 0)) or current_time.minute < 59: #If it is not during the night (when the pips are switched off) or it is any minute in an hour other than the last minute (XX:59), we don't have to do anything
            sleep(30) #So we wait 30 seconds before looping back round to the top of the while loop. We wait so that the programme doesn't unnecessarily loop infinitely at full speed and take up a ridiculous amount of CPU power
        elif current_time.minute == 59: #If it *is* the 59th minute, during which we need to set off the pips,
            lastMinute = True #we set the lastMinute boolean to True so that the next while loop will run
        while lastMinute: #During the last minute of every hour (aside from at night) this while loop will run however fast the processor can possibly get, meaning we should be able to check the accurate time approximately every few milliseconds
            current_time = datetime.datetime.now().time() #Check the up-to-date time
            if current_time.second == 54: #If it has just changed to XX:59:54
                lastMinute = False #Set lastMinute boolean to false so that the pips don't go twice
                pips() #Sound the pips!
                    