import cv2
import numpy as np

# Define the lower and upper bounds of the red color
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])

# Initialize the camera module
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    _, frame = cap.read()
    
    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Apply a mask to the frame to show only the red pixels
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Apply a median blur to remove noise from the image
    mask = cv2.medianBlur(mask, 5)
    
    # Find the contours of the objects in the masked image
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop through the contours and check if their size is large enough to be considered as a traffic light
    for contour in contours:
        area = cv2.contourArea(contour)
        
        if area > 1000:
            # Check the position of the traffic light within the frame to determine its color
            x, y, w, h = cv2.boundingRect(contour)
            
            if y < frame.shape[0] / 2:
                print("Red")
            elif y > frame.shape[0] / 2:
                print("Green")
            else:
                print("Yellow")
    
    # Display the original frame and the masked image
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    
    # Wait for the user to press 'q' to quit the program
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
