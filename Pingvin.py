import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)
#GPIO.setup (20 , GPIO.OUT)
#GPIO.output (20, 1)
#time.sleep (11)
#GPIO.output (20 ,0)
#GPIO.cleanup(20)

ledNumberar = [24, 25, 8, 7, 12, 16, 20, 21]
def lightUp(ledNumber, period):
    GPIO.setup(ledNumberar[ledNumber], GPIO.OUT)
    GPIO.output(ledNumberar[ledNumber], 1)
    time.sleep(period)
    GPIO.output(ledNumberar[ledNumber], 0)

def darkUp(ledNumber, period):
    GPIO.setup(ledNumberar[ledNumber], GPIO.OUT)
    GPIO.output(ledNumberar[ledNumber], 0)
    time.sleep(period)
    GPIO.output(ledNumberar[ledNumber], 1)

def blink(ledNumber, blinkCount, blinkPeriod):
    i = 0
    while i < blinkCount:
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)
        i = i + 1

def runnigLight(count, period):
    i = 0
    j = 0
    for i in range(count):
        for j in range(8):
            lightUp(j, period)
            time.sleep(0)

def runningDark(count, period):
    for k in range(7):
        GPIO.setup(ledNumberar[k], GPIO.OUT)
        GPIO.output(ledNumberar[k], 1)
    i = 0
    j = 0
    for i in range(count):
        for j in range(8):
            darkUp(j, period)
            time.sleep(0)
    for k in range(8):
        GPIO.setup(ledNumberar[k], GPIO.OUT)
        GPIO.output(ledNumberar[k], 0)

def decToBinList(decNumber):
    binNum = [0] * 8
    for i in range(8):
        binNum[7 - i] = decNumber % 2
        decNumber = decNumber // 2
    return binNum

def lightNumber(number):
    binAr = decToBinList(number)
    for i in range(8):
        if binAr[i]:
             GPIO.setup(ledNumberar[i], GPIO.OUT)
             GPIO.output(ledNumberar[i], 1)
    time.sleep(1)
    for i in range(8):
        GPIO.setup(ledNumberar[i], GPIO.OUT)
        GPIO.output(ledNumberar[i], 0)

def arToNum(ar):
    num = 0
    for i in range(8):
        num = num + (2^i)*ar[i]

def moveAr(ar, dir):
    if dir > 0:
        temp = ar[0]
        for i in range (7):
            ar[i] = ar[i + dir]
        ar[7] = temp
    else:
        temp = ar[7]
        for i in range (7):
            ar[i] = ar[i + dir]
        ar[0] = temp
        temp = ar[0]
def runningPattern(pattern, direction):
    patAr = decToBinList(pattern)
    while True:
        lightNumber(pattern)
        pattern = arToNum(patAr)

#ledNumber = input()
#period = input()
blinkCount = 3
blinkPeriod = 3


#lightUp(ledNumber, period)
#blink(ledNumber, blinkCount, blinkPeriod)
#runnigLight(3, 1)
#runningDark(1, 0.5)
#print(decToBinList(127))
#lightNumber(127)
runningPattern(1, 1)