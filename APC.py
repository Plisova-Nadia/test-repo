import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)

ledNumberar = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setup (ledNumberar, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 1)


def decToBinList(decNumber):
    binNum = [0] * 8
    for i in range(8):
        binNum[7 - i] = decNumber % 2
        decNumber = decNumber // 2
    return binNum

def lightNumber(number):
    GPIO.output(ledNumberar, 0)
    binAr = decToBinList(number)
    for i in range(8):
        if binAr[i]:             
             GPIO.output(ledNumberar[7-i], 1)


def binary ():
    p = 255
    l = 0
    while ((p - l) > 1):
        c = (p-l)/2
        lightNumber (c)
        time.sleep (0.1)
        if GPIO.input(4) == 1:
            p = c
        else:
            l = c
    if GPIO.input(4) == 1:
        print (c)
        return round(c) - 1
    else:
        return round(c)



#ПРОГРАММА 1

try:
    i = 1
    while i != 0:
        y = binary ()
        print ("Digital value: ", y, ", Analog value: ", round (y*3.3/256, 2))
            
except (Exception, ValueError):
    print ("Ошибка")
finally:
    GPIO.output(ledNumberar, 0)
    GPIO.cleanup()
