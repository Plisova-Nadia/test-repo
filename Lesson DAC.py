import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)

ledNumberar = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setup (ledNumberar, GPIO.OUT)

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

#ПРОГРАММА 1

try:
    value = 0
    while (value > -1):
        print ("Введите число (-1 для выхода)\n")
        value = int(input())
        num2dac(value)
except (Exception, ValueError):
    print ("Ошибка")
finally:
    GPIO.output(ledNumberar, 0)
    GPIO.cleanup()

#ПРОГРАММА 2

try:
    print ("Введите число повторений:")
    repetitionsNumber = int(input())
    r = 0
    while (r < repetitionsNumber):
        for i in range (0, 255):
            time.sleep(0.03)
            lightNumber(i)
        for i in range (255, 0, -1):
            time.sleep(0.03)
            lightNumber(i)
        r = r + 1
            
except (Exception, ValueError):
    print ("Ошибка")
finally:
    GPIO.output(ledNumberar, 0)
    GPIO.cleanup()