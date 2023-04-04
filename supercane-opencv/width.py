import cv2

# Load the Haar Cascade classifier for detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the input image
img = cv2.imread('input.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect the face and get the bounding box
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
x, y, w, h = faces[0]

# Draw the bounding box around the face
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Show the image with the bounding box
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the width of the bounding box in pixels
print('Width of bounding box:', w)