import cv2
import Hand_Tracking_Module as hm
import math
import map_function as mf
import serial
maping = mf.init.map_range
tracker=hm.handDetector()
cap=cv2.VideoCapture(0)


while True:

#==== Camera & Hand Tracking Module Setup ====
    success, img = cap.read()
    img = tracker.findHands(img=img)
    lmlist=tracker.findPosition(img, draw=False)

    if len(lmlist) !=0:

        #== Calculates Base (middleb to wrist) ==
        wrist_x=lmlist[0][1]
        wrist_y=lmlist[0][2]
        midb_x=lmlist[9][1]
        midb_y=lmlist[9][2]
        
        base=math.hypot(wrist_x-midb_x, wrist_y-midb_y)

#====== Finger Leght Calculation =====
        fingers = [0, 0, 0, 0, 0]
        i=1
        fingers_index=0
        while i<=17:
            #=== Calculate Thumb Leght ===
            if i == 1:
                tip_x = lmlist[4][1]
                tip_y = lmlist[4][2]
                base_x = lmlist[9][1]
                base_y = lmlist[9][2]
                finger_leght = math.hypot(tip_x-base_x,tip_y-base_y)/base
                finger_leght=maping(finger_leght, 0.3, 0.7, 0, 255)

            else:
            #=== Calculate Index, Middle, Ring, Pinky leght from base to tip ===
                tip_x = lmlist[i+3][1]
                tip_y =lmlist[i+3][2]
                base_x= lmlist[i][1]
                base_y=lmlist[i][2]
                finger_leght = math.hypot(tip_x-base_x,tip_y-base_y)/base
                finger_leght=maping(finger_leght, 0.2, 0.7, 0, 255)
            i+=4

    #==== Updates fingers list to current finger leght ====
            fingers[fingers_index] = finger_leght
            fingers_index+=1
    
    #==== Send Finger Leghts to Microcontroller via Serial Communication =====
      # Make sure to adjust usb port ('/dev/ttyACM0') according to where your microcontroller is connected to
        with serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1) as ser:
            message = f"{fingers[0]}, {fingers[1]}, {fingers[2]}, {fingers[3]}, {fingers[4]}\n"
            print(message)
            ser.write(message.encode('utf-8'))

# == Display Camera ==
    cv2.imshow('image', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release
cv2.destroyAllWindows
