#!/bin/bash
# A minimalist led clock for the Pi Zero ( And Pi Zero W )
# Uses only the onboard led to blink the current hour
# And then to quickly blink the the tens place of minutes
#
# Spike Snell - June 2017

# First set the trigger for the onboard green led to none so that we have control of it
echo none | sudo tee /sys/class/leds/led0/trigger

# Turn off the led so that we have a known state to start
echo 1 | sudo tee /sys/class/leds/led0/brightness

# Loop endlessly
while true
do

    # Wait for a full second to seperate our visual count
    sleep 1

    # Loop for the current number of hours
    # Trim leading 0's so that 08 and 09 aren't interpreted as an octal base
    for ((n=0;n<$(date +"%I" | sed 's/^0*//');n++)) 

    do

        # Wait a bit 
        sleep .25

        # Turn the led on
        echo 0 | sudo tee /sys/class/leds/led0/brightness

        # Wait a bit
        sleep .25

        # Turn the led off
        echo 1 | sudo tee /sys/class/leds/led0/brightness
   
    done

    # Wait for a half second
    sleep .5

    # Now loop very quickly for the current first tens digit of minutes
    for ((n=0;n<$(date +"%M" | head -c 1);n++))

    do 

        # Wait for a small bit
        sleep .1

        # Turn the led on
        echo 0 | sudo tee /sys/class/leds/led0/brightness

        # Wait for a small bit
        sleep .1

        # Turn the led off
        echo 1 | sudo tee /sys/class/leds/led0/brightness

    done

done
