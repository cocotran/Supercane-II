import cv2
import numpy as np

# Define the dimensions of the rectangular object (in cm)
rect_width = 16
rect_height = 10

# Get the focal length of the camera (in pixels)
focal_length = 650

# Start the camera capture
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 50, 150)

    # Find contours in the edge image
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours
    for contour in contours:
        # Approximate the contour with a rectangle
        x, y, w, h = cv2.boundingRect(contour)
        rect_area = w * h

        # Compute the distance to the rectangular object
        distance = (rect_width * focal_length) / w

        # Draw the rectangle and the distance on the frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, '{:.2f} cm'.format(distance), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Show the frame with the rectangles and distances
    cv2.imshow('frame', frame)

    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()
