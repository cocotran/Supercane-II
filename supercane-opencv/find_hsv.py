import cv2
import numpy as np

# Load the image
img = cv2.imread('input_red.jpg')

# Convert the image to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the mouse callback function to get the HSV value of the clicked pixel
def get_hsv(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = hsv_img[y, x]
        print('HSV value at (', x, ',', y, '):', pixel)

# Create a window to display the image
cv2.namedWindow('image')

# Set the mouse callback function for the window
cv2.setMouseCallback('image', get_hsv)

# Display the image
cv2.imshow('image', img)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
