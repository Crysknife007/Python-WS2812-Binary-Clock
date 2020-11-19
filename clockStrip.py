# WS2812b Binary Led Strip Clock
# Designed for Pi Zero W board
# By Spike Snell May 2020

# Import all the needed libraries
from datetime import datetime
import board
import neopixel
import time
import sys


# Define our led strip and how many leds we have on D18
pixels = neopixel.NeoPixel(board.D18, 12)

# Make sure the strip is cleared
pixels.fill((0, 0, 0))

# Set the default on RGB value
on = (50, 0, 0)

# Set the default off RGB value
off = (5, 0, 0)

# Set the default divider bit RGB value
div = (15, 15, 15)

# If the length of the arguments passed is 10
if len(sys.argv) == 10:

    # Set the on value based on the RGB tuple sent in
    on = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

    # Set the off value based on the RGB tuple sent in
    off = (int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))

    # Set the div value based on the RGB tuple sent in
    div = (int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9]))

# Else the right number of command line arguments was not found
else:
    print("Pass 9 arguments in the form of RGB tuples for the ON, OFF, and DIV state of the leds.\nFor example: sudo python3 clockStrip.py 50 0 0 5 0 0 15 15 15\nEach RGB value can be 0-255.")

# Refresh the clock every 10 seconds
while True:

        # Get the current date and time
        now = datetime.now()

        # Get the hour string
        hourString = now.strftime("%H")

        # Get the hour in binary
        binaryHourString = bin(int(hourString)).replace("0b","")

        # Get the binary hour string as an array
        binaryHourArray = list(binaryHourString)

        # While the binaryHourArray length is less than 5 pad another zero on the left
        while len(binaryHourArray) < 5:
            binaryHourArray.insert(0, "0")

        # Let our led array start its life as hour binary hour array
        ledArray = binaryHourArray

        # Append a divider indicator to the led array
        ledArray.append("d")

        # Get the minute string
        minuteString = now.strftime("%M")

        # Get the hour in binary
        binaryMinuteString = bin(int(minuteString)).replace("0b","")

        # Get the binary minute string as an array
        binaryMinuteArray = list(binaryMinuteString)

        # While the length of the binaryMinuteArray is less than 6
        while len(binaryMinuteArray) < 6:
            binaryMinuteArray.insert(0, "0")

        # Extend the led array to include the binary minute array
        ledArray.extend(binaryMinuteArray)

        # Make sure we start on pixel 0
        i = 0;

        # For each entry in the led array
        for led in ledArray:

            # If the led should be on
            if led == "1":

                # Set this led to on
                pixels[i] = on

            # Else if the led should be off    
            elif led == "0":

                # Set this led to off
                pixels[i] = off

            # Else we must be on the divider indicator
            else:
                
                # Set this led to the divider indicator color
                pixels[i] = div

            # Make sure we iterate i    
            i += 1

        # Sleep ten seconds
        time.sleep(10)

