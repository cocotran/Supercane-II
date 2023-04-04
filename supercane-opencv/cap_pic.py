import cv2

# Create a VideoCapture object to read from camera (index 0)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening camera")
    exit()

# Capture a frame
ret, frame = cap.read()

# Check if frame captured successfully
if not ret:
    print("Error capturing frame")
    exit()

# Save the captured frame as an image file
cv2.imwrite("input_red.jpg", frame)

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()