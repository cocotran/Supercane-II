import cv2
import numpy as np

# Set the focal length and known width of the object (in this case, a traffic light)
focal_length = 650
object_width = 9

# Initialize the camera module
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    _, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply a Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Detect edges using the Canny edge detection algorithm
    edges = cv2.Canny(blur, 50, 150)
    
    # Find contours of the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop through the contours and estimate the distance to the object
    for contour in contours:
        # Compute the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Only consider contours with a certain aspect ratio and size
        aspect_ratio = w / float(h)
        area = cv2.contourArea(contour)
        
        if aspect_ratio > 0.5 and aspect_ratio < 2.0 and area > 1000:
            # Compute the distance to the object using the width of the bounding box
            distance = (object_width * focal_length) / w
            
            # Draw the bounding box and distance on the frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Distance: {:.2f} cm".format(distance), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow("Frame", frame)
    
    # Wait for the user to press 'q' to quit the program
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()