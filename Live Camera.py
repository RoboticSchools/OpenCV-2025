import cv2

# Open the default camera (0 is usually the default camera)
cam = cv2.VideoCapture(0)

while True:
    # Read a image from the camera
    cam_status, image = cam.read()

    # Display the image
    cv2.imshow('Output', image)

    # Waits for 1 millisecond for a key press
    cv2.waitKey(1)

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
