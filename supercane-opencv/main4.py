import cv2

# Define the lower and upper bounds for each color in HSV color space
green_lower = (70, 50, 50)
green_upper = (90, 255, 255)
yellow_lower = (15, 39, 64)
yellow_upper = (35, 255, 255)
red_lower = (0, 70, 50)
red_upper = (10, 255, 255)
red_high_lower = (170, 70, 50)
red_high_upper = (180, 255, 255)

# Initialize the video stream
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Threshold the image to get binary images for each color
    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    # red_mask = cv2.inRange(hsv, red_lower, red_upper)
    red_mask = 0
    red_high_mask = cv2.inRange(hsv, red_high_lower, red_high_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)
    
    # Calculate the total number of green, yellow, and red pixels
    green_pixels = cv2.countNonZero(green_mask)
    yellow_pixels = cv2.countNonZero(yellow_mask)
    red_pixels = cv2.countNonZero(red_mask)
    red_high_pixels = cv2.countNonZero(red_high_mask)
    
    # Determine the color of the traffic light based on the number of pixels
    if green_pixels > yellow_pixels and green_pixels > (red_pixels + red_high_pixels):
        color = 'Green'
    elif yellow_pixels > green_pixels and yellow_pixels > (red_pixels + red_high_pixels):
        color = 'Yellow'
    else:
        color = 'Red'
    
    # Display the color on the frame
    cv2.putText(frame, color, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow('Traffic Light', frame)
    # cv2.imshow('Traffic Light', hsv)
    
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()
