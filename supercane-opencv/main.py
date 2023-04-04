import cv2
import numpy as np

# Set up the camera
cap = cv2.VideoCapture(0)

# Define the lower and upper bounds for the colors
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
lower_green = np.array([30, 100, 100])
upper_green = np.array([70, 80, 80])

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the image to get only the color of the traffic light
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Find the contours of the traffic light color regions
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Check which color has the most number of contours
    if len(contours_red) > len(contours_yellow) and len(contours_red) > len(contours_green):
        print("Traffic light color: RED")
    elif len(contours_yellow) > len(contours_red) and len(contours_yellow) > len(contours_green):
        print("Traffic light color: YELLOW")
    elif len(contours_green) > len(contours_red) and len(contours_green) > len(contours_yellow):
        print("Traffic light color: GREEN")

    # Display the resulting frames
    cv2.imshow('frame',frame)
    cv2.imshow('mask_red',mask_red)
    cv2.imshow('mask_yellow',mask_yellow)
    cv2.imshow('mask_green',mask_green)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()