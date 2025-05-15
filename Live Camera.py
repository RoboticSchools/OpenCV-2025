import cv2

# Open the default camera (0 is usually the default camera)
cam = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a image from the camera
    cam_status, image = cam.read()
    
    if not cam_status:
        print("Error: Failed to capture image.")
        break

    # Display the image
    cv2.imshow('Output', image)

    key = cv2.waitKey(1)

    # Press 'q' to quit
    if  key == ord('q'):
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
