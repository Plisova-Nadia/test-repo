import time as t
import RPi.GPIO as GPIO
import numpy as np 
import matplotlib.pyplot as plt 
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

def num2dac(value):
    GPIO.output(ledNumberar, 0)
    binAr = decToBinList(value)
    for i in range(8):
        if binAr[i]:             
             GPIO.output(ledNumberar[7-i], 1)

def lightNumber(number):
    binAr = decToBinList(number)
    for i in range(8):
        if binAr[i]:
             GPIO.setup(ledNumberar[i], GPIO.OUT)
             GPIO.output(ledNumberar[i], 1)
    t.sleep(1)
    for i in range(8):
        GPIO.setup(ledNumberar[i], GPIO.OUT)
        GPIO.output(ledNumberar[i], 0)
 
def adc():
    start = 0; end = 255
    while start <= end:
        mid = (start + end) // 2
        num2pins(ledNumberar, mid)
        time.sleep(0.0003)
        if GPIO.input(in_chan) == 0:
            end = mid - 1
        else:
            start = mid + 1
    
    if end < 0:
        return start
    else:
        return end

try:
    t_start = t.time ()
    listV = []
    listT = []
    in_chan = 4
    maxV = 3.3
    outstr = "Digital value: {digital}, analog value: {analog} V"

    while adc () > 0: 
        GPIO.output(17, 0)
        print ("wait")
        t.sleep(1)

    t_start_m = t.time()
    GPIO.output(17,1) #high
    while True:
        #t_start_m = t.time()
        listV.append(adc())
        listT.append(t.time() - t_start)
        if listV[-1] >= 211:
            break

    GPIO.output(17,0) #low
    while True:
        #t_start_m = t.time()
        listV.append(adc())
        listT.append(t.time() - t_start)
        if listV[-1] == 0:
            break

    for i in range (len(listV)): listV[i]*=(3.29/210)
    plt.plot(listT, listV, "r. ")
    plt.show()
    print (len(listV)/10.0)

            
#except (Exception, ValueError):
   # print ("Ошибка")
finally:
    GPIO.output(ledNumberar, 0)
    GPIO.cleanup()