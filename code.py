## ---- TINKERTANK FRISBEE ---- ##
## ------ standard code ------- ##

## ---- Imports ---- ##
import time
import board
import digitalio
import touchio
import usb_hid
import neopixel
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
keyboard_HID = Keyboard(usb_hid.devices)

## ---- Definitions ---- ##

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
BLUE = (0, 20, 255)
BLACK = (0,0,0)
TEAL = (255, 0, 0)
pxColor = BLACK
NUMPIXELS = 160

R = [0 for x in range(NUMPIXELS+1)] 
G = [0 for x in range(NUMPIXELS+1)] 
B = [0 for x in range(NUMPIXELS+1)]

pinValueOld = [0,0,0,0,0,0,0,0,0,0,0,0] # previous pinValues
pinValue = [0,0,0,0,0,0,0,0,0,0,0,0]    # sum of pinValue Readings 
numReadings = 4			# number of readings before evaluating
threshold = 3    			# threshold to trigger key

pixels = neopixel.NeoPixel(board.GP22, NUMPIXELS+10, brightness=1, auto_write=False)

Pin10= digitalio.DigitalInOut(board.GP10)
Pin10.direction=digitalio.Direction.INPUT

Pin11= digitalio.DigitalInOut(board.GP11)
Pin11.direction=digitalio.Direction.INPUT

Pin12= digitalio.DigitalInOut(board.GP12)
Pin12.direction=digitalio.Direction.INPUT

Pin13= digitalio.DigitalInOut(board.GP13)
Pin13.direction=digitalio.Direction.INPUT

Pin14= digitalio.DigitalInOut(board.GP14)
Pin14.direction=digitalio.Direction.INPUT

Pin15= digitalio.DigitalInOut(board.GP15)
Pin15.direction=digitalio.Direction.INPUT

Pin16= digitalio.DigitalInOut(board.GP16)
Pin16.direction=digitalio.Direction.INPUT

Pin17= digitalio.DigitalInOut(board.GP17)
Pin17.direction=digitalio.Direction.INPUT

Pin18= digitalio.DigitalInOut(board.GP18)
Pin18.direction=digitalio.Direction.INPUT

Pin19= digitalio.DigitalInOut(board.GP19)
Pin19.direction=digitalio.Direction.INPUT

Pin20= digitalio.DigitalInOut(board.GP20)
Pin20.direction=digitalio.Direction.INPUT

Pin21= digitalio.DigitalInOut(board.GP21)
Pin21.direction=digitalio.Direction.INPUT

## functions ##

def sensePin(pin):    # digital Read pins and add to 'pinValue' variable
    global pinValue  
    if pin == 0:                      
        pinValue[0] += Pin10.value
    elif pin == 1:
        pinValue[1] += Pin11.value
    elif pin == 2:
        pinValue[2] += Pin12.value
    elif pin == 3:
        pinValue[3] += Pin13.value
    elif pin == 4:
        pinValue[4] += Pin14.value
    elif pin == 5:
        pinValue[5] += Pin15.value
    elif pin == 6:
        pinValue[6] += Pin16.value
    elif pin == 7:
        pinValue[7] += Pin17.value
    elif pin == 8:
        pinValue[8] += Pin18.value
    elif pin == 9:
        pinValue[9] += Pin19.value
    elif pin == 10:
        pinValue[10] += Pin20.value
    elif pin == 11:
        pinValue[11] += Pin21.value
        
def evaluatePins():             # evaluate 'pinValue'
    for i in range(12):
        global pinValue, pinValueOld, pxColor 
        
#         print (pinValue[i], end=" ")        # print raw sum values for debugging
        if pinValue[i] > threshold:  # see if pinValue is higher than threshold
            pinValue[i] = 1
            if i == 0: pxColor = (255, 0, 0)   #arrow keys: green
            elif i == 1: pxColor = (255, 255, 0)
            elif i == 2: pxColor = (255, 255, 255)
            elif i == 3: pxColor = (0, 255, 0)
            elif i == 4: pxColor = (0, 255, 255)
            elif i == 5: pxColor = (0, 0, 255)
            elif i == 6: pxColor = (255, 0, 255)
            elif i == 7: pxColor = (100, 0, 255)
            elif i == 8: pxColor = (0, 100, 255)
            elif i == 9: pxColor = (0, 0, 100)
            elif i == 10: pxColor = (255, 100, 0)
            elif i == 11: pxColor = (50, 20, 200)
            for l in range(3):
                R[l]=pxColor[0]
                G[l]=pxColor[1]
                B[l]=pxColor[2]

        else:
            pinValue[i] = 0					# not pressed
            pxColor = (0,0,0)
            R[0]=pxColor[0]
            G[0]=pxColor[1]
            B[0]=pxColor[2]            
       
        if pinValueOld[i] < pinValue[i]:
            if i == 0: keyboard_HID.press(Keycode.Q)
            elif i == 1: keyboard_HID.press(Keycode.W)
            elif i == 2: keyboard_HID.press(Keycode.E)
            elif i == 3: keyboard_HID.press(Keycode.R)
            elif i == 4: keyboard_HID.press(Keycode.T)
            elif i == 5: keyboard_HID.press(Keycode.Z)
            elif i == 6: keyboard_HID.press(Keycode.U)
            elif i == 7: keyboard_HID.press(Keycode.I)
            elif i == 8: keyboard_HID.press(Keycode.O)
            elif i == 9: keyboard_HID.press(Keycode.P)
            elif i == 10: keyboard_HID.press(Keycode.A)
            elif i == 11: keyboard_HID.press(Keycode.S)
            
        elif pinValueOld[i] > pinValue[i]:
            if i == 0: keyboard_HID.release(Keycode.Q)
            elif i == 1: keyboard_HID.release(Keycode.W)
            elif i == 2: keyboard_HID.release(Keycode.E)
            elif i == 3: keyboard_HID.release(Keycode.R)
            elif i == 4: keyboard_HID.release(Keycode.T)
            elif i == 5: keyboard_HID.release(Keycode.Z)
            elif i == 6: keyboard_HID.release(Keycode.U)
            elif i == 7: keyboard_HID.release(Keycode.I)
            elif i == 8: keyboard_HID.release(Keycode.O)
            elif i == 9: keyboard_HID.release(Keycode.P)
            elif i == 10: keyboard_HID.release(Keycode.A)
            elif i == 11: keyboard_HID.release(Keycode.S)

        pinValueOld[i] = pinValue[i]		# save previous value
        pinValue[i] = 0   					# reset RawValue



## ---- Code ---- ##
while True:
    
    for i in range(numReadings):	#read [10] times
        for j in range(12):	
            sensePin(j)		# read all 12 Pins
#         time.sleep(0.0001)

    evaluatePins()

    #shift array
    for k in range(NUMPIXELS):
        R[NUMPIXELS-k] = R[(NUMPIXELS-1)-k]
        G[NUMPIXELS-k] = G[(NUMPIXELS-1)-k]
        B[NUMPIXELS-k] = B[(NUMPIXELS-1)-k]
        pixels[k] = (R[k],G[k],B[k])
    pixels.show()

    
#     print('')   #for debugging
# 