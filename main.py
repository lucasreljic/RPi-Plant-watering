import RPi.GPIO as GPIO
import time
import board
import busio
import datetime
import pause
from datetime import date
from datetime import datetime
from datetime import timedelta
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_dht
i2c = busio.I2C(board.SCL, board.SDA)

#variable assignment
ads = ADS.ADS1115(i2c)
data_format = "/%Y/%m/%d"
today = datetime.today()
strday = datetime.strftime(today, "%m/%d/%Y")
someday = datetime.strptime('11/29/2020', "%m/%d/%Y")
tenthday = timedelta(days=10)
startday = timedelta(days=9)
temp = None
humid = None
#module setup
mod1 = 25
mod2 = 17
mod3 = 27
mod4 = 29
#digital pin setup
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(25, GPIO.OUT)


#analog pin setup
dht = adafruit_dht.DHT22(board.D22)
p1 = AnalogIn(ads, ADS.P0)
p2 = AnalogIn(ads, ADS.P1)
p3 = AnalogIn(ads, ADS.P2)
p4 = AnalogIn(ads, ADS.P3)


def getTemp():
	global temp
	while temp is None: #tries until it gets a good reading
		try:
			
			temp = dht.temperature
			
			#print(temp)
		except RuntimeError as error:
			#print(error.args[0])
			continue
		except Exception as error:
			dht.exit()
			raise error
	time.sleep(1)

	return temp
def getHumid():
	global humid
	while humid is None: #tries until it gets a good reading
		try:
			
                        humid = dht.humidity
			
		except RuntimeError as error:
			continue
		except Exception as error:
			dht.exit()
			raise error


	return humid

def module1():
	#constant for watering
	k = 1
	#time between pump on and off
	wait1 = k*getTemp()*(getHumid()/100)*(p4.voltage)
	GPIO.output(mod1, GPIO.HIGH)
	wait1
	GPIO.output(mod1, GPIO.LOW)


def module2():
        #constant for watering
        k = 1
        #time between pump on and off
        wait1 = k*getTemp()*(getHumid()/100)*(p3.voltage)
        GPIO.output(mod2, GPIO.HIGH)
        wait1
        GPIO.output(mod2, GPIO.LOW)

def module3():
        #constant for watering
        k = 1
        #time between pump on and off
        wait1 = k*getTemp()*(getHumid()/100)*(p2.voltage)
        GPIO.output(mod3, GPIO.HIGH)
        wait1
        GPIO.output(mod3, GPIO.LOW)

def module4():
        #constant for watering
        k = 1
        #time between pump on and off
        wait1 = k*getTemp()*(getHumid()/100)*(p1.voltage)
        GPIO.output(mod4, GPIO.HIGH)
        wait1
        GPIO.output(mod4, GPIO.LOW)



while True: #run indefinitely
	#update variables
	today = datetime.today()
	if today.hour > 7: #set wait until to ten days into the future
		nexttime = today + startday
	else: #set wait until today
		nexttime = someday + tenthday

	difftime = today - someday
	#if its correct date
	if(difftime >= tenthday and today.hour == 18):
		print("success")
		#GPIO.output(25, GPIO.LOW)
		strday = datetime.strftime(today, "%m/%d/%Y")
		someday = datetime.strptime(strday, "%m/%d/%Y")

	time.sleep(10)
	print(getTemp())
	print(startday)
	print(nexttime)
	pause.until(nexttime)


