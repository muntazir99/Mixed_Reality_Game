import cv2
import numpy as np
import board
import math

def hit_detect():

    lower_bound = np.array([0,0,100])
    upper_bound = np.array([80,80,255])


    cap = cv2.VideoCapture(1)   
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error reading Image")
            break

        # Perform color thresholding to isolate the circle
        mask = cv2.inRange(frame, lower_bound, upper_bound)

        contour_img, bounding_boxs, centers, radius = board.Contours(frame)
        if len(centers)<=2:
            continue
        elif len(centers)==4:    
            centers.sort(reverse=True)
            radius.sort(reverse=True)
            x1 = centers[0][0]
            y1 = centers[0][1]
            x2 = centers[2][0]
            y2 = centers[2][1]
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
            if distance<radius[0]:
                return "Hit"
            else:
                return "Miss"
        
        else:
            print("There are more than 2 contours found....Check kar")


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
