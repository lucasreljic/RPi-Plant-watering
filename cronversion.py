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

today = datetime.today()

temp = None
humid = None
#module setup
mod1 = 25
mod2 = 5
mod3 = 6
mod4 = 13
#digital pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

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
	k = 33.3333 #time in seconds for 1L of water
	kh = 3.33 #max additional seconds for humidity
	kt = 3.33 #max additional seconds for temperature
	#time between pump on and off
	wait1 = (k*abs((p4.value/32752)))+(((40-getHumid())/100)*kh)+(((getTemp()-21)/100)*kt)
	print(wait1)
	GPIO.output(mod1, GPIO.HIGH)
	time.sleep(wait1)
	GPIO.output(mod1, GPIO.LOW)


def module2():
    #constant for watering
	k = 33.3333 #time in seconds for 1L of water
	kh = 3.33 #max additional seconds for humidity
	kt = 3.33 #max additional seconds for temperature
	#time between pump on and off
	wait2 = (k*abs((p3.value/32752)))+(((40-getHumid())/100)*kh)+(((getTemp()-21)/100)*kt)
	print(wait2)
	GPIO.output(mod2, GPIO.HIGH)
	time.sleep(wait2)
	GPIO.output(mod2, GPIO.LOW)

def module3():
    #constant for watering
	k = 33.3333 #time in seconds for 1L of water
	kh = 3.33 #max additional seconds for humidity
	kt = 3.33 #max additional seconds for temperature
	#time between pump on and off
	wait3 = (k*abs((p2.value/32752)))+(((40-getHumid())/100)*kh)+(((getTemp()-21)/100)*kt)
	print(wait3)
	GPIO.output(mod3, GPIO.HIGH)
	time.sleep(wait3)
	GPIO.output(mod3, GPIO.LOW)

def module4():
    #constant for watering
	k = 33.3333 #time in seconds for 1L of water
	kh = 3.33 #max additional seconds for humidity
	kt = 3.33 #max additional seconds for temperature
	#time between pump on and off
	wait4 = (k*abs((p1.value/32752)))+(((40-getHumid())/100)*kh)+(((getTemp()-21)/100)*kt)
	print(wait4)
	GPIO.output(mod4, GPIO.HIGH)
	time.sleep(wait4)
	GPIO.output(mod4, GPIO.LOW)




module1()
module2()
module3()
module4()


