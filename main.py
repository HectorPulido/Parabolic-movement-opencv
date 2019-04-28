#Libraries
import cv2
import numpy as np
import math 

#Universal constant
DEGRETORAD = 0.0174533

#CV2 SETUP
img = np.zeros((400,800,3), np.uint8)
cv2.namedWindow('image')

#floor
cv2.rectangle(img,(0,380),(800,500),(100,255,100),1)

#Initial constants
initialPosition = (39, 380)
gravity = 9.8 * 0.1
initalSpeed = 300 * 0.1
angles = [20, 30, 40, 45, 50, 60, 70, 90]
anglesId = 0

#Problem variables
counter = 0
canonPosition = [initialPosition[0], initialPosition[1]]
velocity = [0.0,0.0]
angle = 20

while(1):
    #Angle set
    canonAngle = (angle + 90)  * DEGRETORAD

    #Initial image clone (avoid trail)
    _img = np.array(img, copy=True)  

    counter += 0.5

    #apply gravity
    velocity[1] += gravity

    #Apply speed
    canonPosition[0] += int(velocity[0])
    canonPosition[1] += int(velocity[1])

    #Collision with floor
    if canonPosition[1] >= 380:
        canonPosition[1] = 380
        velocity[0] = 0
        velocity[1] = 0

    for i in range(0, 100):
        x = initalSpeed * math.sin(canonAngle) * i + initialPosition[0]
        y = initalSpeed * math.cos(canonAngle) * i + 0.5 * gravity * (i ** 2) + initialPosition[1]

        cv2.circle(_img,(int(x), int(y)),1,(100,100,100), 5)
            
        if y > 380:
            break

    
    #
    _canonPosition = tuple(canonPosition)
    _canonPositionToDraw = (canonPosition[0] - initialPosition[0],
        (canonPosition[1] - initialPosition[1]) * -1)

    #Draw the canon ball
    cv2.circle(_img,_canonPosition,5,(0,0,255), 5)

    #LABELS 
    text = "Angle: " + str(angle)
    cv2.putText(_img, text, (10,25), 
        cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
    text = "Velocity: " + str(velocity)
    cv2.putText(_img, text, (10,50), 
        cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
    text = "Position: " + str(_canonPositionToDraw)
    cv2.putText(_img, text, (10,75), 
        cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
    text = "KeyArrows to change the angle"
    cv2.putText(_img, text, (10,90), 
        cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
    text = "Q to reset"
    cv2.putText(_img, text, (10,115), 
        cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
    text = "Spacebar to shoot"
    cv2.putText(_img, text, (10,140), 
        cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))

    cv2.imshow('image',_img)
    
    #Key pressed
    key = cv2.waitKey(20)

    #Print it on console
    if key != -1:
        print(key)

    #Arrow
    if key == 0: 
        anglesId += 1
        if anglesId >= len(angles):
            anglesId = 0
        angle = angles[anglesId]

    #Key A
    if key == 113:
        canonPosition = [initialPosition[0], initialPosition[1]]

    #Spacebar
    if key == 32:
        vectorPositionX = math.sin(canonAngle) * initalSpeed
        vectorPositionY = math.cos(canonAngle) * initalSpeed

        velocity = [vectorPositionX, vectorPositionY]
        #canonPosition[1] = 380
    
    #Escape
    if key == 27:
        break

cv2.destroyAllWindows()

