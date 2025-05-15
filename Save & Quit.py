import cv2

# Open the default camera (0 is usually the default camera)
cam = cv2.VideoCapture(0)

# Counter for saved images
image_counter = 1

while True:
    # Read an image from the camera
    cam_status, image = cam.read()

    # Display the image
    cv2.imshow('Output', image)

    key = cv2.waitKey(1)

    # Press 'q' to quit
    if key == ord('q'):
        break

    # Press 's' to save the image
    elif key == ord('s'):
        filename = f"Picture_{image_counter}.jpg"
        cv2.imwrite(filename, image)
        print(f"✅ Saved: {filename}")
        image_counter += 1

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
