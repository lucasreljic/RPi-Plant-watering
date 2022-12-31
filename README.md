# RPi-Plant-watering
Code for my plant watering project from grade 11. This is running on a Raspberry Pi Zero W, with 4 potentiometers and a humidity/temperature sensor. The code triggers a set of relays that control a pump for each plant. The Cron version is the simplified version of the code that runs using Linux's Cron schedular. The code consists of multiple functions so sections of code can be run multiple times. The primary functions are the modules numbered 1-4, they each activate their corresponding transmitters. Then each module waits until the calculated time expires to deactivate the transmitters. This time is the double value represented by wait(module number). It takes into consideration the max amount of water, which is 1L or 33.33 seconds of the pump running. It also gets the temperature and humidity and compares it against the optimal temp and humidity for plants. Then it subtracts or adds time accordingly for a max of 100 ml based on temperature and humidity.
![alt text](https://github.com/lucasreljic/RPi-Plant-watering/blob/main/IMG_3525.jpeg)
![alt text](https://github.com/lucasreljic/RPi-Plant-watering/blob/main/IMG_3520.jpeg)

